from flask import Flask, request, jsonify, redirect, send_file
from flask_cors import CORS
import argparse
import threading
import time
import base64
import tempfile
import os

from ai.model import AIModel
from data.dataset import Dataset
from utils.helpers import log_message


def create_app(model_container: dict):
    # static files are located in the 'static' folder next to this file
    import pathlib
    static_path = str(pathlib.Path(__file__).resolve().parent / 'static')
    app = Flask(__name__, static_folder=static_path)
    CORS(app)

    # Serve a premium static UI at /ui (no npm required)
    @app.route('/ui', methods=['GET'])
    def ui():
        # redirect to the static path, which Flask will serve from static_folder
        return redirect('/static/ui.html')

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "ok",
            "capabilities": {
                "image_generation": True,
                "pdf_creation": True,
                "text_analysis": True,
                "content_creation": True
            },
            "model_ready": model_container.get("model") is not None
        }), 200

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({
            "status": "Manus AI - Next-Generation AI Platform",
            "developer": "Marwen Rabai",
            "website": "https://marwen-rabai.netlify.app",
            "capabilities": [
                "Image Generation",
                "PDF Creation", 
                "Text Analysis",
                "Content Creation"
            ]
        }), 200

    @app.route("/predict", methods=["POST"])
    def predict():
        payload = request.get_json(force=True)
        if payload is None:
            return jsonify({"error": "invalid json"}), 400

        model = model_container.get("model")
        if model is None:
            return jsonify({"error": "model not ready"}), 503

        if "input" in payload:
            try:
                result = model.predict(payload["input"])
                
                # Handle different types of results
                if isinstance(result, dict) and result.get('type') in ['image', 'pdf', 'content', 'sentiment']:
                    return jsonify(result), 200
                else:
                    # Fallback for simple predictions
                    return jsonify({
                        "type": "prediction",
                        "prediction": int(result),
                        "input": payload["input"]
                    }), 200
                    
            except Exception as e:
                return jsonify({
                    "type": "error",
                    "error": str(e),
                    "input": payload["input"]
                }), 500

        if "features" in payload:
            try:
                pred = model.predict(payload["features"])
                return jsonify({
                    "type": "prediction",
                    "prediction": [int(x) for x in pred.tolist()],
                    "features": payload["features"]
                }), 200
            except Exception as e:
                return jsonify({
                    "type": "error",
                    "error": str(e),
                    "features": payload["features"]
                }), 500

        return jsonify({"error": "no input provided"}), 400

    @app.route("/download/<file_type>/<filename>", methods=["GET"])
    def download_file(file_type, filename):
        """Download generated files (PDFs, images)"""
        try:
            # Create a temporary directory for downloads
            temp_dir = tempfile.gettempdir()
            file_path = os.path.join(temp_dir, filename)
            
            if file_type == "pdf" and os.path.exists(file_path):
                return send_file(file_path, as_attachment=True, download_name=filename)
            elif file_type == "image" and os.path.exists(file_path):
                return send_file(file_path, as_attachment=True, download_name=filename)
            else:
                return jsonify({"error": "File not found"}), 404
                
        except Exception as e:
            return jsonify({"error": f"Download failed: {str(e)}"}), 500

    @app.route("/capabilities", methods=["GET"])
    def get_capabilities():
        """Get available AI capabilities"""
        return jsonify({
            "capabilities": {
                "image_generation": {
                    "enabled": True,
                    "description": "Generate visual content from text descriptions",
                    "examples": [
                        "Generate an image of a futuristic city",
                        "Create a visualization of AI concepts",
                        "Draw a nature-inspired pattern"
                    ]
                },
                "pdf_creation": {
                    "enabled": True,
                    "description": "Create professional PDF documents and reports",
                    "examples": [
                        "Create a PDF report about AI trends",
                        "Generate a business analysis document",
                        "Make a technical specification PDF"
                    ]
                },
                "text_analysis": {
                    "enabled": True,
                    "description": "Analyze text sentiment and extract insights",
                    "examples": [
                        "Analyze sentiment: I love this product!",
                        "Extract key insights from text",
                        "Determine emotional tone of content"
                    ]
                },
                "content_creation": {
                    "enabled": True,
                    "description": "Generate creative stories and articles",
                    "examples": [
                        "Write a story about AI friendship",
                        "Create an article about technology trends",
                        "Generate creative content about robots"
                    ]
                }
            },
            "developer": {
                "name": "Marwen Rabai",
                "website": "https://marwen-rabai.netlify.app",
                "description": "Next-Generation AI Platform Developer"
            }
        }), 200

    return app


def start_model_background(data_path: str | None = None):
    log_message("Starting advanced AI model training for serve mode...")
    ds = Dataset(data_path)
    df = ds.load_data()
    X, y = ds.preprocess_data(df)
    m = AIModel()
    m.train_model(X, y)
    log_message("Advanced AI model ready with multiple capabilities")
    return m


def run_server(host: str = "127.0.0.1", port: int = 5000, data_path: str | None = None):
    # Train model in background thread and start Flask with it
    model_container = {}

    def trainer():
        model_container["model"] = start_model_background(data_path)

    t = threading.Thread(target=trainer, daemon=True)
    t.start()

    # Create app that will reference model_container dynamically
    app = create_app(model_container)
    
    log_message(f"Starting Manus AI server on http://{host}:{port}")
    log_message("Advanced capabilities enabled: Image Generation, PDF Creation, Text Analysis, Content Creation")
    log_message("Developer: Marwen Rabai - https://marwen-rabai.netlify.app")
    
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manus AI - Next-Generation AI Platform")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=5000, help="Port to bind the server to")
    parser.add_argument("--data", dest="data_path", default=None, help="Path to custom dataset")
    args = parser.parse_args()
    run_server(host=args.host, port=args.port, data_path=args.data_path)

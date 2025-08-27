import os
import argparse
from ai.model import AIModel
from data.dataset import Dataset
from utils.helpers import log_message


def run_train(data_path: str | None, non_interactive: bool):
    log_message("Initializing training...")
    dataset = Dataset(data_path)
    df = dataset.load_data()
    X, y = dataset.preprocess_data(df)

    model = AIModel()
    model.train_model(X, y)
    log_message("Training complete.")
    if non_interactive:
        return

    log_message("Enter queries (type 'exit' to quit).")
    while True:
        try:
            user_input = input("Query> ")
        except (EOFError, KeyboardInterrupt):
            log_message("Exiting...")
            break
        if user_input.strip().lower() in ("exit", "quit"):
            log_message("Exiting the application...")
            break
        try:
            pred = model.predict(user_input)
            log_message(f"Prediction: {pred}")
        except Exception as e:
            log_message(f"Error during prediction: {e}")


def main(argv: list | None = None):
    parser = argparse.ArgumentParser(description="Manus AI CLI")
    parser.add_argument("mode", choices=["train", "serve", "evaluate"], default="train", nargs="?")
    parser.add_argument("--data", "-d", dest="data_path", help="Path or URL to dataset (csv/json/parquet)")
    parser.add_argument("--no-interactive", dest="no_interactive", action="store_true", help="Run non-interactive (train only)")
    args = parser.parse_args(argv)

    if args.mode == "train":
        run_train(args.data_path, args.no_interactive)
    elif args.mode == "serve":
        # Start server by running the server.py script directly so imports work
        from subprocess import Popen
        import sys
        import os
        script = os.path.abspath(os.path.join(os.path.dirname(__file__), 'server.py'))
        cmd = [sys.executable, script]
        if args.data_path:
            cmd += ['--data', args.data_path]
        log_message(f"Starting server with command: {' '.join(cmd)}")
        # set cwd to manus-ai project root
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        Popen(cmd, cwd=project_root)
        log_message('Server started (subprocess).')
    else:
        log_message(f"Mode '{args.mode}' is not yet implemented. Use 'train' for now.")


if __name__ == "__main__":
    main()
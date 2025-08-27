# Manus AI - Next-Generation AI Platform

**Developed by [Marwen Rabai](https://marwen-rabai.netlify.app)**

Manus AI is a premium, next-generation artificial intelligence platform featuring Apple Vision Pro-inspired design and advanced AI capabilities. Experience the future of AI with stunning visuals, intelligent content generation, and seamless user interactions.

## ✨ Premium Features

### 🎨 **Advanced AI Capabilities**
- **Image Generation**: Create stunning visualizations from text descriptions
- **PDF Creation**: Generate professional documents and reports
- **Text Analysis**: Advanced sentiment analysis and content insights
- **Content Creation**: AI-powered storytelling and article generation

### 🎯 **Apple Vision Pro-Inspired Design**
- **Glass Morphism UI**: Premium glass-like interface elements
- **Animated Backgrounds**: Dynamic particle effects and gradients
- **Responsive Design**: Seamless experience across all devices
- **Premium Typography**: Inter font family for modern aesthetics

### 🚀 **Next-Level User Experience**
- **Intelligent Intent Detection**: Automatically routes requests to appropriate AI capabilities
- **Real-time Processing**: Instant feedback and status updates
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Professional Output**: High-quality results with detailed formatting

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Windows 10/11 (PowerShell)
- Internet connection (for initial package installation)

### Installation

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/yourusername/manus-ai.git
   cd manus-ai
   ```

2. **One-click installation and launch (Windows):**
   ```powershell
   # Double-click run.ps1 or run from PowerShell
   .\run.ps1 serve
   ```

3. **Manual installation:**
   ```powershell
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   .\.venv\Scripts\Activate.ps1
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the application
   python src/main.py serve
   ```

## 🌟 Premium Interface

### Access the Premium UI
1. **Start the server:**
   ```powershell
   .\run.ps1 serve
   ```

2. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000/ui
   ```

3. **Experience the Premium Features:**
   - **Glass morphism cards** with hover effects
   - **Animated status indicators** with real-time updates
   - **Interactive capability cards** for quick access
   - **Premium color scheme** with gradients and transparency
   - **Smooth animations** and transitions

## 🎨 AI Capabilities

### Image Generation
Generate stunning visualizations from text descriptions:
```
"Generate an image of a futuristic AI city with flying cars and neon lights"
"Create a visualization of machine learning concepts"
"Draw a nature-inspired pattern with mathematical precision"
```

### PDF Creation
Create professional documents and reports:
```
"Create a PDF report about the latest AI trends in 2024"
"Generate a business analysis document"
"Make a technical specification PDF"
```

### Text Analysis
Advanced sentiment analysis and content insights:
```
"Analyze this text sentiment: I love this new AI technology!"
"Extract key insights from this content"
"Determine the emotional tone of this text"
```

### Content Creation
AI-powered storytelling and article generation:
```
"Write a creative story about a robot learning to paint"
"Create an article about technology trends"
"Generate content about AI friendship"
```

## 📖 Usage Guide

### Web Interface (Recommended)

1. **Start the server:**
   ```powershell
   .\run.ps1 serve
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/ui
   ```

3. **Using the Premium Interface:**
   - Wait for the model to finish training (status will show "Model: ready")
   - Enter your query in the premium text area
   - Click "Generate" to get AI-powered results
   - Use "Health Check" to verify system status
   - Explore different AI capabilities with the interactive cards

### Command Line Interface

1. **Training mode (with interactive predictions):**
   ```powershell
   python src/main.py train
   ```

2. **Training mode (non-interactive):**
   ```powershell
   python src/main.py train --no-interactive
   ```

3. **Using custom dataset:**
   ```powershell
   python src/main.py train --data path/to/your/dataset.csv
   ```

### API Endpoints

When the server is running, you can access these premium endpoints:

- `GET /` - Server status and capabilities
- `GET /health` - Health check with capability status
- `GET /ui` - Premium web interface
- `GET /capabilities` - Detailed AI capabilities information
- `POST /predict` - Advanced AI predictions
- `GET /download/<type>/<filename>` - Download generated files

**Example API usage:**
```bash
# Health check with capabilities
curl http://127.0.0.1:5000/health

# Get capabilities information
curl http://127.0.0.1:5000/capabilities

# Make advanced prediction
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": "Generate an image of a futuristic city"}'
```

## 🔧 Configuration

### Supported Data Formats
- CSV files (.csv)
- JSON files (.json)
- Parquet files (.parquet)
- Remote URLs (http/https)

### Dataset Requirements
- Features should be numeric columns
- Target column should be named 'target'
- If no target column exists, a default target (zeros) will be created

### Advanced Model Configuration
The application uses:
- **Multi-Capability AI**: Intelligent routing to appropriate AI functions
- **Image Generation**: Matplotlib-based visualizations with custom styling
- **PDF Creation**: ReportLab-powered document generation
- **Text Processing**: TF-IDF vectorizer with sentiment analysis
- **Content Creation**: Template-based creative content generation

## 🛠️ Advanced Usage

### Custom Dataset Example
```powershell
# Train with local CSV file
python src/main.py train --data data/my_dataset.csv

# Train with remote dataset
python src/main.py train --data https://example.com/dataset.csv

# Start server with custom dataset
python src/main.py serve --data data/my_dataset.csv
```

### Desktop Shortcuts (Windows)
Create convenient shortcuts for easy access:

```powershell
# Create desktop shortcut
.\tools\create_shortcut.ps1

# Create startup task (requires admin)
.\tools\create_startup_task.ps1
```

### Development Mode
```powershell
# Run tests
python -m pytest tests/

# Install in development mode
pip install -e .
```

## 🎨 Design Philosophy

### Apple Vision Pro Inspiration
- **Glass Morphism**: Translucent elements with backdrop blur
- **Dynamic Gradients**: Smooth color transitions and depth
- **Premium Typography**: Inter font family for modern aesthetics
- **Micro-interactions**: Subtle animations and hover effects
- **Responsive Layout**: Adaptive design for all screen sizes

### Premium User Experience
- **Intuitive Navigation**: Clear visual hierarchy and logical flow
- **Real-time Feedback**: Instant status updates and progress indicators
- **Error Handling**: Graceful error messages with helpful suggestions
- **Accessibility**: High contrast and readable text throughout

## 📁 Project Structure

```
manus-ai/
├── src/
│   ├── main.py              # Main CLI entry point
│   ├── server.py            # Enhanced Flask web server
│   ├── static/
│   │   └── ui.html          # Premium web interface
│   ├── ai/
│   │   └── model.py         # Advanced AI model with multiple capabilities
│   ├── data/
│   │   └── dataset.py       # Data loading and preprocessing
│   └── utils/
│       └── helpers.py       # Utility functions
├── tools/
│   ├── create_shortcut.ps1  # Windows shortcut creator
│   └── create_startup_task.ps1  # Windows startup task
├── tests/                   # Test files
├── requirements.txt         # Enhanced Python dependencies
├── run.ps1                 # One-click launcher
└── README.md               # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **Port 5000 already in use:**
   ```powershell
   # Use different port
   python src/server.py --port 5001
   ```

2. **Dependencies not found:**
   ```powershell
   # Reinstall requirements
   pip install -r requirements.txt --force-reinstall
   ```

3. **Virtual environment issues:**
   ```powershell
   # Remove and recreate virtual environment
   Remove-Item -Recurse -Force .venv
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. **Permission errors (Windows):**
   - Run PowerShell as Administrator
   - Check Windows Defender settings
   - Ensure execution policy allows scripts

### Logs and Debugging
- Check console output for error messages
- Server logs appear in the terminal
- Model training progress is displayed in real-time

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👨‍💻 Developer

**Marwen Rabai**
- **Website**: [marwen-rabai.netlify.app](https://marwen-rabai.netlify.app)
- **Description**: Next-Generation AI Platform Developer
- **Specialties**: AI/ML, Full-Stack Development, UI/UX Design

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the console output for error messages
3. Ensure all dependencies are properly installed
4. Try running with a fresh virtual environment

---

**Experience the future of AI with Manus AI - Where Premium Design Meets Advanced Intelligence! 🚀**

*Developed with ❤️ by Marwen Rabai*
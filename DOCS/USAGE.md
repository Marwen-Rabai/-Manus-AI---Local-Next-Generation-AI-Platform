# Manus AI - Complete Usage Guide

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Web Interface](#web-interface)
4. [Command Line Interface](#command-line-interface)
5. [API Usage](#api-usage)
6. [Custom Datasets](#custom-datasets)
7. [Advanced Configuration](#advanced-configuration)
8. [Troubleshooting](#troubleshooting)
9. [Examples](#examples)

## 🚀 Quick Start

### Prerequisites
- **Operating System:** Windows 10/11
- **Python:** 3.8 or higher
- **PowerShell:** Built into Windows
- **Internet:** Required for initial package installation

### One-Click Launch (Recommended)
1. **Download or clone** the Manus AI repository
2. **Navigate** to the project folder
3. **Double-click** `run.ps1` or run from PowerShell:
   ```powershell
   .\run.ps1 serve
   ```
4. **Open your browser** and go to: `http://127.0.0.1:5000/ui`
5. **Wait** for the model to finish training (status will show "Model: ready")
6. **Start making predictions!**

## 📦 Installation

### Method 1: One-Click Installation (Windows)
```powershell
# Navigate to project directory
cd manus-ai

# Run the launcher
.\run.ps1 serve
```

The launcher will automatically:
- Create a virtual environment
- Install all dependencies
- Start the web server
- Open the interface in your browser

### Method 2: Manual Installation
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

## 🌐 Web Interface

### Getting Started
1. **Start the server:**
   ```powershell
   .\run.ps1 serve
   ```

2. **Access the interface:**
   - Open your web browser
   - Navigate to: `http://127.0.0.1:5000/ui`

3. **Wait for initialization:**
   - The status bar will show "Model: starting..."
   - Once ready, it will change to "Model: ready"
   - The Predict button will become enabled

### Using the Interface

#### Making Predictions
1. **Enter your query** in the text box
2. **Click "Predict"** or press Enter
3. **View results** in the output section

#### Example Queries
- "Is this positive?"
- "test query"
- "Hello world"
- "AI prediction"
- "Machine learning"

#### Available Actions
- **🔮 Predict:** Make AI predictions
- **💓 Health Check:** Verify server status
- **🗑️ Clear:** Clear input and output

### Interface Features
- **Real-time status** monitoring
- **Responsive design** for mobile devices
- **Example queries** for quick testing
- **Error handling** with clear messages
- **Loading indicators** during processing

## 💻 Command Line Interface

### Training Mode
```powershell
# Interactive training with predictions
python src/main.py train

# Non-interactive training only
python src/main.py train --no-interactive

# Training with custom dataset
python src/main.py train --data path/to/dataset.csv
```

### Server Mode
```powershell
# Start web server
python src/main.py serve

# Start server with custom dataset
python src/main.py serve --data path/to/dataset.csv
```

### CLI Examples
```powershell
# Basic training
python src/main.py train

# Training with remote dataset
python src/main.py train --data https://example.com/data.csv

# Start server on different port
python src/server.py --port 5001
```

## 🔌 API Usage

### Endpoints

#### Health Check
```bash
GET /health
```
**Response:**
```json
{
  "status": "ok"
}
```

#### Server Status
```bash
GET /
```
**Response:**
```json
{
  "status": "manus-ai server"
}
```

#### Make Prediction
```bash
POST /predict
Content-Type: application/json

{
  "input": "your query here"
}
```
**Response:**
```json
{
  "prediction": 1
}
```

### API Examples

#### Using curl
```bash
# Health check
curl http://127.0.0.1:5000/health

# Make prediction
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": "Is this positive?"}'
```

#### Using Python requests
```python
import requests

# Health check
response = requests.get('http://127.0.0.1:5000/health')
print(response.json())

# Make prediction
data = {'input': 'Is this positive?'}
response = requests.post('http://127.0.0.1:5000/predict', json=data)
print(response.json())
```

#### Using JavaScript fetch
```javascript
// Health check
fetch('/health')
  .then(response => response.json())
  .then(data => console.log(data));

// Make prediction
fetch('/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({input: 'Is this positive?'})
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📊 Custom Datasets

### Supported Formats
- **CSV files** (.csv)
- **JSON files** (.json)
- **Parquet files** (.parquet)
- **Remote URLs** (http/https)

### Dataset Requirements
- **Features:** Numeric columns
- **Target:** Column named 'target'
- **Missing target:** Will create default target (zeros)

### Example Dataset Structure
```csv
feature1,feature2,feature3,target
1.2,3.4,5.6,1
2.1,4.3,6.7,0
3.0,5.2,7.8,1
```

### Using Custom Datasets
```powershell
# Local CSV file
python src/main.py train --data data/my_dataset.csv

# Remote dataset
python src/main.py train --data https://example.com/dataset.csv

# JSON dataset
python src/main.py train --data data/my_dataset.json

# Parquet dataset
python src/main.py train --data data/my_dataset.parquet
```

## ⚙️ Advanced Configuration

### Server Configuration
```powershell
# Custom host and port
python src/server.py --host 0.0.0.0 --port 8080

# Custom dataset with server
python src/server.py --data data/custom.csv --port 5001
```

### Model Configuration
The application uses:
- **Algorithm:** Logistic Regression with StandardScaler
- **Text Processing:** TF-IDF vectorizer (if text column present)
- **Fallback:** Hash-based feature extraction for text input

### Environment Variables
```powershell
# Set custom port
$env:MANUS_PORT = "5001"
python src/server.py

# Set custom host
$env:MANUS_HOST = "0.0.0.0"
python src/server.py
```

## 🛠️ Windows Integration

### Desktop Shortcuts
```powershell
# Create desktop shortcut
.\tools\create_shortcut.ps1
```

### Auto-Start (Requires Admin)
```powershell
# Create startup task
.\tools\create_startup_task.ps1
```

### PowerShell Profile Integration
Add to your PowerShell profile:
```powershell
# Add to $PROFILE
function Start-ManusAI {
    Set-Location "C:\path\to\manus-ai"
    .\run.ps1 serve
}
```

## 🔍 Troubleshooting

### Common Issues

#### Port Already in Use
```powershell
# Use different port
python src/server.py --port 5001
```

#### Dependencies Not Found
```powershell
# Reinstall requirements
pip install -r requirements.txt --force-reinstall

# Or recreate virtual environment
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### Permission Errors
- Run PowerShell as Administrator
- Check Windows Defender settings
- Ensure execution policy allows scripts:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

#### Model Not Training
- Check console output for error messages
- Ensure dataset format is correct
- Verify all dependencies are installed

### Debug Mode
```powershell
# Enable debug logging
$env:FLASK_ENV = "development"
python src/server.py
```

### Logs and Monitoring
- **Console output:** Real-time training progress
- **Server logs:** HTTP requests and errors
- **Model status:** Available via health endpoint

## 📝 Examples

### Basic Usage Examples

#### 1. Quick Start with Web Interface
```powershell
# Start server
.\run.ps1 serve

# Open browser to http://127.0.0.1:5000/ui
# Enter query: "Is this positive?"
# Click Predict
```

#### 2. Command Line Training
```powershell
# Start interactive training
python src/main.py train

# Enter queries when prompted
# Type 'exit' to quit
```

#### 3. Custom Dataset Training
```powershell
# Create sample dataset
@"
feature1,feature2,target
1.0,2.0,1
2.0,3.0,0
3.0,4.0,1
"@ | Out-File -FilePath "sample.csv" -Encoding UTF8

# Train with custom dataset
python src/main.py train --data sample.csv
```

#### 4. API Integration
```python
import requests
import time

# Wait for server to start
time.sleep(5)

# Health check
response = requests.get('http://127.0.0.1:5000/health')
print(f"Server status: {response.json()}")

# Make predictions
queries = ["Hello", "Is this positive?", "test query"]
for query in queries:
    response = requests.post('http://127.0.0.1:5000/predict', 
                           json={'input': query})
    result = response.json()
    print(f"Query: {query} -> Prediction: {result['prediction']}")
```

### Advanced Examples

#### 1. Batch Processing
```python
import requests
import pandas as pd

# Load data
df = pd.read_csv('queries.csv')

# Process in batch
results = []
for query in df['query']:
    response = requests.post('http://127.0.0.1:5000/predict', 
                           json={'input': query})
    results.append(response.json()['prediction'])

# Save results
df['prediction'] = results
df.to_csv('results.csv', index=False)
```

#### 2. Custom Server Configuration
```python
# Custom server script
from src.server import run_server

# Run with custom settings
run_server(host='0.0.0.0', port=8080, data_path='custom_data.csv')
```

#### 3. Integration with Other Tools
```python
# Flask integration
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    text = request.json['text']
    
    # Send to Manus AI
    response = requests.post('http://127.0.0.1:5000/predict', 
                           json={'input': text})
    
    return {'result': response.json()['prediction']}

if __name__ == '__main__':
    app.run(port=5001)
```

## 📚 Additional Resources

### Documentation Files
- `README.md` - Main project documentation
- `requirements.txt` - Python dependencies
- `run.ps1` - One-click launcher

### Project Structure
```
manus-ai/
├── src/                    # Source code
│   ├── main.py            # CLI entry point
│   ├── server.py          # Web server
│   ├── static/ui.html     # Web interface
│   ├── ai/model.py        # AI model
│   ├── data/dataset.py    # Data handling
│   └── utils/helpers.py   # Utilities
├── tools/                  # Helper scripts
├── tests/                  # Test files
└── DOCS/                   # Documentation
```

### Getting Help
1. Check the troubleshooting section
2. Review console output for errors
3. Verify all dependencies are installed
4. Try with a fresh virtual environment
5. Check the project repository for updates

---

**Happy AI Development! 🚀**

For more information, visit the main README.md file or check the project repository.

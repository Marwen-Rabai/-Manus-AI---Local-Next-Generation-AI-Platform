# 🚀 Manus AI - Quick Start Guide

## ⚡ One-Click Launch
```powershell
# Double-click run.ps1 or run from PowerShell
.\run.ps1 serve
```

## 🌐 Access the Interface
1. **Wait** for the server to start
2. **Open browser** to: `http://127.0.0.1:5000/ui`
3. **Wait** for "Model: ready" status
4. **Start making predictions!**

## 💡 Quick Examples
- **Query:** "Is this positive?"
- **Query:** "Hello world"
- **Query:** "test query"

## 🔧 Common Commands
```powershell
# Start web server
.\run.ps1 serve

# Command line training
python src/main.py train

# Health check
curl http://127.0.0.1:5000/health
```

## 🆘 Need Help?
- Check `README.md` for full documentation
- Check `DOCS/USAGE.md` for detailed usage guide
- Review console output for error messages

## 📁 Key Files
- `run.ps1` - One-click launcher
- `start.bat` - Alternative launcher
- `src/static/ui.html` - Web interface
- `src/server.py` - Web server

---
**Happy AI Development! 🤖**

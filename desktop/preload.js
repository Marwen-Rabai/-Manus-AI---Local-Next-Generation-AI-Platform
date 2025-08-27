const { contextBridge, ipcRenderer } = require('electron')
const { spawn } = require('child_process')
const path = require('path')

let backend = null

contextBridge.exposeInMainWorld('backend', {
  start: (onStarted) => {
    if (backend) return
    // prefer repository root .venv python
    const py = process.platform === 'win32' ? path.join(__dirname, '..', '..', '.venv', 'Scripts', 'python.exe') : path.join(__dirname, '..', '..', '.venv', 'bin', 'python')
    // server script path
    const script = path.join(__dirname, '..', 'src', 'server.py')
    backend = spawn(py, [script, '--host', '127.0.0.1', '--port', '5000'], { cwd: path.join(__dirname, '..') })
    backend.stdout.on('data', (data) => {
      console.log('PY:', data.toString())
      if (onStarted) onStarted(data.toString())
    })
    backend.stderr.on('data', (data) => console.error('PYERR:', data.toString()))
  },
  stop: () => {
    if (!backend) return
    backend.kill()
    backend = null
  }
})

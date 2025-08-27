Param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$ScriptArgs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$venv = Join-Path $root '.venv'
$python = Join-Path $venv 'Scripts\python.exe'
$activate = Join-Path $venv 'Scripts\Activate.ps1'

Write-Host "[run.ps1] repo root: $root"

if (-not (Test-Path $venv)) {
    Write-Host "[run.ps1] .venv not found — creating virtual environment..."
    python -m venv $venv
}

if (Test-Path $activate) {
    Write-Host "[run.ps1] Activating .venv..."
    # dot-source so activation modifies this session
    . $activate
} else {
    Write-Host "[run.ps1] Activation script not found, will call venv python directly."
}

# Check for a key package (sklearn); if missing, install requirements
Write-Host "[run.ps1] Verifying required packages..."
try {
    & $python -c 'import importlib.util, sys; sys.exit(0 if importlib.util.find_spec("sklearn") else 1)'
} catch {
    # Keep going; check exit code below
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "[run.ps1] Required packages missing — installing from requirements.txt (this may take a while)..."
    & $python -m pip install --upgrade pip
    & $python -m pip install -r (Join-Path $root 'requirements.txt')
} else {
    Write-Host "[run.ps1] Required packages present."
}

# Default to 'train' if no args provided
if (($ScriptArgs -eq $null) -or ($ScriptArgs.Count -eq 0)) {
    $ScriptArgs = @('train')
}

Write-Host "[run.ps1] Running: $python src\main.py $($ScriptArgs -join ' ')"
& $python (Join-Path $root 'src\main.py') $ScriptArgs

exit $LASTEXITCODE
# One-click launcher for Manus AI on Windows PowerShell
# Usage: double-click this file or run it from PowerShell

$ErrorActionPreference = 'Stop'

# Create venv if missing
if (-not (Test-Path -Path '.venv')) {
    python -m venv .venv
}

# Activate venv
. .\.venv\Scripts\Activate.ps1

# Install requirements if not installed (quick check)
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip not found in venv. Exiting." -ForegroundColor Red
    exit 1
}

pip install -r requirements.txt

# Run the app
python src/main.py

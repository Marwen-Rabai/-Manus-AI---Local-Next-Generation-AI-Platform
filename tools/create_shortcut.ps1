Param(
    [string]$Target = "$PWD\run.ps1",
    [string]$ShortcutPath = "$env:UserProfile\Desktop\ManusAI.lnk"
)

$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut($ShortcutPath)
$shortcut.TargetPath = 'powershell.exe'
$shortcut.Arguments = "-NoExit -ExecutionPolicy Bypass -File `"$Target`" serve"
$shortcut.WorkingDirectory = (Split-Path $Target)
$shortcut.WindowStyle = 1
$shortcut.IconLocation = "$PWD\manus-ai.ico"
$shortcut.Save()

Write-Host "Shortcut created: $ShortcutPath"

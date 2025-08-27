Param(
    [string]$TaskName = 'ManusAI-Server',
    [string]$Script = "$PWD\run.ps1"
)

$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$Script`" serve"
$trigger = New-ScheduledTaskTrigger -AtLogOn
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -RunLevel LeastPrivilege -Force

Write-Host "Scheduled task '$TaskName' registered to run at logon."

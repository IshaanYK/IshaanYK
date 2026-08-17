# Strict mode
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$TargetScript = Join-Path $ScriptDir "auto_streak.ps1"
$TaskName = "IshaanYK_DailyGitHubStreak"

Write-Output "=========================================================="
Write-Output "[*] Setting up Windows Task Scheduler for Daily GitHub Streak"
Write-Output "=========================================================="

try {
    # Check if task already exists and remove
    $existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($null -ne $existing) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Output "[INFO] Removed previous scheduled task registration."
    }

    # Create Action (Execute PowerShell script hiddenly)
    $Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -File `"$TargetScript`""

    # Create Trigger (Daily at 10:00 AM)
    $Trigger = New-ScheduledTaskTrigger -Daily -At 10:00AM

    # Create Settings
    $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

    # Register Task
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Automated daily GitHub contribution and streak maintainer for IshaanYK" | Out-Null

    Write-Output "[OK] Scheduled task '$TaskName' registered successfully!"
    Write-Output "[INFO] It will automatically run every day at 10:00 AM in the background."
    Write-Output "=========================================================="
    exit 0
}
catch {
    Write-Warning "[ERROR] Failed to register task: $_"
    Write-Output "[TIP] Please run PowerShell as Administrator to register scheduled tasks."
    exit 1
}

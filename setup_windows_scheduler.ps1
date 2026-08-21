# Strict mode
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$TargetScript = Join-Path $ScriptDir "auto_streak.ps1"
$TaskName = "IshaanYK_DailyGitHubStreak"

Write-Output "=========================================================="
Write-Output "[*] Setting up Resilient Windows Task Scheduler for Daily Streak"
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

    # Create Trigger (Daily starting at 09:00 AM, repeating every 4 hours for 1 day)
    $Trigger = New-ScheduledTaskTrigger -Daily -At 09:00AM
    $Trigger.Repetition = (New-ScheduledTaskTrigger -Once -At 09:00AM -RepetitionInterval (New-TimeSpan -Hours 4) -RepetitionDuration (New-TimeSpan -Days 1)).Repetition

    # Create Settings (Start when available, run on battery or plugged in)
    $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -MultipleInstances IgnoreNew

    # Register Task
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Resilient automated multi-commit GitHub streak engine for IshaanYK" | Out-Null

    Write-Output "[OK] Scheduled task '$TaskName' registered successfully!"
    Write-Output "[INFO] Repeating trigger active (every 4 hours, start when available)."
    Write-Output "=========================================================="
    exit 0
}
catch {
    Write-Warning "[ERROR] Failed to register task: $_"
    exit 1
}

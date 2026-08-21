# Strict mode and error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# Determine script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PusherScript = Join-Path $ScriptDir "scripts\random_streak_pusher.py"

Write-Output "=========================================================="
Write-Output "[*] IshaanYK GitHub Multi-Commit Streak & Code Engine"
Write-Output "=========================================================="

try {
    Set-Location -Path $ScriptDir

    if (Test-Path $PusherScript) {
        Write-Output "[*] Launching Randomized Daily Multi-Commit Engine..."
        # Random commit count between 5 and 20
        $randomCount = Get-Random -Minimum 5 -Maximum 21
        Write-Output "[*] Selected random target commit batch: $randomCount commits"
        & python $PusherScript $randomCount
    }
    else {
        Write-Warning "[WARN] Pusher script not found at $PusherScript"
    }

    Write-Output "=========================================================="
    Write-Output "[OK] All streak tasks completed successfully!"
    Write-Output "=========================================================="
    exit 0
}
catch {
    Write-Warning "[ERROR] Failed to execute auto streak: $_"
    exit 1
}

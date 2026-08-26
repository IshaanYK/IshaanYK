# Strict mode and error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# Determine script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PusherScript = Join-Path $ScriptDir "scripts\random_streak_pusher.py"
$LogDir = Join-Path $ScriptDir "data"
$LogFile = Join-Path $LogDir "auto_streak.log"

if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

function Log-Msg {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$timestamp] $Message"
    Write-Output $line
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
}

Log-Msg "=========================================================="
Log-Msg "[*] IshaanYK GitHub Multi-Commit Streak & Code Engine"
Log-Msg "=========================================================="

try {
    Set-Location -Path $ScriptDir

    # Ensure verified GitHub account email is present
    if (-not $env:GIT_COMMIT_EMAIL) {
        $env:GIT_COMMIT_EMAIL = "isen97509@gmail.com"
    }

    if (Test-Path $PusherScript) {
        Log-Msg "[*] Launching Randomized Daily Multi-Commit Engine (Author: IshaanYK <$($env:GIT_COMMIT_EMAIL)>)..."
        # Random commit count between 5 and 20
        $randomCount = Get-Random -Minimum 5 -Maximum 21
        Log-Msg "[*] Selected random target commit batch: $randomCount commits"
        & python $PusherScript $randomCount *>> $LogFile
    }
    else {
        Log-Msg "[WARN] Pusher script not found at $PusherScript"
    }

    Log-Msg "=========================================================="
    Log-Msg "[OK] All streak tasks completed successfully!"
    Log-Msg "=========================================================="
    exit 0
}
catch {
    Log-Msg "[ERROR] Failed to execute auto streak: $_"
    exit 1
}

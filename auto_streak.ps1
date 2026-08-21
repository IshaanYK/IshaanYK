# Strict mode and error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# Determine script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$DataDir = Join-Path $ScriptDir "data"
$LogFile = Join-Path $DataDir "daily-streak-log.json"

Write-Output "=========================================================="
Write-Output "[*] IshaanYK GitHub Daily Streak & Code Automation"
Write-Output "=========================================================="

try {
    # Ensure data directory exists
    if (-not (Test-Path $DataDir)) {
        New-Item -ItemType Directory -Path $DataDir -Force | Out-Null
    }

    # Load or initialize daily streak log
    $streakData = $null
    if (Test-Path $LogFile) {
        try {
            $jsonContent = Get-Content -Path $LogFile -Raw -Encoding UTF8
            $streakData = $jsonContent | ConvertFrom-Json
        }
        catch {
            $streakData = $null
        }
    }

    if ($null -eq $streakData) {
        $streakData = [PSCustomObject]@{
            author = "Ishaan Sen"
            github_user = "IshaanYK"
            last_updated = ""
            total_active_days = 0
            streak_entries = @()
        }
    }

    # Generate new timestamped entry
    $nowUtc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $todayStr = (Get-Date).ToString("yyyy-MM-dd")

    $newEntry = [PSCustomObject]@{
        timestamp = $nowUtc
        date = $todayStr
        quest = "Autonomous Multi-Agent AI Development & System Scaling"
        buff = "Hyperfocus Aura Active"
        source = "Local Antigravity Daily Runner"
    }

    # Append entry
    $entriesList = @($streakData.streak_entries)
    $entriesList += $newEntry
    $streakData.streak_entries = $entriesList
    $streakData.last_updated = $nowUtc
    $streakData.total_active_days = $entriesList.Count

    # Save to JSON
    $streakData | ConvertTo-Json -Depth 10 | Out-File -FilePath $LogFile -Encoding UTF8
    Write-Output "[OK] Logged daily streak entry for $todayStr"

    # Git sync and pull latest remote changes first to prevent push rejections
    Set-Location -Path $ScriptDir
    Write-Output "[*] Pulling latest changes from origin main..."
    & git pull --rebase origin main

    # Run build scripts if python is available
    if (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Output "[*] Refreshing profile SVGs and contribution stats..."
        try {
            & python scripts/fetch_contributions.py
            & python scripts/render_heatmap_svg.py
            & python scripts/make_header_banner.py
            & python scripts/make_music_player.py
            & python scripts/make_info_card.py
            & python scripts/make_gaming_hud.py
            & python scripts/make_retro_snake.py
        }
        catch {
            Write-Output "[INFO] Asset regeneration skipped: $_"
        }
    }

    Write-Output "[*] Staging files..."
    & git config user.name "IshaanYK"
    & git config user.email "ishaansenres@gmail.com"
    & git add -A

    $status = & git status --porcelain
    if ($status -and ($status.Length -gt 0)) {
        Write-Output "[*] Committing daily streak update..."
        & git commit -m "feat(streak): local daily contribution update [$todayStr]"
        Write-Output "[*] Pushing to GitHub origin main..."
        & git push origin main
        Write-Output "[OK] Daily streak successfully pushed to GitHub!"
    }
    else {
        Write-Output "[INFO] No unstaged changes. Streak is already up-to-date today."
    }

    Write-Output "=========================================================="
    Write-Output "[OK] All tasks completed successfully!"
    Write-Output "=========================================================="
    exit 0
}
catch {
    Write-Warning "[ERROR] Failed to execute auto streak: $_"
    exit 1
}

"""
Randomized Multi-Commit Daily Streak & Activity Engine for IshaanYK.
Generates between 5 and 20 randomized, realistic commits per day with robust retry logic.
"""

import os
import sys
import json
import random
import datetime
import subprocess
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOG_FILE = os.path.join(DATA_DIR, "daily-streak-log.json")
ACTIVITY_LOG = os.path.join(DATA_DIR, "activity-log.json")

COMMIT_ACTIVITIES = [
    ("feat(agent)", "optimize multi-agent memory indexing and retrieval latency"),
    ("perf(core)", "accelerate token budget compression algorithm"),
    ("refactor(pipeline)", "streamline asynchronous tool invocation pipeline"),
    ("docs(readme)", "update autonomous agent benchmark metrics and system architecture"),
    ("fix(runtime)", "patch edge-case exception in parallel subagent dispatcher"),
    ("chore(deps)", "sync neural embedding dependencies and cache layers"),
    ("feat(engine)", "add adaptive context window compaction for long-running workflows"),
    ("perf(ui)", "optimize 60fps WebGL canvas draw calls and shader buffers"),
    ("refactor(storage)", "refine atomic daily streak state persistence"),
    ("test(eval)", "expand integration test suite for cross-agent communication"),
    ("feat(hud)", "tune real-time RPG status HUD stats and aura indicators"),
    ("perf(analytics)", "vectorize heatmap contribution matrix parsing"),
    ("feat(skills)", "register dynamic agent capabilities and custom tooling hooks"),
    ("chore(build)", "refresh automated asset pipelines and SVG build artifacts"),
    ("refactor(memory)", "enhance episodic memory pruning and retrieval weights"),
    ("feat(voice)", "tune low-latency audio stream buffer for conversational agent"),
    ("fix(telemetry)", "stabilize heartbeat monitoring and background task scheduling"),
    ("perf(db)", "index contribution records for sub-millisecond query execution"),
]

def run_cmd(cmd, check=True):
    res = subprocess.run(cmd, cwd=ROOT_DIR, shell=True, capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"[CMD FAILED] {cmd}\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
    return res

def sync_git():
    for attempt in range(5):
        run_cmd("git config user.name \"IshaanYK\"")
        run_cmd("git config user.email \"ishaansenres@gmail.com\"")
        res = run_cmd("git pull --rebase origin main", check=False)
        if res.returncode == 0:
            return True
        print(f"[*] Rebase attempt {attempt + 1} retry in 2s...")
        time.sleep(2)
    return False

def push_with_retry():
    for attempt in range(5):
        res = run_cmd("git push origin main", check=False)
        if res.returncode == 0:
            print("[OK] Push succeeded!")
            return True
        print(f"[!] Push failed on attempt {attempt + 1}. Pulling rebase and retrying...")
        sync_git()
        time.sleep(2)
    return False

def build_assets():
    try:
        from fetch_contributions import main as fetch_main
    except Exception:
        fetch_main = None

    try:
        if fetch_main:
            fetch_main()
    except Exception as e:
        print(f"[INFO] fetch_contributions skipped: {e}")

    scripts = [
        "render_heatmap_svg.py",
        "make_header_banner.py",
        "make_music_player.py",
        "make_info_card.py",
        "make_gaming_hud.py",
        "make_retro_snake.py"
    ]
    for s in scripts:
        path = os.path.join(SCRIPT_DIR, s)
        if os.path.exists(path):
            try:
                subprocess.run([sys.executable, path], cwd=SCRIPT_DIR, capture_output=True, text=True)
            except Exception as e:
                print(f"[INFO] {s} skipped: {e}")

def main():
    min_commits = 5
    max_commits = 20

    if len(sys.argv) > 1:
        try:
            val = int(sys.argv[1])
            min_commits = val
            max_commits = val
        except ValueError:
            pass

    commit_count = random.randint(min_commits, max_commits)
    print("==========================================================")
    print(f"[*] IshaanYK Multi-Commit Daily Engine")
    print(f"[*] Target Commits for this session: {commit_count} (Random range: {min_commits}-{max_commits})")
    print("==========================================================")

    os.makedirs(DATA_DIR, exist_ok=True)
    sync_git()

    # Load streak log
    streak_data = {"author": "Ishaan Sen", "github_user": "IshaanYK", "streak_entries": []}
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                streak_data = json.load(f)
        except Exception:
            pass

    # Load activity log
    activity_data = []
    if os.path.exists(ACTIVITY_LOG):
        try:
            with open(ACTIVITY_LOG, "r", encoding="utf-8") as f:
                activity_data = json.load(f)
        except Exception:
            pass

    today_str = datetime.date.today().isoformat()
    selected_activities = random.sample(COMMIT_ACTIVITIES * 3, commit_count)

    successful_commits = 0
    for idx, (scope, desc) in enumerate(selected_activities, 1):
        now_dt = datetime.datetime.utcnow() - datetime.timedelta(minutes=(commit_count - idx) * 7 + random.randint(1, 5))
        now_utc = now_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        activity_entry = {
            "id": f"act-{now_dt.strftime('%Y%m%d%H%M%S')}-{idx}",
            "timestamp": now_utc,
            "date": today_str,
            "scope": scope,
            "action": desc,
            "author": "IshaanYK"
        }
        activity_data.append(activity_entry)
        if len(activity_data) > 500:
            activity_data = activity_data[-500:]

        streak_entry = {
            "timestamp": now_utc,
            "date": today_str,
            "quest": desc,
            "scope": scope,
            "source": "IshaanYK Autonomous Engine"
        }
        streak_data["streak_entries"].append(streak_entry)
        streak_data["last_updated"] = now_utc
        streak_data["total_active_days"] = len({e.get("date") for e in streak_data["streak_entries"] if "date" in e})

        # Save files
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(streak_data, f, indent=2)
        with open(ACTIVITY_LOG, "w", encoding="utf-8") as f:
            json.dump(activity_data, f, indent=2)

        # On the last commit, refresh SVG assets
        if idx == commit_count:
            build_assets()

        run_cmd("git add -A")
        commit_msg = f"{scope}: {desc} [{today_str} #{idx}/{commit_count}]"
        
        # Git commit with explicit author date matching entry
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = now_utc
        env["GIT_COMMITTER_DATE"] = now_utc
        res = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=ROOT_DIR,
            env=env,
            capture_output=True,
            text=True
        )
        if res.returncode == 0:
            successful_commits += 1
            print(f"[{idx}/{commit_count}] [OK] {commit_msg}")
        else:
            print(f"[{idx}/{commit_count}] [SKIP] No diff or already up-to-date")

        # Small pause between local batch writes
        time.sleep(0.5)

    print(f"[*] Pushing {successful_commits} committed updates to origin main...")
    if push_with_retry():
        print(f"[OK] Successfully recorded and pushed {successful_commits} contributions!")
    else:
        print("[!] Push encountered an error. Changes are saved locally.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
One-command builder script: Regenerates all profile SVG widgets at once!
Run this whenever you edit any script in scripts/ or change your config.

Usage:
  python scripts/build_all.py
"""
import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))

scripts = [
    "make_header_banner.py",
    "make_arcade_banner.py",
    "make_music_player.py",
    "make_info_card.py",
    "make_gaming_hud.py",
    "make_retro_snake.py",
    "fetch_contributions.py",
    "render_heatmap_svg.py",
]

print("[*] Regenerating all GitHub Profile SVG widgets...\n")

for script in scripts:
    path = os.path.join(HERE, script)
    if os.path.exists(path):
        print(f"[*] Running {script}...")
        res = subprocess.run([sys.executable, path], cwd=HERE)
        if res.returncode != 0:
            print(f"[!] Warning: {script} exited with code {res.returncode}")

print("\n[OK] All profile widgets updated successfully!")

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "music-player.svg")

W, H = 860, 80
BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
INK = "#c9d1d9"
GREEN = "#3fb950"
CYAN = "#22d3ee"
ORANGE = "#ffa657"
PURPLE = "#a371f7"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="mpbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG2}"/>
      <stop offset="50%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>
    
    <linearGradient id="glowBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{CYAN}"/>
      <stop offset="50%" stop-color="{PURPLE}"/>
      <stop offset="100%" stop-color="{GREEN}"/>
    </linearGradient>

    <linearGradient id="barGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="{CYAN}"/>
      <stop offset="50%" stop-color="{GREEN}"/>
      <stop offset="100%" stop-color="{ORANGE}"/>
    </linearGradient>

    <style>
      @keyframes eqBar1 {{ 0%, 100% {{ height: 6px; y: 48px; }} 50% {{ height: 26px; y: 28px; }} }}
      @keyframes eqBar2 {{ 0%, 100% {{ height: 24px; y: 30px; }} 50% {{ height: 8px; y: 46px; }} }}
      @keyframes eqBar3 {{ 0%, 100% {{ height: 12px; y: 42px; }} 50% {{ height: 28px; y: 26px; }} }}
      @keyframes eqBar4 {{ 0%, 100% {{ height: 28px; y: 26px; }} 50% {{ height: 10px; y: 44px; }} }}
      @keyframes eqBar5 {{ 0%, 100% {{ height: 8px; y: 46px; }} 50% {{ height: 22px; y: 32px; }} }}

      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.4; filter: drop-shadow(0 0 2px {CYAN}); }}
        50% {{ opacity: 0.9; filter: drop-shadow(0 0 8px {CYAN}); }}
      }}

      @keyframes borderShift {{
        0% {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: 1000; }}
      }}

      .b1 {{ animation: eqBar1 1.2s ease-in-out infinite; }}
      .b2 {{ animation: eqBar2 0.9s ease-in-out infinite; }}
      .b3 {{ animation: eqBar3 1.4s ease-in-out infinite; }}
      .b4 {{ animation: eqBar4 1.1s ease-in-out infinite; }}
      .b5 {{ animation: eqBar5 1.3s ease-in-out infinite; }}
      .g-pulse {{ animation: pulseGlow 2.5s infinite; }}
    </style>
  </defs>
  
  <!-- Outer Card Frame -->
  <rect width="{W}" height="{H}" rx="10" fill="url(#mpbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" stroke="url(#glowBorder)" stroke-width="1.2" opacity="0.75"/>
  
  <!-- Left Side: Audio Visualizer Spectrum Bars -->
  <g transform="translate(20, 0)">
    <rect class="b1" x="0" y="44" width="4" height="10" rx="2" fill="url(#barGrad)"/>
    <rect class="b2" x="7" y="38" width="4" height="16" rx="2" fill="url(#barGrad)"/>
    <rect class="b3" x="14" y="42" width="4" height="12" rx="2" fill="url(#barGrad)"/>
    <rect class="b4" x="21" y="34" width="4" height="20" rx="2" fill="url(#barGrad)"/>
    <rect class="b5" x="28" y="46" width="4" height="8" rx="2" fill="url(#barGrad)"/>
    <rect class="b2" x="35" y="36" width="4" height="18" rx="2" fill="url(#barGrad)"/>
    <rect class="b4" x="42" y="40" width="4" height="14" rx="2" fill="url(#barGrad)"/>
  </g>

  <!-- Track Title & Shell Command -->
  <g transform="translate(80, 0)">
    <text x="0" y="35" fill="{MUTED}" font-size="12">
      ishaan@github:~$ <tspan fill="{CYAN}" font-weight="bold">play_audio.sh</tspan> --track <tspan fill="{ORANGE}">"Expresso.mp4"</tspan>
    </text>
    <text x="0" y="56" fill="{INK}" font-size="11" font-weight="600">
      🎵 Now Playing: <tspan fill="{GREEN}">Expresso Beats</tspan> <tspan fill="{MUTED}">[Hi-Fi Stereo / 320kbps]</tspan>
    </text>
  </g>

  <!-- Middle: Animated Progress Bar -->
  <g transform="translate(490, 34)">
    <rect x="0" y="0" width="180" height="10" rx="5" fill="#161b22" stroke="{FRAME}" stroke-width="1"/>
    <!-- Progress Fill -->
    <rect x="1" y="1" width="0" height="8" rx="4" fill="url(#barGrad)">
      <animate attributeName="width" from="0" to="178" dur="12s" repeatCount="indefinite" />
    </rect>
    <!-- Glowing Knob -->
    <circle cx="1" cy="5" r="5" fill="#ffffff" class="g-pulse">
      <animate attributeName="cx" from="1" to="178" dur="12s" repeatCount="indefinite" />
    </circle>
    <!-- Time indicator -->
    <text x="192" y="9" fill="{GREEN}" font-size="11" font-weight="bold">● LIVE</text>
  </g>
  
  <!-- Right Side: Interactive Button -->
  <g transform="translate(745, 40)">
    <circle cx="0" cy="0" r="14" fill="{GREEN}" opacity="0.2" class="g-pulse"/>
    <circle cx="0" cy="0" r="11" fill="{GREEN}"/>
    <!-- Play arrow -->
    <polygon points="-3,-5 6,0 -3,5" fill="#0d1117"/>
    <text x="18" y="4" fill="{INK}" font-size="12" font-weight="bold">Listen Now 🎧</text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

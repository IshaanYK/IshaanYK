import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "header-banner.svg")

W, H = 860, 140
BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
INK = "#e6edf3"
GREEN = "#3fb950"
CYAN = "#00f2fe"
BLUE = "#4facfe"
PURPLE = "#a371f7"
PINK = "#ff007f"
GOLD = "#f2cc60"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="hbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="#121824"/>
    </linearGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{CYAN}"/>
      <stop offset="50%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{PURPLE}"/>
    </linearGradient>

    <linearGradient id="borderGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{CYAN}">
        <animate attributeName="stop-color" values="{CYAN};{PINK};{PURPLE};{CYAN}" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="{PURPLE}">
        <animate attributeName="stop-color" values="{PURPLE};{BLUE};{GREEN};{PURPLE}" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{GREEN}">
        <animate attributeName="stop-color" values="{GREEN};{CYAN};{PINK};{GREEN}" dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Cyber Grid Pattern -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1f293d" stroke-width="0.5" opacity="0.4"/>
    </pattern>

    <style>
      @keyframes typeLine1 {{
        0%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 97% {{ opacity: 0; transform: translateY(-10px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes typeLine2 {{
        0%, 23% {{ opacity: 0; transform: translateY(10px); }}
        27%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-10px); }}
      }}
      @keyframes typeLine3 {{
        0%, 48% {{ opacity: 0; transform: translateY(10px); }}
        52%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-10px); }}
      }}
      @keyframes typeLine4 {{
        0%, 73% {{ opacity: 0; transform: translateY(10px); }}
        77%, 96% {{ opacity: 1; transform: translateY(0); }}
        98%, 100% {{ opacity: 0; transform: translateY(10px); }}
      }}

      @keyframes pulseGlow {{
        0%, 100% {{ filter: drop-shadow(0 0 4px {CYAN}); opacity: 0.9; }}
        50% {{ filter: drop-shadow(0 0 12px {PURPLE}); opacity: 1; }}
      }}

      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      .l1 {{ animation: typeLine1 14s infinite; }}
      .l2 {{ animation: typeLine2 14s infinite; }}
      .l3 {{ animation: typeLine3 14s infinite; }}
      .l4 {{ animation: typeLine4 14s infinite; }}
      .cursor {{ animation: cursorBlink 0.8s infinite; fill: {CYAN}; }}
      .glow-title {{ animation: pulseGlow 4s infinite; }}
    </style>
  </defs>

  <!-- Card Frame -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#hbg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#borderGlow)" stroke-width="1.8"/>

  <!-- macOS Top Bar -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="40" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="56" cy="22" r="5" fill="#27c93f"/>

  <!-- Status pill on top right -->
  <g transform="translate(620, 14)">
    <rect width="216" height="22" rx="11" fill="#161b22" stroke="{FRAME}" stroke-width="1"/>
    <circle cx="14" cy="11" r="4" fill="{GREEN}">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="26" y="15" fill="{INK}" font-size="10.5" font-weight="600">Open for AI / FullStack Collabs</text>
  </g>

  <!-- Greeting Title -->
  <g transform="translate(24, 66)">
    <text font-size="28" font-weight="800" fill="url(#textGrad)" class="glow-title" letter-spacing="-0.5px">
      ⚡ Hi, I'm Ishaan Sen 👋
    </text>
    <text x="420" y="-2" fill="{GOLD}" font-size="13" font-weight="700">🎓 IIT Madras</text>
  </g>

  <!-- Dynamic Typing Subtitle Lines -->
  <g transform="translate(24, 104)">
    <text class="l1" font-size="14" fill="{INK}" font-weight="600">
      🚀 <tspan fill="{CYAN}">AI Engineer &amp; Full-Stack Developer</tspan> — Crafting Intelligent Systems <tspan class="cursor">█</tspan>
    </text>
    <text class="l2" font-size="14" fill="{INK}" font-weight="600">
      🤖 <tspan fill="{PURPLE}">Building Autonomous Agents &amp; RAG Architectures</tspan> <tspan class="cursor">█</tspan>
    </text>
    <text class="l3" font-size="14" fill="{INK}" font-weight="600">
      ⚡ <tspan fill="{GREEN}">Designing High-Performance React &amp; Next.js Web Apps</tspan> <tspan class="cursor">█</tspan>
    </text>
    <text class="l4" font-size="14" fill="{INK}" font-weight="600">
      💡 <tspan fill="{PINK}">Open Source Contributor &amp; Tech Enthusiast</tspan> <tspan class="cursor">█</tspan>
    </text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

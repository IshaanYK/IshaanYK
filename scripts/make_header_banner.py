import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "header-banner.svg")

W, H = 860, 120
BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
INK = "#e6edf3"
GREEN = "#3fb950"
CYAN = "#22d3ee"
BLUE = "#58a6ff"
PURPLE = "#bc8cff"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="hbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG2}"/>
      <stop offset="50%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="50%" stop-color="{CYAN}"/>
      <stop offset="100%" stop-color="{GREEN}"/>
    </linearGradient>

    <linearGradient id="bannerGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="{CYAN}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{PURPLE}" stop-opacity="0.8"/>
    </linearGradient>

    <style>
      @keyframes typing {{
        0% {{ width: 0; }}
        50% {{ width: 100%; }}
        100% {{ width: 100%; }}
      }}

      @keyframes cursor {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(0.85); }}
      }}

      .title-text {{
        font-size: 26px;
        font-weight: 800;
        fill: url(#textGrad);
        letter-spacing: -0.5px;
      }}

      .subtitle {{
        font-size: 14px;
        fill: {MUTED};
        font-weight: 500;
      }}

      .highlight {{
        fill: {CYAN};
        font-weight: 700;
      }}

      .cursor-blink {{
        animation: cursor 0.9s infinite;
        fill: {CYAN};
      }}
    </style>
  </defs>

  <!-- Background Box -->
  <rect width="{W}" height="{H}" rx="12" fill="url(#hbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="url(#bannerGlow)" stroke-width="1.2" opacity="0.6"/>

  <!-- Top macOS Window Dots -->
  <circle cx="24" cy="20" r="5" fill="#ff5f56"/>
  <circle cx="40" cy="20" r="5" fill="#ffbd2e"/>
  <circle cx="56" cy="20" r="5" fill="#27c93f"/>

  <text x="{W - 24}" y="24" fill="{MUTED}" font-size="11" text-anchor="end">ishaan@github: ~</text>

  <!-- Main Animated Greeting -->
  <g transform="translate(24, 62)">
    <text class="title-text">⚡ Hi, I'm Ishaan Sen 👋</text>
  </g>

  <!-- Subtitle Line -->
  <g transform="translate(24, 94)">
    <text class="subtitle">
      AI Engineer &amp; Full-Stack Developer <tspan fill="{BLUE}">|</tspan> <tspan class="highlight">Agentic Systems &amp; Scalable Web Apps</tspan> <tspan class="cursor-blink">█</tspan>
    </text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

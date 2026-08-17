import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "header-banner.svg")

W, H = 860, 144

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">
  <defs>
    <linearGradient id="hbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#04060a"/>
    </linearGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="40%" stop-color="#5e6ad2"/>
      <stop offset="80%" stop-color="#a371f7"/>
      <stop offset="100%" stop-color="#38ef7d"/>
    </linearGradient>

    <linearGradient id="borderGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#5e6ad2">
        <animate attributeName="stop-color" values="#5e6ad2;#00f2fe;#38ef7d;#a371f7;#5e6ad2" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe;#a371f7;#5e6ad2;#38ef7d;#00f2fe" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#38ef7d">
        <animate attributeName="stop-color" values="#38ef7d;#5e6ad2;#00f2fe;#a371f7;#38ef7d" dur="7s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1f293d" stroke-width="0.5" opacity="0.3"/>
    </pattern>

    <style>
      @keyframes typeLine1 {{
        0%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 97% {{ opacity: 0; transform: translateY(-8px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes typeLine2 {{
        0%, 23% {{ opacity: 0; transform: translateY(8px); }}
        27%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes typeLine3 {{
        0%, 48% {{ opacity: 0; transform: translateY(8px); }}
        52%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes typeLine4 {{
        0%, 73% {{ opacity: 0; transform: translateY(8px); }}
        77%, 96% {{ opacity: 1; transform: translateY(0); }}
        98%, 100% {{ opacity: 0; transform: translateY(8px); }}
      }}

      @keyframes pulseGlow {{
        0%, 100% {{ filter: drop-shadow(0 0 4px #00f2fe); opacity: 0.95; }}
        50% {{ filter: drop-shadow(0 0 14px #5e6ad2); opacity: 1; }}
      }}

      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      .l1 {{ animation: typeLine1 14s infinite; }}
      .l2 {{ animation: typeLine2 14s infinite; }}
      .l3 {{ animation: typeLine3 14s infinite; }}
      .l4 {{ animation: typeLine4 14s infinite; }}
      .cursor {{ animation: cursorBlink 0.8s infinite; fill: #00f2fe; }}
      .glow-title {{ animation: pulseGlow 4s infinite; }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" rx="14" fill="url(#hbg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#borderGlow)" stroke-width="1.8"/>

  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="40" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="56" cy="22" r="5" fill="#27c93f"/>

  <g transform="translate(615, 12)">
    <rect width="220" height="22" rx="11" fill="#141824" stroke="#30363d" stroke-width="1"/>
    <circle cx="14" cy="11" r="4" fill="#3fb950">
      <animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="26" y="15" fill="#e6edf3" font-size="10.5" font-weight="600">Open for AI &amp; Full-Stack Collabs</text>
  </g>

  <g transform="translate(24, 68)">
    <text font-size="28" font-weight="800" fill="url(#textGrad)" class="glow-title" letter-spacing="-0.5px">
      ⚡ Hi, I'm Ishaan Sen 👋
    </text>
    <rect x="365" y="-18" width="130" height="22" rx="6" fill="#1c2333" stroke="#f2cc60" stroke-width="0.8" opacity="0.9"/>
    <text x="375" y="-3" fill="#f2cc60" font-size="11.5" font-weight="700">🎓 IIT Madras</text>
  </g>

  <g transform="translate(24, 108)">
    <text class="l1" font-size="14" fill="#e6edf3" font-weight="600">
      🚀 <tspan fill="#00f2fe">AI Engineer &amp; Full-Stack Developer</tspan> — Crafting Intelligent Systems <tspan class="cursor">█</tspan>
    </text>
    <text class="l2" font-size="14" fill="#e6edf3" font-weight="600">
      🤖 <tspan fill="#a371f7">Autonomous Multi-Agent Systems &amp; Production RAG Pipelines</tspan> <tspan class="cursor">█</tspan>
    </text>
    <text class="l3" font-size="14" fill="#e6edf3" font-weight="600">
      ⚡ <tspan fill="#38ef7d">High-Performance Next.js, React &amp; Cloud Scalability</tspan> <tspan class="cursor">█</tspan>
    </text>
    <text class="l4" font-size="14" fill="#e6edf3" font-weight="600">
      💡 <tspan fill="#ffa657">Building Next-Gen Developer Tools &amp; Open Source Innovation</tspan> <tspan class="cursor">█</tspan>
    </text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "retro-snake.svg")

W, H = 860, 124

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="snakeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08090e"/>
      <stop offset="50%" stop-color="#0c0e16"/>
      <stop offset="100%" stop-color="#050609"/>
    </linearGradient>

    <linearGradient id="snakeBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#27a644" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#5e6ad2" stop-opacity="0.8"/>
    </linearGradient>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; }}
      .font-mono {{ font-family: 'SF Mono', 'JetBrains Mono', 'Fira Code', Menlo, monospace; }}

      @keyframes snakeCrawl {{
        0% {{ transform: translateX(0px); }}
        50% {{ transform: translateX(520px); }}
        100% {{ transform: translateX(0px); }}
      }}
      @keyframes itemPulse {{
        0%, 100% {{ transform: scale(1); opacity: 0.9; }}
        50% {{ transform: scale(1.25); opacity: 1; filter: drop-shadow(0 0 6px #00f2fe); }}
      }}
      @keyframes floatGhost {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-3px); }}
      }}

      .snake-runner {{ animation: snakeCrawl 18s ease-in-out infinite; }}
      .pulse-item {{ animation: itemPulse 1.6s infinite; transform-origin: center; }}
      .ghost-float {{ animation: floatGhost 2.2s ease-in-out infinite; }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" rx="14" fill="url(#snakeBg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#snakeBorder)" stroke-width="1.2"/>

  <!-- Arcade Top Header -->
  <g transform="translate(24, 26)">
    <text x="0" y="0" fill="#27a644" class="font-mono" font-size="12" font-weight="700" letter-spacing="1px">🕹️ RETRO ARCADE: CONTRIBUTION HUNTER</text>
    <text x="370" y="0" fill="#f2cc60" class="font-mono" font-size="11" font-weight="600">🪙 COINS: 99</text>
    <text x="485" y="0" fill="#00f2fe" class="font-mono" font-size="11" font-weight="600">SCORE: 185,420</text>
    <text x="635" y="0" fill="#828fff" class="font-mono" font-size="11" font-weight="600">STREAK: x64 FIRE 🔥</text>
    <text x="770" y="0" fill="#f7f8f8" class="font-mono" font-size="11" font-weight="700">STAGE 09</text>
  </g>

  <!-- Arcade Matrix Grid -->
  <g transform="translate(24, 44)" opacity="0.3">
    <line x1="0" y1="0" x2="812" y2="0" stroke="#23252a" stroke-width="1"/>
    <line x1="0" y1="56" x2="812" y2="56" stroke="#23252a" stroke-width="1"/>
    <rect x="30" y="22" width="10" height="10" rx="2" fill="#141724"/>
    <rect x="70" y="22" width="10" height="10" rx="2" fill="#0e4429"/>
    <rect x="120" y="22" width="10" height="10" rx="2" fill="#006d32"/>
    <rect x="180" y="22" width="10" height="10" rx="2" fill="#26a641"/>
    <rect x="250" y="22" width="10" height="10" rx="2" fill="#39d353"/>
    <rect x="340" y="22" width="10" height="10" rx="2" fill="#141724"/>
    <rect x="440" y="22" width="10" height="10" rx="2" fill="#006d32"/>
    <rect x="540" y="22" width="10" height="10" rx="2" fill="#39d353"/>
    <rect x="650" y="22" width="10" height="10" rx="2" fill="#26a641"/>
    <rect x="740" y="22" width="10" height="10" rx="2" fill="#39d353"/>
  </g>

  <!-- Glowing Food Items -->
  <g transform="translate(190, 68)" class="pulse-item">
    <circle cx="0" cy="0" r="6" fill="#00f2fe"/>
    <circle cx="0" cy="0" r="2.5" fill="#ffffff"/>
  </g>
  <g transform="translate(460, 68)" class="pulse-item">
    <polygon points="0,-6 5,4 -5,4" fill="#f2cc60"/>
  </g>
  <g transform="translate(700, 68)" class="pulse-item">
    <circle cx="0" cy="0" r="5.5" fill="#27a644"/>
  </g>

  <!-- Snake Crawl Unit -->
  <g class="snake-runner" transform="translate(40, 68)">
    <rect x="0" y="-6" width="13" height="13" rx="3" fill="#00f2fe" stroke="#06070a" stroke-width="1.2"/>
    <circle cx="8" cy="-2" r="1.8" fill="#06070a"/>
    <rect x="-15" y="-6" width="13" height="13" rx="3" fill="#5e6ad2" stroke="#06070a" stroke-width="1.2"/>
    <rect x="-30" y="-6" width="13" height="13" rx="3" fill="#828fff" stroke="#06070a" stroke-width="1.2"/>
    <rect x="-45" y="-6" width="13" height="13" rx="3" fill="#27a644" stroke="#06070a" stroke-width="1.2"/>
    <rect x="-60" y="-6" width="13" height="13" rx="3" fill="#39d353" stroke="#06070a" stroke-width="1.2"/>
    <rect x="-75" y="-6" width="13" height="13" rx="3" fill="#0e4429" stroke="#06070a" stroke-width="1.2"/>
  </g>

  <!-- Retro Cyber Ghost -->
  <g class="ghost-float" transform="translate(768, 68)">
    <path d="M -7 -7 C -7 -13 7 -13 7 -7 L 7 5 L 3.5 2 L 0 5 L -3.5 2 L -7 5 Z" fill="#828fff"/>
    <circle cx="-2.5" cy="-5" r="1.8" fill="#ffffff"/>
    <circle cx="2.5" cy="-5" r="1.8" fill="#ffffff"/>
    <circle cx="-1.8" cy="-5" r="0.9" fill="#06070a"/>
    <circle cx="3.2" cy="-5" r="0.9" fill="#06070a"/>
  </g>

  <text x="430" y="112" fill="#8a8f98" class="font-sans" font-size="11" text-anchor="middle">
    👾 <tspan fill="#27a644" font-weight="600">Daily Quest:</tspan> Auto-sync commits to keep the green matrix alive &amp; energize the agent engine! 🚀
  </text>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

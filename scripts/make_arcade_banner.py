import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "arcade-game-banner.svg")

W, H = 860, 84

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Frosted Glass Gradient -->
    <linearGradient id="gameGlassBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#191a1e"/>
      <stop offset="6%" stop-color="#111215"/>
      <stop offset="100%" stop-color="#08080a"/>
    </linearGradient>

    <!-- Top Specular Sheen -->
    <linearGradient id="gameSheen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.12"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- Titanium Border -->
    <linearGradient id="gameBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.04"/>
    </linearGradient>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif; }}
      .font-mono {{ font-family: "SF Mono", Menlo, Consolas, monospace; }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" rx="14" fill="url(#gameGlassBg)"/>
  <rect width="{W}" height="{H/2}" rx="14" fill="url(#gameSheen)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#gameBorder)" stroke-width="1"/>

  <!-- Ship Icon -->
  <g transform="translate(36, 42)">
    <circle cx="0" cy="0" r="18" fill="#ffffff" fill-opacity="0.06"/>
    <polygon points="0,-12 10,8 4,5 0,8 -4,5 -10,8" fill="#2997ff"/>
  </g>

  <!-- Title & Subtitle -->
  <g transform="translate(74, 32)">
    <text x="0" y="0" fill="#f5f5f7" class="font-sans" font-size="13.5" font-weight="600" letter-spacing="-0.2px">Neural Defender • Playable 60fps HTML5 Arcade Game</text>
    <text x="0" y="20" fill="#86868b" class="font-sans" font-size="11.5">
      Cyberpunk browser arcade shooter built with custom canvas physics &amp; Web Audio SFX
    </text>
  </g>

  <!-- Play Button -->
  <g transform="translate(710, 42)">
    <rect x="-6" y="-16" width="138" height="32" rx="16" fill="#2997ff" fill-opacity="0.12" stroke="#2997ff" stroke-opacity="0.3" stroke-width="0.8"/>
    <polygon points="8,-4 15,0 8,4" fill="#2997ff"/>
    <text x="24" y="4" fill="#2997ff" class="font-sans" font-size="11.5" font-weight="600">Launch Game 🚀</text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "music-player.svg")

W, H = 860, 68

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Frosted Glass Gradient -->
    <linearGradient id="audioBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#191a1e"/>
      <stop offset="6%" stop-color="#111215"/>
      <stop offset="100%" stop-color="#08080a"/>
    </linearGradient>

    <!-- Top Specular Sheen -->
    <linearGradient id="audioSpecular" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.12"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- Titanium Glass Border -->
    <linearGradient id="audioBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.04"/>
    </linearGradient>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif; }}
      .font-mono {{ font-family: "SF Mono", Menlo, Consolas, monospace; }}

      @keyframes wave1 {{ 0%, 100% {{ height: 5px; y: 39px; }} 50% {{ height: 22px; y: 22px; }} }}
      @keyframes wave2 {{ 0%, 100% {{ height: 18px; y: 26px; }} 50% {{ height: 7px; y: 37px; }} }}
      @keyframes wave3 {{ 0%, 100% {{ height: 10px; y: 34px; }} 50% {{ height: 24px; y: 20px; }} }}
      @keyframes wave4 {{ 0%, 100% {{ height: 22px; y: 22px; }} 50% {{ height: 6px; y: 38px; }} }}

      .w1 {{ animation: wave1 1.2s ease-in-out infinite; fill: #2997ff; }}
      .w2 {{ animation: wave2 0.9s ease-in-out infinite; fill: #ffffff; fill-opacity: 0.85; }}
      .w3 {{ animation: wave3 1.4s ease-in-out infinite; fill: #2997ff; }}
      .w4 {{ animation: wave4 1.1s ease-in-out infinite; fill: #ffffff; fill-opacity: 0.85; }}
    </style>
  </defs>
  
  <rect width="{W}" height="{H}" rx="12" fill="url(#audioBg)"/>
  <rect width="{W}" height="{H/2}" rx="12" fill="url(#audioSpecular)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="url(#audioBorder)" stroke-width="1"/>
  
  <!-- Waveform Indicator -->
  <g transform="translate(20, 0)">
    <rect class="w1" x="0" y="34" width="3.5" height="10" rx="1.75"/>
    <rect class="w2" x="6" y="26" width="3.5" height="18" rx="1.75"/>
    <rect class="w3" x="12" y="30" width="3.5" height="14" rx="1.75"/>
    <rect class="w4" x="18" y="22" width="3.5" height="22" rx="1.75"/>
    <rect class="w1" x="24" y="36" width="3.5" height="8" rx="1.75"/>
    <rect class="w2" x="30" y="28" width="3.5" height="16" rx="1.75"/>
  </g>

  <!-- Track Title -->
  <g transform="translate(70, 0)">
    <text x="0" y="30" fill="#86868b" class="font-mono" font-size="11">
      Now Playing: <tspan fill="#f5f5f7" font-weight="600">Expresso Ambient Beats</tspan>
    </text>
    <text x="0" y="48" fill="#a1a1a6" class="font-sans" font-size="11.5">
      Focus Audio Stream • Hi-Fi Stereo
    </text>
  </g>

  <!-- Progress Bar -->
  <g transform="translate(480, 28)">
    <rect x="0" y="5" width="200" height="4" rx="2" fill="#ffffff" fill-opacity="0.1"/>
    <rect x="0" y="5" width="0" height="4" rx="2" fill="#2997ff">
      <animate attributeName="width" from="0" to="200" dur="18s" repeatCount="indefinite" />
    </rect>
    <text x="212" y="9.5" fill="#86868b" class="font-mono" font-size="10">LIVE</text>
  </g>
  
  <!-- Apple-Style Play Pill -->
  <g transform="translate(745, 34)">
    <rect x="-6" y="-15" width="105" height="30" rx="15" fill="#ffffff" fill-opacity="0.08" stroke="#ffffff" stroke-opacity="0.15" stroke-width="0.8"/>
    <polygon points="10,-4 17,0 10,4" fill="#f5f5f7"/>
    <text x="26" y="3.5" fill="#f5f5f7" class="font-sans" font-size="11" font-weight="500">Play Audio</text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "music-player.svg")

W, H = 860, 84

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">
  <defs>
    <linearGradient id="mpbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#141824"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#070a10"/>
    </linearGradient>
    
    <linearGradient id="glowBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#5e6ad2"/>
      <stop offset="50%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#38ef7d"/>
    </linearGradient>

    <linearGradient id="barGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#5e6ad2"/>
      <stop offset="40%" stop-color="#00f2fe"/>
      <stop offset="80%" stop-color="#38ef7d"/>
      <stop offset="100%" stop-color="#f2cc60"/>
    </linearGradient>

    <style>
      @keyframes eqBar1 {{ 0%, 100% {{ height: 6px; y: 50px; }} 50% {{ height: 26px; y: 30px; }} }}
      @keyframes eqBar2 {{ 0%, 100% {{ height: 24px; y: 32px; }} 50% {{ height: 8px; y: 48px; }} }}
      @keyframes eqBar3 {{ 0%, 100% {{ height: 12px; y: 44px; }} 50% {{ height: 28px; y: 28px; }} }}
      @keyframes eqBar4 {{ 0%, 100% {{ height: 28px; y: 28px; }} 50% {{ height: 10px; y: 46px; }} }}
      @keyframes eqBar5 {{ 0%, 100% {{ height: 8px; y: 48px; }} 50% {{ height: 22px; y: 34px; }} }}

      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.5; filter: drop-shadow(0 0 3px #00f2fe); }}
        50% {{ opacity: 0.95; filter: drop-shadow(0 0 9px #5e6ad2); }}
      }}

      .b1 {{ animation: eqBar1 1.2s ease-in-out infinite; }}
      .b2 {{ animation: eqBar2 0.9s ease-in-out infinite; }}
      .b3 {{ animation: eqBar3 1.4s ease-in-out infinite; }}
      .b4 {{ animation: eqBar4 1.1s ease-in-out infinite; }}
      .b5 {{ animation: eqBar5 1.3s ease-in-out infinite; }}
      .g-pulse {{ animation: pulseGlow 2.5s infinite; }}
    </style>
  </defs>
  
  <rect width="{W}" height="{H}" rx="12" fill="url(#mpbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="url(#glowBorder)" stroke-width="1.3" opacity="0.8"/>
  
  <g transform="translate(20, 0)">
    <rect class="b1" x="0" y="44" width="4" height="12" rx="2" fill="url(#barGrad)"/>
    <rect class="b2" x="7" y="36" width="4" height="20" rx="2" fill="url(#barGrad)"/>
    <rect class="b3" x="14" y="40" width="4" height="16" rx="2" fill="url(#barGrad)"/>
    <rect class="b4" x="21" y="32" width="4" height="24" rx="2" fill="url(#barGrad)"/>
    <rect class="b5" x="28" y="46" width="4" height="10" rx="2" fill="url(#barGrad)"/>
    <rect class="b2" x="35" y="34" width="4" height="22" rx="2" fill="url(#barGrad)"/>
    <rect class="b4" x="42" y="38" width="4" height="18" rx="2" fill="url(#barGrad)"/>
    <rect class="b1" x="49" y="42" width="4" height="14" rx="2" fill="url(#barGrad)"/>
  </g>

  <g transform="translate(86, 0)">
    <text x="0" y="35" fill="#8b949e" font-size="12">
      ishaan@system:~$ <tspan fill="#00f2fe" font-weight="bold">play_audio.sh</tspan> --track <tspan fill="#ffa657">"Expresso.mp4"</tspan>
    </text>
    <text x="0" y="58" fill="#e6edf3" font-size="11.5" font-weight="600">
      🎧 Now Streaming: <tspan fill="#3fb950" font-weight="700">Expresso Ambient Beats</tspan> <tspan fill="#8b949e">[Hi-Fi Stereo / Focus Mode]</tspan>
    </text>
  </g>

  <g transform="translate(485, 36)">
    <rect x="0" y="0" width="180" height="10" rx="5" fill="#141824" stroke="#30363d" stroke-width="1"/>
    <rect x="1" y="1" width="0" height="8" rx="4" fill="url(#barGrad)">
      <animate attributeName="width" from="0" to="178" dur="14s" repeatCount="indefinite" />
    </rect>
    <circle cx="1" cy="5" r="5" fill="#ffffff" class="g-pulse">
      <animate attributeName="cx" from="1" to="178" dur="14s" repeatCount="indefinite" />
    </circle>
    <text x="192" y="9" fill="#3fb950" font-size="11" font-weight="bold">● PLAYING</text>
  </g>
  
  <g transform="translate(740, 42)">
    <rect x="-8" y="-16" width="108" height="32" rx="16" fill="#1f293d" stroke="#3fb950" stroke-width="1" opacity="0.85"/>
    <circle cx="8" cy="0" r="9" fill="#3fb950"/>
    <polygon points="6,-4 13,0 6,4" fill="#0d1117"/>
    <text x="24" y="4" fill="#e6edf3" font-size="11.5" font-weight="bold">Play Track 🎵</text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "header-banner.svg")

W, H = 860, 128

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Obsidian Glossy Glass Gradient -->
    <linearGradient id="glossyBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1c1d22"/>
      <stop offset="4%" stop-color="#121316"/>
      <stop offset="100%" stop-color="#08080a"/>
    </linearGradient>

    <!-- Apple Specular Top-Light Glass Reflection -->
    <linearGradient id="glassReflection" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
      <stop offset="35%" stop-color="#ffffff" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- Hairline Titanium Border -->
    <linearGradient id="titaniumBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.03"/>
    </linearGradient>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Helvetica, Arial, sans-serif; }}
      .font-mono {{ font-family: "SF Mono", Menlo, Consolas, Monaco, monospace; }}

      @keyframes cursorBlink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
      @keyframes pulseDot {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.4; transform: scale(0.9); }} }}

      @keyframes slideCycle1 {{
        0%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 97% {{ opacity: 0; transform: translateY(-4px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes slideCycle2 {{
        0%, 23% {{ opacity: 0; transform: translateY(4px); }}
        27%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes slideCycle3 {{
        0%, 48% {{ opacity: 0; transform: translateY(4px); }}
        52%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes slideCycle4 {{
        0%, 73% {{ opacity: 0; transform: translateY(4px); }}
        77%, 96% {{ opacity: 1; transform: translateY(0); }}
        98%, 100% {{ opacity: 0; transform: translateY(4px); }}
      }}

      .c-blink {{ animation: cursorBlink 0.9s infinite; fill: #2997ff; }}
      .dot-live {{ animation: pulseDot 2s infinite ease-in-out; transform-origin: center; }}
      .t1 {{ animation: slideCycle1 16s infinite; }}
      .t2 {{ animation: slideCycle2 16s infinite; }}
      .t3 {{ animation: slideCycle3 16s infinite; }}
      .t4 {{ animation: slideCycle4 16s infinite; }}
    </style>
  </defs>

  <!-- Glass Card Body -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#glossyBg)"/>
  <!-- Top Half Specular Sheen -->
  <rect width="{W}" height="{H/2}" rx="14" fill="url(#glassReflection)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#titaniumBorder)" stroke-width="1"/>

  <!-- Window Dots -->
  <g transform="translate(22, 18)">
    <circle cx="0" cy="0" r="4.5" fill="#ffffff" fill-opacity="0.2"/>
    <circle cx="14" cy="0" r="4.5" fill="#ffffff" fill-opacity="0.2"/>
    <circle cx="28" cy="0" r="4.5" fill="#ffffff" fill-opacity="0.2"/>
  </g>

  <!-- Status Pill -->
  <g transform="translate(635, 12)">
    <rect width="200" height="24" rx="12" fill="#ffffff" fill-opacity="0.05" stroke="#ffffff" stroke-opacity="0.1" stroke-width="0.8"/>
    <circle cx="14" cy="12" r="3.5" fill="#30d158" class="dot-live"/>
    <text x="24" y="15.5" fill="#a1a1a6" class="font-sans" font-size="11" font-weight="500">Available for Opportunities</text>
  </g>

  <!-- Main Identity Header -->
  <g transform="translate(24, 62)">
    <text class="font-sans" font-size="28" font-weight="600" fill="#f5f5f7" letter-spacing="-0.5px">
      Ishaan Sen
    </text>
    
    <!-- IIT Madras Badge -->
    <g transform="translate(170, -20)">
      <rect width="125" height="22" rx="11" fill="#ffffff" fill-opacity="0.06" stroke="#ffffff" stroke-opacity="0.12" stroke-width="0.8"/>
      <text x="12" y="15" fill="#e5e5e7" class="font-sans" font-size="11" font-weight="500">🎓 IIT Madras</text>
    </g>

    <!-- AI Systems Badge -->
    <g transform="translate(302, -20)">
      <rect width="150" height="22" rx="11" fill="#2997ff" fill-opacity="0.12" stroke="#2997ff" stroke-opacity="0.3" stroke-width="0.8"/>
      <text x="12" y="15" fill="#2997ff" class="font-sans" font-size="11" font-weight="500">⚡ AI Systems Engineer</text>
    </g>
  </g>

  <!-- Clean Subtitle Loop -->
  <g transform="translate(24, 100)" class="font-mono">
    <g class="t1">
      <text font-size="12.5" fill="#a1a1a6">
        <tspan fill="#f5f5f7">&gt;</tspan> Architecting autonomous multi-agent pipelines &amp; real-time voice intelligence <tspan class="c-blink">█</tspan>
      </text>
    </g>
    <g class="t2">
      <text font-size="12.5" fill="#a1a1a6">
        <tspan fill="#f5f5f7">&gt;</tspan> Crafting ultra-responsive 60fps web apps, Next.js systems &amp; modern interfaces <tspan class="c-blink">█</tspan>
      </text>
    </g>
    <g class="t3">
      <text font-size="12.5" fill="#a1a1a6">
        <tspan fill="#f5f5f7">&gt;</tspan> Engineering production RAG architectures, embeddings &amp; low-latency tools <tspan class="c-blink">█</tspan>
      </text>
    </g>
    <g class="t4">
      <text font-size="12.5" fill="#a1a1a6">
        <tspan fill="#f5f5f7">&gt;</tspan> Building next-gen open-source software, agentic workflows &amp; developer tools <tspan class="c-blink">█</tspan>
      </text>
    </g>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

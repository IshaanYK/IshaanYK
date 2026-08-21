import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "interactive-bento.svg")

W, H = 860, 190

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bentoBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141519"/>
      <stop offset="6%" stop-color="#0e0f13"/>
      <stop offset="100%" stop-color="#060608"/>
    </linearGradient>

    <linearGradient id="bentoSheen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="bentoBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#2997ff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.04"/>
    </linearGradient>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", sans-serif; }}
      .font-mono {{ font-family: "SF Mono", Menlo, Consolas, monospace; }}

      @keyframes waveLoop {{
        0% {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: -120; }}
      }}
      @keyframes pulseChip {{
        0%, 100% {{ filter: drop-shadow(0 0 2px rgba(41,151,255,0.4)); opacity: 0.9; }}
        50% {{ filter: drop-shadow(0 0 10px rgba(41,151,255,0.9)); opacity: 1; }}
      }}

      .flow-line {{ stroke-dasharray: 6, 6; animation: waveLoop 3s linear infinite; }}
      .chip-glow {{ animation: pulseChip 2.5s infinite ease-in-out; }}
    </style>
  </defs>

  <!-- Container -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#bentoBg)"/>
  <rect width="{W}" height="{H/2}" rx="14" fill="url(#bentoSheen)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#bentoBorder)" stroke-width="1"/>

  <!-- Top Title -->
  <g transform="translate(24, 24)">
    <text x="0" y="0" fill="#f5f5f7" class="font-sans" font-size="13" font-weight="600" letter-spacing="-0.2px">⚡ NEURAL ARCHITECTURE &amp; FULL-STACK ECOSYSTEM</text>
    <text x="590" y="0" fill="#86868b" class="font-mono" font-size="11">Core Runtime: <tspan fill="#2997ff">Asynchronous Agent Loop</tspan></text>
  </g>

  <line x1="24" y1="36" x2="836" y2="36" stroke="#ffffff" stroke-opacity="0.06" stroke-width="1"/>

  <!-- 4 Interactive Pillar Cards -->
  <g transform="translate(24, 52)">
    <!-- Pillar 1: Autonomous AI -->
    <g transform="translate(0, 0)">
      <rect width="194" height="114" rx="10" fill="#ffffff" fill-opacity="0.03" stroke="#2997ff" stroke-opacity="0.25" stroke-width="0.8"/>
      <circle cx="16" cy="20" r="4" fill="#2997ff" class="chip-glow"/>
      <text x="28" y="24" fill="#f5f5f7" class="font-sans" font-size="12" font-weight="600">Autonomous Agents</text>
      <text x="14" y="48" fill="#86868b" class="font-mono" font-size="10">● Multi-Agent Chains</text>
      <text x="14" y="66" fill="#86868b" class="font-mono" font-size="10">● Tool-Calling Loops</text>
      <text x="14" y="84" fill="#86868b" class="font-mono" font-size="10">● Recursive Reasoning</text>
      <rect x="14" y="94" width="85" height="12" rx="4" fill="#2997ff" fill-opacity="0.15"/>
      <text x="18" y="103" fill="#2997ff" class="font-mono" font-size="8.5" font-weight="600">CREWAI &amp; PYTORCH</text>
    </g>

    <!-- Pillar 2: Real-time Voice -->
    <g transform="translate(206, 0)">
      <rect width="194" height="114" rx="10" fill="#ffffff" fill-opacity="0.03" stroke="#30d158" stroke-opacity="0.25" stroke-width="0.8"/>
      <circle cx="16" cy="20" r="4" fill="#30d158" class="chip-glow"/>
      <text x="28" y="24" fill="#f5f5f7" class="font-sans" font-size="12" font-weight="600">Real-Time Voice AI</text>
      <text x="14" y="48" fill="#86868b" class="font-mono" font-size="10">● Sub-300ms Audio I/O</text>
      <text x="14" y="66" fill="#86868b" class="font-mono" font-size="10">● Whisper Streaming STT</text>
      <text x="14" y="84" fill="#86868b" class="font-mono" font-size="10">● Low-Latency WebRTC</text>
      <rect x="14" y="94" width="80" height="12" rx="4" fill="#30d158" fill-opacity="0.15"/>
      <text x="18" y="103" fill="#30d158" class="font-mono" font-size="8.5" font-weight="600">WEBSOCKETS &amp; STT</text>
    </g>

    <!-- Pillar 3: 60fps Graphics & Web -->
    <g transform="translate(412, 0)">
      <rect width="194" height="114" rx="10" fill="#ffffff" fill-opacity="0.03" stroke="#ffffff" stroke-opacity="0.15" stroke-width="0.8"/>
      <circle cx="16" cy="20" r="4" fill="#ffffff" class="chip-glow"/>
      <text x="28" y="24" fill="#f5f5f7" class="font-sans" font-size="12" font-weight="600">Next.js 15 &amp; Canvas</text>
      <text x="14" y="48" fill="#86868b" class="font-mono" font-size="10">● 60fps Particle Physics</text>
      <text x="14" y="66" fill="#86868b" class="font-mono" font-size="10">● React 19 App Router</text>
      <text x="14" y="84" fill="#86868b" class="font-mono" font-size="10">● Glassmorphic Tokens</text>
      <rect x="14" y="94" width="75" height="12" rx="4" fill="#ffffff" fill-opacity="0.12"/>
      <text x="18" y="103" fill="#f5f5f7" class="font-mono" font-size="8.5" font-weight="600">TYPESCRIPT &amp; UI</text>
    </g>

    <!-- Pillar 4: Cloud & Distributed Backend -->
    <g transform="translate(618, 0)">
      <rect width="194" height="114" rx="10" fill="#ffffff" fill-opacity="0.03" stroke="#2997ff" stroke-opacity="0.25" stroke-width="0.8"/>
      <circle cx="16" cy="20" r="4" fill="#2997ff" class="chip-glow"/>
      <text x="28" y="24" fill="#f5f5f7" class="font-sans" font-size="12" font-weight="600">Distributed Cloud</text>
      <text x="14" y="48" fill="#86868b" class="font-mono" font-size="10">● FastAPI High-Speed I/O</text>
      <text x="14" y="66" fill="#86868b" class="font-mono" font-size="10">● Redis &amp; PostgreSQL</text>
      <text x="14" y="84" fill="#86868b" class="font-mono" font-size="10">● Dockerized Microservices</text>
      <rect x="14" y="94" width="75" height="12" rx="4" fill="#2997ff" fill-opacity="0.15"/>
      <text x="18" y="103" fill="#2997ff" class="font-mono" font-size="8.5" font-weight="600">DOCKER &amp; REDIS</text>
    </g>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

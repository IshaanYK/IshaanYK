import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "neural-terminal.svg")

W, H = 860, 220

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Obsidian Carbon Void -->
    <linearGradient id="cyberBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#14151a"/>
      <stop offset="5%" stop-color="#0d0e12"/>
      <stop offset="100%" stop-color="#050507"/>
    </linearGradient>

    <!-- Specular Light Sheen -->
    <linearGradient id="cyberSheen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.16"/>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- Titanium Laser Hairline Border -->
    <linearGradient id="laserBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2997ff" stop-opacity="0.8"/>
      <stop offset="35%" stop-color="#ffffff" stop-opacity="0.15"/>
      <stop offset="70%" stop-color="#30d158" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.05"/>
    </linearGradient>

    <!-- Holographic Radar Sweep -->
    <linearGradient id="radarSweep" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2997ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#2997ff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#2997ff" stop-opacity="0"/>
    </linearGradient>

    <pattern id="dotGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.8" fill="#ffffff" fill-opacity="0.06"/>
    </pattern>

    <style>
      .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", sans-serif; }}
      .font-mono {{ font-family: "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace; }}

      @keyframes radarMove {{
        0% {{ transform: translateX(-860px); }}
        100% {{ transform: translateX(860px); }}
      }}
      @keyframes pulseNode {{
        0%, 100% {{ opacity: 0.3; transform: scale(0.9); }}
        50% {{ opacity: 1; transform: scale(1.15); filter: drop-shadow(0 0 6px #2997ff); }}
      }}
      @keyframes waveFlux {{
        0%, 100% {{ d: path("M 0 30 Q 50 10 100 30 T 200 30 T 300 30 T 400 30"); }}
        50% {{ d: path("M 0 30 Q 50 50 100 30 T 200 10 T 300 45 T 400 30"); }}
      }}
      @keyframes agentPulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.4; }}
      }}

      .radar-bar {{ animation: radarMove 6s linear infinite; }}
      .node-glow {{ animation: pulseNode 3s infinite ease-in-out; transform-origin: center; }}
      .pulse-agent {{ animation: agentPulse 1.8s infinite; }}
    </style>
  </defs>

  <!-- Card Surface -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#cyberBg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#dotGrid)"/>
  <rect width="{W}" height="{H/2}" rx="14" fill="url(#cyberSheen)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#laserBorder)" stroke-width="1"/>

  <!-- Holographic Laser Radar Line -->
  <g class="radar-bar">
    <rect x="0" y="0" width="120" height="{H}" fill="url(#radarSweep)"/>
  </g>

  <!-- Title Header Bar -->
  <g transform="translate(24, 24)">
    <circle cx="0" cy="0" r="4" fill="#ffffff" fill-opacity="0.2"/>
    <circle cx="12" cy="0" r="4" fill="#ffffff" fill-opacity="0.2"/>
    <circle cx="24" cy="0" r="4" fill="#ffffff" fill-opacity="0.2"/>
    <text x="42" y="4" fill="#2997ff" class="font-mono" font-size="11.5" font-weight="700" letter-spacing="1px">AI AGENT SUPERVISOR KERNEL v4.2</text>
    <text x="640" y="4" fill="#30d158" class="font-mono" font-size="11" font-weight="600" class="pulse-agent">● 4 PERSISTENT THREADS ONLINE</text>
  </g>

  <line x1="0" y1="38" x2="{W}" y2="38" stroke="#ffffff" stroke-opacity="0.06" stroke-width="1"/>

  <!-- Left: Live Autonomous Subagent Monitor -->
  <g transform="translate(24, 58)">
    <text x="0" y="0" fill="#86868b" class="font-mono" font-size="10.5" font-weight="600">&#8212; ACTIVE AGENT WORKFLOWS</text>

    <!-- Subagent 1 -->
    <g transform="translate(0, 16)">
      <rect x="0" y="0" width="380" height="28" rx="6" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <circle cx="14" cy="14" r="3" fill="#2997ff" class="node-glow"/>
      <text x="26" y="18" fill="#f5f5f7" class="font-mono" font-size="11" font-weight="600">agent-voice-pipeline</text>
      <text x="265" y="18" fill="#30d158" class="font-mono" font-size="10.5">SUB-300ms STT/TTS</text>
    </g>

    <!-- Subagent 2 -->
    <g transform="translate(0, 48)">
      <rect x="0" y="0" width="380" height="28" rx="6" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <circle cx="14" cy="14" r="3" fill="#30d158" class="node-glow"/>
      <text x="26" y="18" fill="#f5f5f7" class="font-mono" font-size="11" font-weight="600">agent-rag-vector-mesh</text>
      <text x="265" y="18" fill="#2997ff" class="font-mono" font-size="10.5">SEMANTIC CACHE: HIT</text>
    </g>

    <!-- Subagent 3 -->
    <g transform="translate(0, 80)">
      <rect x="0" y="0" width="380" height="28" rx="6" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <circle cx="14" cy="14" r="3" fill="#ffffff" class="node-glow"/>
      <text x="26" y="18" fill="#f5f5f7" class="font-mono" font-size="11" font-weight="600">agent-daily-streak-sync</text>
      <text x="265" y="18" fill="#30d158" class="font-mono" font-size="10.5">189 COMMITS SYNCED</text>
    </g>

    <!-- Subagent 4 -->
    <g transform="translate(0, 112)">
      <rect x="0" y="0" width="380" height="28" rx="6" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <circle cx="14" cy="14" r="3" fill="#2997ff" class="node-glow"/>
      <text x="26" y="18" fill="#f5f5f7" class="font-mono" font-size="11" font-weight="600">agent-neural-canvas-60fps</text>
      <text x="265" y="18" fill="#f5f5f7" class="font-mono" font-size="10.5">LOCKED 16.6ms FRAME</text>
    </g>
  </g>

  <!-- Center Divider -->
  <line x1="430" y1="48" x2="430" y2="208" stroke="#ffffff" stroke-opacity="0.06" stroke-width="1"/>

  <!-- Right: Quantum Telemetry & System Gauges -->
  <g transform="translate(455, 58)">
    <text x="0" y="0" fill="#86868b" class="font-mono" font-size="10.5" font-weight="600">&#8212; HARDWARE &amp; REASONING TELEMETRY</text>

    <!-- Stat Grid -->
    <g transform="translate(0, 16)">
      <!-- Token Throughput -->
      <rect x="0" y="0" width="180" height="58" rx="8" fill="#ffffff" fill-opacity="0.03" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <text x="14" y="20" fill="#86868b" class="font-mono" font-size="10">TOKEN THROUGHPUT</text>
      <text x="14" y="44" fill="#2997ff" class="font-mono" font-size="18" font-weight="700">42.8k <tspan font-size="11" fill="#86868b">tok/sec</tspan></text>

      <!-- Context Compression -->
      <rect x="195" y="0" width="185" height="58" rx="8" fill="#ffffff" fill-opacity="0.03" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <text x="14" y="20" fill="#86868b" class="font-mono" font-size="10">CONTEXT WINDOW EFFICIENCY</text>
      <text x="14" y="44" fill="#30d158" class="font-mono" font-size="18" font-weight="700">99.4% <tspan font-size="11" fill="#86868b">compacted</tspan></text>
    </g>

    <g transform="translate(0, 84)">
      <!-- GPU Cluster Memory -->
      <rect x="0" y="0" width="180" height="56" rx="8" fill="#ffffff" fill-opacity="0.03" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <text x="14" y="20" fill="#86868b" class="font-mono" font-size="10">EMBEDDING LATENCY</text>
      <text x="14" y="42" fill="#f5f5f7" class="font-mono" font-size="17" font-weight="700">12.4ms <tspan font-size="11" fill="#30d158">OPTIMAL</tspan></text>

      <!-- Autonomous Convergence -->
      <rect x="195" y="0" width="185" height="56" rx="8" fill="#ffffff" fill-opacity="0.03" stroke="#ffffff" stroke-opacity="0.06" stroke-width="0.8"/>
      <text x="14" y="20" fill="#86868b" class="font-mono" font-size="10">AGENT TOOL CONSENSUS</text>
      <text x="14" y="42" fill="#2997ff" class="font-mono" font-size="17" font-weight="700">100% <tspan font-size="11" fill="#86868b">verified</tspan></text>
    </g>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

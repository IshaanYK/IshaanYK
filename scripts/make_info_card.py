import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 490, 330
PAD = 20
TITLEBAR_H = 32
KEY_X = PAD
VAL_X = PAD + 94
LINE_H = 20

ROWS = [
    ("host",),
    ("kv", "Role", "AI Engineer & Full-Stack Systems Architect"),
    ("kv", "Academy", "Indian Institute of Technology Madras"),
    ("kv", "Focus", "Autonomous Multi-Agent AI & Real-Time Voice"),
    ("kv", "Status", "Available for High-Impact Roles"),
    ("kv", "Portfolio", "ishaanyk.github.io/portfolio-me/"),
    ("gap",),
    ("sec", "Core Ecosystem"),
    ("kv", "Languages", "Python, TypeScript, JavaScript, SQL, C++"),
    ("kv", "AI & ML", "PyTorch, LangChain, CrewAI, RAG, Voice AI"),
    ("kv", "Full-Stack", "Next.js 15, React 19, FastAPI, Tailwind"),
    ("kv", "Cloud & DB", "Docker, PostgreSQL, Redis, GitHub Actions"),
    ("gap",),
    ("sec", "Engineering Passions"),
    ("bul", "Designing zero-lag autonomous agent loops & tools"),
    ("bul", "Crafting ultra-smooth 60fps dark-mode interfaces"),
]


def esc(s):
    return html.escape(s)


def rise(inner, i):
    if STATIC:
        return f"<g>{inner}</g>"
    delay = 0.05 + i * 0.03
    return (f'<g opacity="0" transform="translate(0,4)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.35s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 4" to="0 0" '
            f'begin="{delay:.2f}s" dur="0.35s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>')


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<defs>',
    '  <linearGradient id="infoGlossyBg" x1="0%" y1="0%" x2="0%" y2="100%">',
    '    <stop offset="0%" stop-color="#191a1e"/>',
    '    <stop offset="5%" stop-color="#111215"/>',
    '    <stop offset="100%" stop-color="#08080a"/>',
    '  </linearGradient>',
    '  <linearGradient id="infoSpecular" x1="0%" y1="0%" x2="0%" y2="100%">',
    '    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.12"/>',
    '    <stop offset="40%" stop-color="#ffffff" stop-opacity="0.02"/>',
    '    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>',
    '  </linearGradient>',
    '  <linearGradient id="infoBorder" x1="0%" y1="0%" x2="100%" y2="100%">',
    '    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2"/>',
    '    <stop offset="60%" stop-color="#ffffff" stop-opacity="0.06"/>',
    '    <stop offset="100%" stop-color="#ffffff" stop-opacity="0.02"/>',
    '  </linearGradient>',
    '  <style>',
    '    .font-sans { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif; }',
    '    .font-mono { font-family: "SF Mono", Menlo, Consolas, monospace; }',
    '    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }',
    '    .cursor { animation: blink 0.9s infinite; fill: #2997ff; }',
    '  </style>',
    '</defs>',
    f'<rect width="{W}" height="{H}" rx="14" fill="url(#infoGlossyBg)"/>',
    f'<rect width="{W}" height="{H/2}" rx="14" fill="url(#infoSpecular)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#infoBorder)" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="#ffffff" stroke-opacity="0.06"/>',
]

for i in range(3):
    parts.append(f'<circle cx="{PAD + i*14}" cy="{TITLEBAR_H/2}" r="4" fill="#ffffff" fill-opacity="0.2"/>')

parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="#86868b" class="font-mono" font-size="11" '
             f'text-anchor="middle">ishaan@machine: ~$ sysinfo <tspan class="cursor">_</tspan></text>')

y = TITLEBAR_H + 22
for i, row in enumerate(ROWS):
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.25
        continue
    if kind == "host":
        rule_x = KEY_X + 115
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-mono" font-size="12" font-weight="600">'
                 f'<tspan fill="#f5f5f7">ISHAANYK</tspan><tspan fill="#86868b">@</tspan>'
                 f'<tspan fill="#2997ff">github</tspan></text>'
                 f'<line x1="{rule_x}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="#ffffff" stroke-opacity="0.07"/>')
    elif kind == "sec":
        title = esc(row[1])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-sans" fill="#86868b" font-size="11" font-weight="600" letter-spacing="0.4px">'
                 f'&#8212; {title.upper()}</text>'
                 f'<line x1="{KEY_X + 10 + len(row[1])*7}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="#ffffff" stroke-opacity="0.07"/>')
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        val_color = "#30d158" if "Available" in val else ("#f5f5f7" if "IIT" in val else ("#2997ff" if "portfolio" in key.lower() else "#d2d2d7"))
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-mono" fill="#86868b" font-size="11">{key}</text>'
                 f'<text x="{VAL_X}" y="{y:.1f}" class="font-sans" fill="{val_color}" font-size="11">{val}</text>')
    elif kind == "bul":
        txt = esc(row[1])
        inner = (f'<circle cx="{KEY_X+3}" cy="{y-4:.1f}" r="2" fill="#2997ff"/>'
                 f'<text x="{KEY_X+12}" y="{y:.1f}" class="font-sans" fill="#d2d2d7" font-size="11">{txt}</text>')
    else:
        continue
    parts.append(rise(inner, i))
    y += LINE_H

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

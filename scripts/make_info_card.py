import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 490, 388
PAD = 22
TITLEBAR_H = 34
KEY_X = PAD
VAL_X = PAD + 98
LINE_H = 22

BG = "#0c0e14"
BG2 = "#06070a"
FRAME = "#23252a"
MUTED = "#8a8f98"
INK = "#f7f8f8"
KEY = "#828fff"
SECTION = "#00f2fe"
GREEN = "#27a644"
CYAN = "#00f2fe"
PURPLE = "#5e6ad2"
GOLD = "#f2cc60"

HOST = "ISHAANYK"

ROWS = [
    ("host",),
    ("kv", "Role", "AI Engineer & Full-Stack Systems Architect"),
    ("kv", "Academy", "Indian Institute of Technology Madras"),
    ("kv", "Specialty", "Autonomous Multi-Agent AI & Voice Systems"),
    ("kv", "Status", "🟢 Available for High-Impact Collabs"),
    ("kv", "Portfolio", "ishaanyk.github.io/portfolio-me/"),
    ("gap",),
    ("sec", "Core Tech Arsenal"),
    ("kv", "Languages", "Python, TypeScript, JavaScript, SQL, C++, Rust"),
    ("kv", "AI & Agents", "PyTorch, LangChain, CrewAI, RAG, Whisper/Voice AI"),
    ("kv", "Full-Stack", "Next.js 15, React 19, FastAPI, Node.js, Tailwind v4"),
    ("kv", "Infrastructure", "Docker, PostgreSQL, Redis, Pinecone, GitHub Actions"),
    ("gap",),
    ("sec", "Engineering Passions"),
    ("bul", "Designing zero-lag autonomous agent pipelines & tool-calling loops"),
    ("bul", "Crafting ultra-smooth 60fps+ dark-mode interfaces & 3D graphics"),
]


def esc(s):
    return html.escape(s)


def rise(inner, i):
    if STATIC:
        return f"<g>{inner}</g>"
    delay = 0.08 + i * 0.035
    return (f'<g opacity="0" transform="translate(0,5)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.4s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" '
            f'begin="{delay:.2f}s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>')


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<defs>',
    f'<linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">',
    f'<stop offset="0%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG}"/></linearGradient>',
    f'<linearGradient id="cardGlow" x1="0%" y1="0%" x2="100%" y2="100%">',
    f'<stop offset="0%" stop-color="{PURPLE}" stop-opacity="0.8"/>',
    f'<stop offset="50%" stop-color="{CYAN}" stop-opacity="0.4"/>',
    f'<stop offset="100%" stop-color="{PURPLE}" stop-opacity="0.7"/>',
    f'</linearGradient>',
    '<style>',
    '.font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", Roboto, sans-serif; }',
    '.font-mono { font-family: "SF Mono", "JetBrains Mono", "Fira Code", Menlo, monospace; }',
    '@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }',
    '.cursor { animation: blink 0.9s infinite; fill: #00f2fe; }',
    '</style>',
    '</defs>',
    f'<rect width="{W}" height="{H}" rx="14" fill="url(#cardBg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="url(#cardGlow)" stroke-width="1.2"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')

parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" class="font-mono" font-size="11.5" '
             f'text-anchor="middle">{esc(HOST)}@machine: ~$ sysinfo --verbose <tspan class="cursor">_</tspan></text>')

y = TITLEBAR_H + 26
for i, row in enumerate(ROWS):
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.35
        continue
    if kind == "host":
        host = esc(HOST)
        rule_x = KEY_X + (len(HOST) + 7) * 8 + 6
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-mono" font-size="13" font-weight="700">'
                 f'<tspan fill="{PURPLE}">{host}</tspan><tspan fill="{MUTED}">@</tspan>'
                 f'<tspan fill="{CYAN}">github</tspan></text>'
                 f'<line x1="{rule_x}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "sec":
        title = esc(row[1])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-sans" fill="{SECTION}" font-size="12" font-weight="700" letter-spacing="0.3px">'
                 f'&#8212; {title}</text>'
                 f'<line x1="{KEY_X + 14 + len(row[1])*7.2}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        val_color = GREEN if "🟢" in val else (GOLD if "IIT" in val else (CYAN if "portfolio" in key.lower() else INK))
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" class="font-mono" fill="{KEY}" font-size="11.5" font-weight="600">{key}</text>'
                 f'<text x="{VAL_X}" y="{y:.1f}" class="font-sans" fill="{val_color}" font-size="11.5" font-weight="400">{val}</text>')
    elif kind == "bul":
        txt = esc(row[1])
        inner = (f'<circle cx="{KEY_X+3}" cy="{y-4:.1f}" r="2.5" fill="{CYAN}"/>'
                 f'<text x="{KEY_X+14}" y="{y:.1f}" class="font-sans" fill="{INK}" font-size="11.5">{txt}</text>')
    else:
        continue
    parts.append(rise(inner, i))
    y += LINE_H

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

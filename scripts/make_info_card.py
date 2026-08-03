"""
Build a neofetch-style info card SVG (Andrew6rant style) to sit to the RIGHT of
the ASCII portrait: colored key/value rows for work experience, tech stack, and
highlights.
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 490, 376
PAD = 20
TITLEBAR_H = 32
KEY_X = PAD
VAL_X = PAD + 95
LINE_H = 21

BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
INK = "#e6edf3"
KEY = "#ffa657"      # orange keys
SECTION = "#4facfe"  # blue section headers
GREEN = "#3fb950"
CYAN = "#00f2fe"
PURPLE = "#a371f7"
GOLD = "#f2cc60"

HOST = "ISHAANYK"

ROWS = [
    ("host",),
    ("kv", "Role", "AI Engineer & Full-Stack Developer"),
    ("kv", "Edu", "Indian Institute of Technology Madras"),
    ("kv", "Focus", "Autonomous AI Agents & RAG Pipelines"),
    ("kv", "Status", "🟢 Available for AI/ML & Web Projects"),
    ("kv", "Portfolio", "ishaanyk.github.io/portfolio-me/"),
    ("gap",),
    ("sec", "Tech Ecosystem"),
    ("kv", "Languages", "Python, TypeScript, JavaScript, SQL"),
    ("kv", "AI / ML", "PyTorch, OpenAI API, LangChain, RAG"),
    ("kv", "FullStack", "React, Next.js, Node.js, FastAPI, Tailwind"),
    ("kv", "Infra", "Docker, PostgreSQL, Redis, AWS, GitHub Actions"),
    ("gap",),
    ("sec", "Highlights & Hobbies"),
    ("bul", "Building custom multi-agent autonomous tools"),
    ("bul", "Crafting ultra-smooth interactive UI/UX experiences"),
]


def esc(s):
    return html.escape(s)


def rise(inner, i):
    """fade + slight upward slide, staggered by row index; freezes visible."""
    if STATIC:
        return f"<g>{inner}</g>"
    delay = 0.10 + i * 0.04
    return (f'<g opacity="0" transform="translate(0,6)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.4s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 6" to="0 0" '
            f'begin="{delay:.2f}s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>')


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs>',
    f'<linearGradient id="ibg" x1="0%" y1="0%" x2="100%" y2="100%">',
    f'<stop offset="0%" stop-color="#0a0e17"/><stop offset="100%" stop-color="{BG}"/></linearGradient>',
    f'<linearGradient id="cardGlow" x1="0%" y1="0%" x2="100%" y2="100%">',
    f'<stop offset="0%" stop-color="{CYAN}"/>',
    f'<stop offset="50%" stop-color="{SECTION}"/>',
    f'<stop offset="100%" stop-color="{PURPLE}"/>',
    f'</linearGradient>',
    '<style>',
    '@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }',
    '.cursor { animation: blink 0.9s infinite; fill: #00f2fe; }',
    '</style>',
    '</defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="url(#cardGlow)" stroke-width="1.5" stroke-opacity="0.8"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')

parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">{esc(HOST)}@github: ~$ neofetch <tspan class="cursor">_</tspan></text>')

y = TITLEBAR_H + 26
for i, row in enumerate(ROWS):
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.4
        continue
    if kind == "host":
        host = esc(HOST)
        rule_x = KEY_X + (len(HOST) + 7) * 8 + 8
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" font-size="13.5" font-weight="700">'
                 f'<tspan fill="{GREEN}">{host}</tspan><tspan fill="{MUTED}">@</tspan>'
                 f'<tspan fill="{CYAN}">github</tspan></text>'
                 f'<line x1="{rule_x}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "sec":
        title = esc(row[1])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{SECTION}" font-size="12" font-weight="700">'
                 f'&#8212; {title}</text>'
                 f'<line x1="{KEY_X + 14 + len(row[1])*7.5}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        val_color = GREEN if "🟢" in val else (GOLD if "IIT" in val else INK)
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{KEY}" font-size="12" font-weight="700">{key}</text>'
                 f'<text x="{VAL_X}" y="{y:.1f}" fill="{val_color}" font-size="12">{val}</text>')
    elif kind == "bul":
        txt = esc(row[1])
        inner = (f'<circle cx="{KEY_X+3}" cy="{y-4:.1f}" r="2.5" fill="{CYAN}"/>'
                 f'<text x="{KEY_X+14}" y="{y:.1f}" fill="{INK}" font-size="12">{txt}</text>')
    else:
        continue
    parts.append(rise(inner, i))
    y += LINE_H

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT)

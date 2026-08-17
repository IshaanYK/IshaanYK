const fs = require('fs');
const path = require('path');

const inPath = path.join(__dirname, '..', 'data', 'contributions.json');
const outPath = path.join(__dirname, '..', 'contrib-heatmap.svg');

const data = JSON.parse(fs.readFileSync(inPath, 'utf-8'));

// GitHub Dark Palette: empty -> brightest emerald neon
const PALETTE = ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353', '#69f0a0'];

const CELL = 12;
const GAP = 3;
const STEP = CELL + GAP;
const PAD = 22;
const LEFT_LABEL_W = 30;
const TOP_LABEL_H = 20;
const TITLEBAR_H = 30;

const BG = '#0a0e14';
const BG2 = '#0d1420';
const FRAME = '#1f6feb';
const MUTED = '#7d8590';
const TEXT = '#e6edf3';
const ACCENT = '#22d3ee';
const GREEN = '#39d353';
const GOLD = '#f2cc60';

function levelFor(count) {
  if (!count || count === 0) return 0;
  if (count <= 2) return 1;
  if (count <= 6) return 2;
  if (count <= 12) return 3;
  if (count <= 20) return 4;
  return 5;
}

function buildGrid(days) {
  if (!days || days.length === 0) return [];
  const first = new Date(days[0].date);
  const leadPad = first.getUTCDay(); // Sunday = 0
  const grid = [];
  let col = new Array(leadPad).fill(null);

  for (const d of days) {
    const dt = new Date(d.date);
    const weekday = dt.getUTCDay();
    while (col.length < weekday) {
      col.push(null);
    }
    col.push({ date: d.date, count: d.count, level: levelFor(d.count) });
    if (col.length === 7) {
      grid.push(col);
      col = [];
    }
  }
  if (col.length > 0) {
    while (col.length < 7) {
      col.push(null);
    }
    grid.push(col);
  }
  return grid;
}

function render(data) {
  const days = data.days;
  const grid = buildGrid(days);
  const nCols = grid.length;
  const artW = nCols * STEP;
  const artH = 7 * STEP;

  const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const monthLabels = [];
  const seenMonths = new Set();

  grid.forEach((column, ci) => {
    for (const cell of column) {
      if (!cell) continue;
      const dt = new Date(cell.date);
      const m = dt.getUTCMonth();
      const y = dt.getUTCFullYear();
      const key = `${y}-${m}`;
      if (!seenMonths.has(key) && dt.getUTCDate() <= 8) {
        seenMonths.add(key);
        monthLabels.push({ ci, label: monthNames[m] });
      }
      break;
    }
  });

  const canvasW = PAD + LEFT_LABEL_W + artW + PAD;
  const statsH = 88;
  const canvasH = TITLEBAR_H + TOP_LABEL_H + artH + statsH + PAD;

  const css = `
    @keyframes cell {
      0%   { opacity: 0; transform: translateY(-6px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    .c { opacity: 0; animation: cell 0.42s cubic-bezier(.2,.8,.2,1) both; }
  `.trim();

  const parts = [
    `<svg xmlns="http://www.w3.org/2000/svg" width="${canvasW}" height="${canvasH}" viewBox="0 0 ${canvasW} ${canvasH}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">`,
    `<style>${css}</style>`,
    '<defs>',
    `<linearGradient id="hbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${BG2}"/><stop offset="100%" stop-color="${BG}"/></linearGradient>`,
    '</defs>',
    `<rect width="${canvasW}" height="${canvasH}" rx="12" fill="url(#hbg)"/>`,
    `<rect x="0.5" y="0.5" width="${canvasW - 1}" height="${canvasH - 1}" rx="12" fill="none" stroke="${FRAME}" stroke-width="1" stroke-opacity="0.55"/>`,
    `<line x1="0" y1="${TITLEBAR_H}" x2="${canvasW}" y2="${TITLEBAR_H}" stroke="${FRAME}" stroke-opacity="0.35"/>`
  ];

  const dotCols = ['#ff5f56', '#ffbd2e', '#27c93f'];
  dotCols.forEach((col, i) => {
    parts.push(`<circle cx="${PAD + i * 16}" cy="${TITLEBAR_H / 2}" r="5" fill="${col}"/>`);
  });

  parts.push(`<text x="${canvasW / 2}" y="${TITLEBAR_H / 2 + 4}" fill="${MUTED}" font-size="12" text-anchor="middle">ishaan@github: ~/contributions --graph</text>`);

  const gridTop = TITLEBAR_H + TOP_LABEL_H;
  const gridLeft = PAD + LEFT_LABEL_W;

  monthLabels.forEach(({ ci, label }) => {
    const x = gridLeft + ci * STEP;
    parts.push(`<text x="${x}" y="${TITLEBAR_H + 14}" fill="${MUTED}" font-size="10">${label}</text>`);
  });

  const weekLabels = [{ ri: 1, name: 'Mon' }, { ri: 3, name: 'Wed' }, { ri: 5, name: 'Fri' }];
  weekLabels.forEach(({ ri, name }) => {
    const y = gridTop + ri * STEP + CELL * 0.78;
    parts.push(`<text x="${PAD}" y="${y.toFixed(1)}" fill="${MUTED}" font-size="9">${name}</text>`);
  });

  grid.forEach((column, ci) => {
    const gx = gridLeft + ci * STEP;
    column.forEach((cell, ri) => {
      if (!cell) return;
      const gy = gridTop + ri * STEP;
      const delay = ci * 0.018 + ri * 0.045;
      const plural = cell.count !== 1 ? 's' : '';
      const color = PALETTE[cell.level];
      parts.push(
        `<rect class="c" x="${gx}" y="${gy}" width="${CELL}" height="${CELL}" rx="2.5" fill="${color}" style="animation-delay:${delay.toFixed(3)}s"><title>${cell.date}: ${cell.count} contribution${plural}</title></rect>`
      );
    });
  });

  // Legend
  const legY = gridTop + artH + 6;
  const legX = canvasW - PAD - (PALETTE.length * (CELL - 1) + 70);
  parts.push(`<text x="${legX}" y="${(legY + CELL * 0.8).toFixed(1)}" fill="${MUTED}" font-size="10" text-anchor="end">Less</text>`);
  let lx = legX + 8;
  PALETTE.forEach((col) => {
    parts.push(`<rect x="${lx}" y="${legY}" width="${CELL - 1}" height="${CELL - 1}" rx="2.2" fill="${col}"/>`);
    lx += CELL;
  });
  parts.push(`<text x="${lx + 4}" y="${(legY + CELL * 0.8).toFixed(1)}" fill="${MUTED}" font-size="10">More</text>`);

  const sepY = legY + CELL + 14;
  parts.push(`<line x1="0" y1="${sepY}" x2="${canvasW}" y2="${sepY}" stroke="${FRAME}" stroke-opacity="0.25"/>`);

  const cs = data.current_streak.length;
  const ls = data.longest_streak.length;
  const total = data.total_contributions;
  const best = data.best_day;
  const rng = data.range;

  let ly = sepY + 24;
  parts.push(
    `<text x="${PAD}" y="${ly}" font-size="13" fill="${GREEN}"><tspan font-weight="700">${total.toLocaleString()}</tspan><tspan fill="${MUTED}"> contributions in the last year</tspan></text>`
  );
  parts.push(
    `<text x="${canvasW - PAD}" y="${ly}" font-size="12" fill="${MUTED}" text-anchor="end">${rng.start} &#8594; ${rng.end}</text>`
  );

  ly += 24;
  parts.push(
    `<text x="${PAD}" y="${ly}" font-size="13" fill="${MUTED}">current streak <tspan fill="${ACCENT}" font-weight="700">${cs} days</tspan><tspan fill="${MUTED}">   &#183;   longest </tspan><tspan fill="${ACCENT}" font-weight="700">${ls} days</tspan></text>`
  );
  parts.push(
    `<text x="${canvasW - PAD}" y="${ly}" font-size="12" fill="${MUTED}" text-anchor="end">best day <tspan fill="${GOLD}" font-weight="700">${best.count}</tspan> on ${best.date}</text>`
  );

  parts.push('</svg>');
  return parts.join('');
}

const svg = render(data);
fs.writeFileSync(outPath, svg, 'utf-8');
console.log(`[OK] Successfully rendered ${outPath} (${svg.length} bytes)`);

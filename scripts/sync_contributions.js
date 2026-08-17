const https = require('https');
const fs = require('fs');
const path = require('path');

const username = 'IshaanYK';
const url = `https://github.com/users/${username}/contributions`;
const outPath = path.join(__dirname, '..', 'data', 'contributions.json');

console.log(`Fetching real GitHub contributions from: ${url}`);

https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' } }, (res) => {
  let html = '';
  res.on('data', chunk => html += chunk);
  res.on('end', () => {
    // Extract total contributions header
    const totalMatch = html.match(/([0-9,]+)\s+contributions\s+in\s+the\s+last\s+year/i);
    const reportedTotal = totalMatch ? parseInt(totalMatch[1].replace(/,/g, ''), 10) : 0;
    console.log(`Reported Total on GitHub: ${reportedTotal}`);

    // Parse all days and tooltips
    // Look for <tool-tip for="contribution-day-component-...">N contributions on Month D, YYYY</tool-tip>
    // or td with data-date
    const tooltips = {};
    const tooltipRegex = /<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]+)<\/tool-tip>/gi;
    let tm;
    while ((tm = tooltipRegex.exec(html)) !== null) {
      tooltips[tm[1]] = tm[2].trim();
    }

    const dayRegex = /<td[^>]*data-date="([^"]+)"[^>]*id="([^"]+)"[^>]*>/gi;
    const days = [];
    let dm;
    while ((dm = dayRegex.exec(html)) !== null) {
      const date = dm[1];
      const id = dm[2];
      const tip = tooltips[id] || '';
      let count = 0;
      if (/no contributions/i.test(tip)) {
        count = 0;
      } else {
        const countMatch = tip.match(/(\d+)\s+contribution/i);
        if (countMatch) {
          count = parseInt(countMatch[1], 10);
        }
      }
      days.push({ date, count });
    }

    // Also handle fallback if td doesn't have id or tooltips are different format
    if (days.length === 0) {
      const fallbackRegex = /data-date="([0-9]{4}-[0-9]{2}-[0-9]{2})"[^>]*data-level="([0-9]+)"/gi;
      let fm;
      while ((fm = fallbackRegex.exec(html)) !== null) {
        days.push({ date: fm[1], count: parseInt(fm[2], 10) });
      }
    }

    days.sort((a, b) => a.date.localeCompare(b.date));
    console.log(`Found ${days.length} calendar days.`);

    const parsedSum = days.reduce((sum, d) => sum + d.count, 0);
    console.log(`Parsed count sum: ${parsedSum}`);

    const actualTotal = Math.max(reportedTotal, parsedSum);

    // Compute streaks
    let curStreak = 0;
    let curStart = null;
    let curEnd = null;

    let idx = days.length - 1;
    if (idx >= 0 && days[idx].count === 0) {
      idx--; // today might be in progress
    }
    curEnd = idx >= 0 ? days[idx].date : null;
    while (idx >= 0 && days[idx].count > 0) {
      curStreak++;
      curStart = days[idx].date;
      idx--;
    }
    if (curStreak === 0) {
      curStart = null;
      curEnd = null;
    }

    let longestStreak = 0;
    let longestStart = null;
    let longestEnd = null;
    let run = 0;
    let runStart = null;

    for (let i = 0; i < days.length; i++) {
      if (days[i].count > 0) {
        if (run === 0) runStart = days[i].date;
        run++;
        if (run > longestStreak) {
          longestStreak = run;
          longestStart = runStart;
          longestEnd = days[i].date;
        }
      } else {
        run = 0;
      }
    }

    const bestDay = days.reduce((max, d) => (d.count > max.count ? d : max), { date: '', count: 0 });

    const data = {
      username,
      generated_at: new Date().toISOString(),
      range: {
        start: days.length > 0 ? days[0].date : '',
        end: days.length > 0 ? days[days.length - 1].date : ''
      },
      total_contributions: actualTotal,
      active_days: days.filter(d => d.count > 0).length,
      current_streak: {
        length: curStreak,
        start: curStart,
        end: curEnd
      },
      longest_streak: {
        length: longestStreak,
        start: longestStart,
        end: longestEnd
      },
      best_day: bestDay,
      days
    };

    fs.writeFileSync(outPath, JSON.stringify(data, null, 2), 'utf-8');
    console.log(`[OK] Successfully wrote ${outPath} with total ${actualTotal} contributions!`);
  });
}).on('error', (err) => {
  console.error('Error fetching contributions:', err);
});

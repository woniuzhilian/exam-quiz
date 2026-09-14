// T3: 列出 ,\cmd- 形式的全部不同字符串及所在 (id,field)
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'exam-quiz', 'src', 'data', 'questions.json'), 'utf8'));
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis'];
const B = String.fromCharCode(92);
const RE = new RegExp('.{0,12},' + B + B + '[A-Za-z]+.{0,6}', 'g');
const map = new Map();
for (const q of data) {
  for (const f of FIELDS) {
    const t = String(q[f] || '');
    const frags = t.match(new RegExp('\\$[^$]*\\$', 'g')) || [];
    for (const fr of frags) {
      const m = fr.match(RE);
      if (!m) continue;
      for (const s of m) {
        if (!/,\\[A-Za-z]/.test(s)) continue;
        const k = s;
        if (!map.has(k)) map.set(k, []);
        map.get(k).push(q.id + '/' + f);
      }
    }
  }
}
const out = [];
out.push('distinct=' + map.size);
for (const [k, v] of [...map.entries()].sort((a, b) => b[1].length - a[1].length)) {
  out.push(JSON.stringify(k) + '  n=' + v.length + '  ' + v.slice(0, 12).join(' '));
}
fs.writeFileSync(path.join(ROOT, '_t3_brk2.txt'), out.join('\r\n'), 'utf8');
console.log('ok');

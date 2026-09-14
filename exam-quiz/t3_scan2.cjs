// T3 补充扫描：[ ] 被转成 , - 的签名统计
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'exam-quiz', 'src', 'data', 'questions.json'), 'utf8'));
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis'];
const B = String.fromCharCode(92);

const pats = {
  'comma-backslash': new RegExp(',' + B + '[A-Za-z]+', 'g'),
  'bracket-pair-cmd': new RegExp(',' + B + '[A-Za-z]+-?', 'g'),
  'open-bracket': new RegExp('\\[', 'g'),
  'close-bracket': new RegExp('\\]', 'g'),
};
const res = {};
for (const k in pats) res[k] = { occ: 0, ids: new Set() };
for (const q of data) {
  for (const f of FIELDS) {
    const t = String(q[f] || '');
    for (const k in pats) {
      const m = t.match(pats[k]);
      if (m) { res[k].occ += m.length; res[k].ids.add(q.id); }
    }
  }
}
const out = [];
for (const k in res) out.push(k + ': occ=' + res[k].occ + ' q=' + res[k].ids.size);
// 逗号紧跟字母/数字 的签名（可能是 [ 丢失）
const ids2 = new Set(); let occ2 = 0;
for (const q of data) for (const f of FIELDS) {
  const t = String(q[f] || '');
  for (const frag of t.match(new RegExp('\\$[^$]*\\$', 'g')) || []) {
    const m = frag.match(/(\\[A-Za-z]+|[A-Za-z0-9}])?,[A-Za-z\\]/g);
    if (m) { occ2 += m.length; ids2.add(q.id); }
  }
}
out.push('comma-then-alnum-in-math: occ=' + occ2 + ' q=' + ids2.size);
out.push('ids(sample)=' + [...ids2].slice(0, 200).join(','));
fs.writeFileSync(path.join(ROOT, '_t3_scan2.txt'), out.join('\r\n'), 'utf8');
console.log('ok');

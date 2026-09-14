// 对比 T3 备份与当前题库，列出所有差异字段
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const a = JSON.parse(fs.readFileSync(path.join(ROOT, '_fix_backup', 'questions_BEFORE_T3.json'), 'utf8'));
const b = JSON.parse(fs.readFileSync(path.join(ROOT, 'exam-quiz', 'src', 'data', 'questions.json'), 'utf8'));
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis'];
const L = [];
L.push('count ' + a.length + ' -> ' + b.length);
const ma = new Map(a.map((q) => [q.id, q]));
let n = 0;
for (const q of b) {
  const o = ma.get(q.id);
  if (!o) { L.push('!! new id ' + q.id); continue; }
  for (const k of Object.keys(o)) {
    if (k === 'id') continue;
    if (JSON.stringify(o[k]) !== JSON.stringify(q[k])) { L.push('OTHERFIELD id=' + q.id + ' ' + k); n++; }
  }
  for (const f of FIELDS) if (o[f] !== q[f]) n++;
  const diff = FIELDS.filter((f) => o[f] !== q[f]);
  if (diff.length) L.push('id=' + q.id + ' :: ' + diff.join(','));
}
for (const o of a) if (!b.find((q) => q.id === o.id)) L.push('!! removed id ' + o.id);
L.unshift('changed fields total=' + n);
fs.writeFileSync(path.join(ROOT, '_t3_diffcheck.txt'), L.join('\r\n'), 'utf8');
console.log('changed=' + n);

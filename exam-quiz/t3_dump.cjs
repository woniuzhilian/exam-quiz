// T3 取证：把指定 id / 指定 token 命中的字段导出到 UTF-8 文本
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const DB = path.join(ROOT, 'exam-quiz', 'src', 'data', 'questions.json');
const data = JSON.parse(fs.readFileSync(DB, 'utf8'));
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis'];

function dumpIds(ids, tag) {
  const out = [];
  for (const id of ids) {
    const q = data.find((x) => x.id === id);
    if (!q) { out.push('!! missing ' + id); continue; }
    out.push('======== id=' + id + ' yearQnum=' + q.yearQnum + ' ========');
    for (const f of FIELDS) {
      const v = q[f];
      if (typeof v === 'string' && v.length) out.push('  [' + f + '] ' + v);
    }
  }
  fs.writeFileSync(path.join(ROOT, '_t3_dump_' + tag + '.txt'), out.join('\r\n'), 'utf8');
  console.log(tag + ' -> ' + out.length + ' lines');
}

const which = process.argv[2] || 'cdots';
const RE = {
  cdots: /\\cdots/,
  brk: /,\\[A-Za-z]+-/,
  theta: /\\Theta/,
  eps: /\\epsilon/,
  sig: /\\varsigma/,
}[which];
if (RE) {
  const ids = data.filter((q) => FIELDS.some((f) => RE.test(String(q[f] || '')))).map((q) => q.id);
  dumpIds(ids, which);
} else {
  dumpIds(which.split(',').map(Number), 'ids');
}

// katex_check.mjs — validate every $...$ span in questions.json using project's katex
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';

const PATH = process.argv[2] || 'src/data/questions.json';
const MODE = process.argv[3] || 'report'; // report | emit
const qs = JSON.parse(fs.readFileSync(PATH, 'utf8'));
const FIELDS = ['question','A','B','C','D','analysis'];

const spanRe = /\$([^$]+)\$/g;
let totalSpans = 0, errSpans = 0;
const errByQ = new Map();
const errDetail = [];

for (const q of qs) {
  for (const f of FIELDS) {
    const s = String(q[f] ?? '');
    let m;
    spanRe.lastIndex = 0;
    while ((m = spanRe.exec(s)) !== null) {
      totalSpans++;
      const tex = m[1];
      try {
        katex.renderToString(tex, { throwOnError: true, strict: false });
      } catch (e) {
        errSpans++;
        if (!errByQ.has(q.id)) errByQ.set(q.id, []);
        errByQ.get(q.id).push({ field: f, tex, msg: String(e.message).split('\n')[0].slice(0,90) });
        if (errDetail.length < 400) errDetail.push({ id: q.id, field: f, tex, msg: String(e.message).split('\n')[0].slice(0,90) });
      }
    }
  }
}
console.log(JSON.stringify({
  totalQuestions: qs.length,
  totalSpans,
  errSpans,
  affectedQuestions: errByQ.size,
}, null, 2));
if (MODE === 'emit') {
  const out = [...errByQ.entries()].map(([id, arr]) => ({ id, errors: arr }));
  fs.writeFileSync('katex_errors.json', JSON.stringify(out, null, 2), 'utf8');
  console.log('wrote katex_errors.json');
} else {
  console.log(JSON.stringify(errDetail.slice(0,120), null, 2));
}

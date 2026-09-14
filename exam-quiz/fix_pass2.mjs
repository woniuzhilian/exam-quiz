// fix_pass2.mjs — mechanical residual repairs
//  a) stray backslash before a digit:  10^{-\2} -> 10^{-2}
//  b) escaped apostrophes:             y\'  -> y'
//  c) unbalanced braces inside a $...$ span (close the opened groups)
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';

const PATH = process.argv[2] || 'src/data/questions.json';
const FIELDS = ['question','A','B','C','D','analysis'];
const qs = JSON.parse(fs.readFileSync(PATH, 'utf8'));

let a=0,b=0,c=0;
const cIds=new Set();

function fixSpan(inner, qid){
  let s = inner;
  // a) \ before digit
  const s1 = s.replace(/(?<!\\)\\(?=[0-9])/g, '');
  if (s1!==s){ a++; s=s1; }
  // b) \' -> '
  const s2 = s.replace(/\\'/g, "'");
  if (s2!==s){ b++; s=s2; }
  // c) close unbalanced braces (skip if \begin present to avoid cases env)
  if (!/\\begin/.test(s)) {
    const open = (s.match(/{/g)||[]).length;
    const close = (s.match(/}/g)||[]).length;
    if (open>close){
      // only when the excess opens look like ^{ or _{ or dangling {
      s = s + '}'.repeat(open-close);
      c++; cIds.add(qid);
    }
  }
  return s;
}

function walk(text, qid){
  if (!text || !text.includes('$')) return text;
  return text.replace(/\$([^$]*)\$/g, (full, inner) => '$'+fixSpan(inner,qid)+'$');
}

for (const q of qs) for (const f of FIELDS) if (typeof q[f]==='string') q[f]=walk(q[f], q.id);
fs.writeFileSync(PATH, JSON.stringify(qs,null,2),'utf8');
console.log(`pass2: digit-backslash=${a}, apostrophe=${b}, brace-close=${c} (qids ${cIds.size})`);

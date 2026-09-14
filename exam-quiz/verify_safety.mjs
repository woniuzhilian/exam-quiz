// verify_safety.mjs — confirm edits only touched $...$ spans; list non-math diffs
import fs from 'fs';
const before = JSON.parse(fs.readFileSync('../_fix_backup/questions_ORIGINAL.json','utf8'));
const after  = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
const bmap=new Map(before.map(q=>[q.id,q]));
function stripMath(s){ return String(s).replace(/\$[^$]*\$/g, '\u0001'); } // mask math spans
let nonMathDiffs=0;
for(const a of after){
  const b=bmap.get(a.id);
  for(const f of FIELDS){
    if(String(a[f])===String(b[f])) continue;
    if(stripMath(a[f])!==stripMath(b[f])){
      nonMathDiffs++;
      console.log(`NON-MATH DIFF id${a.id}.${f}`);
      console.log('  B:',String(b[f]).slice(0,200));
      console.log('  A:',String(a[f]).slice(0,200));
    }
  }
}
console.log('non-math diffs (should be 0):', nonMathDiffs);
// also confirm span count unchanged
function spans(s){ return (String(s).match(/\$[^$]*\$/g)||[]).length; }
let sc=0;
for(const a of after){ const b=bmap.get(a.id); for(const f of FIELDS){ if(spans(a[f])!==spans(b[f])){sc++; console.log('SPAN COUNT CHANGED', a.id, f, spans(b[f]),'->',spans(a[f])); } } }
console.log('span-count changes (should be 0):', sc);

import fs from 'fs';
const before = JSON.parse(fs.readFileSync('../_fix_backup/questions_BEFORE_TOKENS.json','utf8'));
const after = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const bmap = new Map(before.map(q=>[q.id,q]));
const FIELDS=['question','A','B','C','D','analysis'];
// ids with residual errors to inspect
const ids=[58,59,154,274,893,550,748,1398,291,651,421,963,789,23,6,501,983,1343,368,371,619,1334,613,1108,1211,848,172,292,410,550];
for(const id of ids){
  const b=bmap.get(id), a=after.find(q=>q.id===id);
  if(!b) continue;
  let printed=false;
  for(const f of FIELDS){
    if(String(b[f])!==String(a[f])){ printed=true; }
  }
  console.log(`==== id ${id} ====`);
  for(const f of FIELDS){
    const bv=String(b[f]), av=String(a[f]);
    // find difference region
    console.log(`  [${f}] BEFORE: ${bv.slice(0,220)}`);
    if(bv!==av) console.log(`  [${f}] AFTER : ${av.slice(0,220)}`);
  }
  console.log();
}

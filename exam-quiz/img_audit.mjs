import fs from 'fs';
import path from 'path';
const qs=JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
const refs=new Map(); // image src -> [ids]
for(const q of qs) for(const f of FIELDS){
  const s=String(q[f]??'');
  for(const m of s.matchAll(/<img\s+src="([^"]+)"/g)){
    const src=m[1];
    if(!refs.has(src)) refs.set(src,[]);
    refs.get(src).push(`${q.id}.${f}`);
  }
}
const roots=['public','dist'];
let missing=[], present=0;
for(const [src,users] of refs){
  const rel=src.replace(/^\//,'');
  const found=roots.some(r=>fs.existsSync(path.join(r,rel)));
  if(found) present++; else missing.push({src,users:users.slice(0,4),n:users.length});
}
console.log('distinct image refs:', refs.size, '| present:', present, '| missing:', missing.length);
for(const m of missing) console.log(`  MISSING ${m.src}  (used by ${m.n}: ${m.users.join(',')})`);

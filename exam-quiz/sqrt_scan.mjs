import fs from 'fs';
const qs = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
let n=0; const pats=new Map();
for(const q of qs) for(const f of FIELDS){
  const s=String(q[f]??'');
  for(const m of s.matchAll(/\$\\sqrt\$\s*([\s\S]{0,12})/g)){
    n++;
    const key=(m[1]||'').slice(0,6);
    pats.set(key,(pats.get(key)||0)+1);
  }
}
console.log('total $\\sqrt$ occurrences:', n);
for(const [k,v] of [...pats.entries()].sort((a,b)=>b[1]-a[1]).slice(0,40)) console.log(String(v).padStart(4), JSON.stringify(k));

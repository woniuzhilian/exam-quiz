import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';
const qs=JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
function renders(t){try{katex.renderToString(t,{throwOnError:true,strict:false});return true;}catch{return false;}}
let n=0; const samples=[];
for(const q of qs) for(const f of FIELDS){
  if(typeof q[f]!=='string')continue;
  for(const m of q[f].matchAll(/\\sqrt\{\}([\s\S]{0,6})/g)){ n++; if(samples.length<30)samples.push(`id${q.id}.${f} ${JSON.stringify(m[0])}`); }
}
console.log('sqrt{} occurrences:',n);
for(const s of samples) console.log(' ',s);

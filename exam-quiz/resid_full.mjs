import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';
const qs = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
const spanRe=/\$([^$]*)\$/g;
const out=[];
for(const q of qs){
  for(const f of FIELDS){
    const s=String(q[f]??''); let m; spanRe.lastIndex=0;
    while((m=spanRe.exec(s))!==null){
      try{ katex.renderToString(m[1],{throwOnError:true,strict:false}); }
      catch(e){ out.push({id:q.id, field:f, span:m[0]}); }
    }
  }
}
fs.writeFileSync('resid_full.json', JSON.stringify(out,null,2),'utf8');
console.log('count', out.length);
for(const o of out) console.log(`id${o.id}.${o.field} :: ${JSON.stringify(o.span)}`);

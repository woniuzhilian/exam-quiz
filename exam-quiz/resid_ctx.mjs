// resid_ctx.mjs — dump raw context of residual error spans
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';
const qs = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS=['question','A','B','C','D','analysis'];
const spanRe=/\$([^$]*)\$/g;
for(const q of qs){
  for(const f of FIELDS){
    const s=String(q[f]??''); let m; spanRe.lastIndex=0;
    while((m=spanRe.exec(s))!==null){
      try{ katex.renderToString(m[1],{throwOnError:true,strict:false}); }
      catch(e){
        const a=Math.max(0,m.index-60), b=Math.min(s.length,m.index+m[0].length+60);
        console.log(`id${q.id}.${f}: …${JSON.stringify(s.slice(a,b))}…`);
      }
    }
  }
}

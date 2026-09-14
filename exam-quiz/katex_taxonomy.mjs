// katex_taxonomy.mjs
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';
const qs = JSON.parse(fs.readFileSync('src/data/questions.json','utf8'));
const FIELDS = ['question','A','B','C','D','analysis'];
const spanRe = /\$([^$]+)\$/g;
const tax = new Map();
for (const q of qs) {
  for (const f of FIELDS) {
    const s = String(q[f] ?? '');
    let m; spanRe.lastIndex=0;
    while ((m = spanRe.exec(s)) !== null) {
      try { katex.renderToString(m[1], {throwOnError:true, strict:false}); }
      catch(e) {
        let msg = String(e.message).split('\n')[0];
        // normalize
        msg = msg.replace(/\\.{0,30}/, '\\TOKEN').replace(/position \d+/, 'position N');
        let key = msg;
        if (/Undefined control sequence/.test(msg)) key='UndefinedControl';
        else if (/Expected '}', got 'EOF'/.test(msg)) key="ExpectedBrace-EOF";
        else if (/Can't use function/.test(msg)) key="CantUseFunction";
        else if (/Expected group after/.test(msg)) key="ExpectedGroupAfter";
        else if (/Unexpected token/.test(msg)) key="UnexpectedToken";
        else if (/Expected '\\right'/.test(msg)) key="ExpectedRight";
        else if (/Invalid/.test(msg)) key="Invalid";
        tax.set(key,(tax.get(key)||0)+1);
      }
    }
  }
}
for (const [k,v] of [...tax.entries()].sort((a,b)=>b[1]-a[1])) console.log(String(v).padStart(5), k);

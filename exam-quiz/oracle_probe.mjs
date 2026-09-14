// oracle_probe.mjs
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';
function defined(cmd) {
  try { katex.renderToString(cmd, { throwOnError: true, strict: false }); return true; }
  catch (e) {
    const m = String(e.message);
    if (/Undefined control sequence/.test(m)) return false;
    return true; // defined but wrong usage
  }
}
for (const w of ['sqrt','cdot','cdotx','begin','end','in','varepsilonx','sum','sumM','DeltaE','pi','pid','g','m','b','e','f','r','a','c','sin','cos','times','leq','leqy','alpha','alphat','arcsin','nabla','varkappa','Y','X','curvearrowright']) {
  console.log(w.padEnd(16), defined('\\'+w));
}

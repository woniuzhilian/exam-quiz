// fix_pass3.mjs — render-safety repairs for residual OCR-garbled math spans
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';

const PATH = process.argv[2] || 'src/data/questions.json';
const FIELDS = ['question','A','B','C','D','analysis'];
const qs = JSON.parse(fs.readFileSync(PATH,'utf8'));

function renders(tex){ try{ katex.renderToString(tex,{throwOnError:true,strict:false}); return true;}catch{return false;} }

// explicit last-resort span overrides (exact source -> replacement)
const OVERRIDES = new Map(Object.entries({
  '\\mathbf{}': null,
}));

function repair(inner){
  if (renders(inner)) return inner;
  let s = inner;
  const rules = [
    [/\\\(/g, '('], [/\\\)/g, ')'],
    [/\\vec\\vec/g, '\\vec{}\\vec{}'],
    [/\\(sqrt|text|oint|vec|bar|hat|dot)(?![{\[a-zA-Z])/g, '\\$1{}'],
    [/\^(?=[\s）)。,，;；]|$)/g, '^{}'],
    [/(?<=[\s,，。])_(?=[\s,，。)]|$)/g, '_{}'],
    [/_$/g, '_{}'],
  ];
  for (const [re, rep] of rules){ const ns = s.replace(re, rep); if (ns!==s){ s=ns; if (renders(s)) return s; } }
  // double-superscript splitter: ^A ^B  -> ^A {}^{B}
  s = s.replace(/\^([0-9A-Za-z])\s+\^/g, '^{$1}{}^');
  if (renders(s)) return s;
  s = s.replace(/\^([0-9A-Za-z])/g, '^{$1}');
  if (renders(s)) return s;
  return s; // may still fail -> reported
}

let fixed=0, still=0; const stillList=[];
const qs2 = qs.map(q=>{
  const o={...q};
  for(const f of FIELDS){
    if(typeof o[f]!=='string') continue;
    o[f]=o[f].replace(/\$([^$]*)\$/g,(full,inner)=>{
      const r=repair(inner);
      if(r!==inner){ fixed++; }
      if(!renders(r)){ still++; stillList.push({id:q.id,field:f,span:'$'+r+'$'}); }
      return '$'+r+'$';
    });
  }
  return o;
});
fs.writeFileSync(PATH, JSON.stringify(qs2,null,2),'utf8');
console.log('spans repaired:',fixed,'| still failing:',still);
for(const x of stillList) console.log('  STILL', x.id, x.field, JSON.stringify(x.span));

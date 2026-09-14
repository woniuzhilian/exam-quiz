// fix_tokens.mjs — split glued LaTeX commands using katex as the validity oracle
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';

const PATH = process.argv[2] || 'src/data/questions.json';
const FIELDS = ['question','A','B','C','D','analysis'];

function ok(tex) {
  try { katex.renderToString(tex, { throwOnError: true, strict: false }); return true; }
  catch { return false; }
}

// longest prefix of `word` such that \prefix renders successfully
function bestPrefix(word) {
  for (let L = word.length; L >= 1; L--) {
    if (ok('\\' + word.slice(0, L) + '{}')) return word.slice(0, L);
  }
  return null;
}

function splitWord(word) {
  const out = [];
  let i = 0;
  while (i < word.length) {
    const sub = word.slice(i);
    const p = bestPrefix(sub);
    if (p) { out.push(p); i += p.length; }
    else { out.push(sub[0]); i += 1; } // leave stray letter as variable
  }
  return out;
}

let splitCount = 0;
function fixSpans(text) {
  if (!text || !text.includes('$')) return text;
  return text.replace(/\$([^$]*)\$/g, (full, inner) => {
    const nw = inner.replace(/(?<!\\)\\([A-Za-z]+)/g, (m, word) => {
      const parts = splitWord(word);
      const joined = parts.map(p => '\\' + p).join(' ');
      if (joined !== '\\' + word) splitCount++;
      return joined;
    });
    return '$' + nw + '$';
  });
}

const qs = JSON.parse(fs.readFileSync(PATH, 'utf8'));
for (const q of qs) for (const f of FIELDS) if (typeof q[f] === 'string') q[f] = fixSpans(q[f]);
fs.writeFileSync(PATH, JSON.stringify(qs, null, 2), 'utf8');
console.log('split tokens:', splitCount);

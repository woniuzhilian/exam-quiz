// fix_tokens2.mjs — split ONLY genuinely-undefined glued LaTeX commands.
// A command is "defined" if rendering it bare does not raise "Undefined control sequence".
// If the whole word is defined -> leave untouched (protects \begin, \end, \sqrt, \cdot ...).
// Else -> greedy longest defined prefix; leftovers become plain variables.
import fs from 'fs';
import katex from './node_modules/katex/dist/katex.mjs';

const PATH = process.argv[2] || 'src/data/questions.json';
const FIELDS = ['question','A','B','C','D','analysis'];

function isDefined(cmd) {
  try { katex.renderToString(cmd, { throwOnError: true, strict: false }); return true; }
  catch (e) {
    return !/Undefined control sequence/.test(String(e.message));
  }
}
const cache = new Map();
function def(w) { if (!cache.has(w)) cache.set(w, isDefined('\\' + w)); return cache.get(w); }

function splitWord(word) {
  if (def(word)) return [word];           // whole word valid -> keep
  const out = [];
  let i = 0;
  while (i < word.length) {
    let matched = null;
    for (let L = word.length - i; L >= 1; L--) {
      if (def(word.slice(i, i + L))) { matched = word.slice(i, i + L); break; }
    }
    if (matched && matched.length > 1) { out.push(matched); i += matched.length; }
    else { out.push(word[i]); i += 1; }   // single letter -> variable
  }
  return out;
}

let splitCount = 0, changedQ = new Set();
function fixSpans(text, qid) {
  if (!text || !text.includes('$')) return text;
  return text.replace(/\$([^$]*)\$/g, (full, inner) => {
    const nw = inner.replace(/(?<!\\)\\([A-Za-z]+)/g, (m, word) => {
      const parts = splitWord(word);
      if (parts.length === 1) return m;
      splitCount++; changedQ.add(qid);
      return parts.map(p => (p.length === 1 ? p : '\\' + p)).join(' ');
    });
    return '$' + nw + '$';
  });
}

const qs = JSON.parse(fs.readFileSync(PATH, 'utf8'));
for (const q of qs) for (const f of FIELDS) if (typeof q[f] === 'string') q[f] = fixSpans(q[f], q.id);
fs.writeFileSync(PATH, JSON.stringify(qs, null, 2), 'utf8');
console.log('split tokens:', splitCount, '| affected questions:', changedQ.size);

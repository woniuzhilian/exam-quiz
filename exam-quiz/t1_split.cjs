// 拆分 T1：题干/选项侧 vs 仅解析侧（判定式与 formula_tiers.cjs 保持完全一致）
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_t1_split.txt')
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))
const STEM = ['question', 'A', 'B', 'C', 'D']

const DOLLAR = String.fromCharCode(36)
const vis = h => h.replace(/<[^>]+>/g, '')
function render(t) {
  const re = new RegExp('\\' + DOLLAR + '([^' + DOLLAR + ']+)\\' + DOLLAR, 'g')
  return t.replace(re, (m, f) => {
    try { return katex.renderToString(f, { throwOnError: false, displayMode: false, output: 'html' }) } catch (e) { return m }
  })
}
const RE_CMD = new RegExp('\\\\[a-zA-Z]{2,}', 'g')
const RE_OUTSIDE = new RegExp('\\\\[a-zA-Z]{2,}|(?<![A-Za-z0-9_])[A-Za-z]_[{]?[0-9]')
const RE_ADJ = new RegExp('\\' + DOLLAR + '\\' + DOLLAR)
const RE_BOUND = /\\(?:int|sum)\s*[:：]?\s*\\infty/

function t1Hit(t) {
  const out = []
  if (RE_ADJ.test(t)) out.push('相邻双美元')
  const v = vis(render(t))
  if (v.indexOf(DOLLAR) >= 0) out.push('页面残留美元')
  const lk = v.match(RE_CMD)
  if (lk) out.push('泄漏命令:' + Array.from(new Set(lk)).slice(0, 2).join('+'))
  if (RE_BOUND.test(t)) out.push('积分级数限丢失')
  const placeholder = String.fromCharCode(0)
  const outside = vis(t.replace(new RegExp('\\' + DOLLAR + '([^' + DOLLAR + ']+)\\' + DOLLAR, 'g'), placeholder)
    .split(placeholder).join(''))
  if (RE_OUTSIDE.test(outside)) out.push('片段外裸LaTeX')
  return out
}

const stemSide = [], anaOnly = []
for (const q of data) {
  let sSig = []
  for (const f of STEM) sSig = sSig.concat(t1Hit(q[f] || '').map(x => x + '@' + f))
  const aSig = t1Hit(q.analysis || '').map(x => x + '@解析')
  if (sSig.length) stemSide.push({ id: q.id, big: q.bigSubject, yr: q.year, n: q.yearQnum, sig: sSig })
  else if (aSig.length) anaOnly.push({ id: q.id, big: q.bigSubject, yr: q.year, n: q.yearQnum, sig: aSig })
}

const L = []
L.push('T1 题干/选项侧受影响: ' + stemSide.length + ' 题')
L.push('T1 仅解析侧受影响    : ' + anaOnly.length + ' 题')
L.push('T1 合计              : ' + (stemSide.length + anaOnly.length) + ' 题')
L.push('')
L.push('===== 题干/选项侧清单 =====')
for (const e of stemSide) {
  const kinds = Array.from(new Set(e.sig.map(x => x.split('@')[0])))
  L.push('id=' + e.id + ' [' + e.big + ' ' + e.yr + '-' + e.n + '] ' + kinds.join(';'))
}
L.push('')
L.push('===== 仅解析侧 id 列表 =====')
L.push(anaOnly.map(e => e.id).join(', '))
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('stemSide=%d anaOnly=%d', stemSide.length, anaOnly.length)

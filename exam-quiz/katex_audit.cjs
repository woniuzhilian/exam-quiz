// 用 KaTeX 本身审计 questions.json：抓取渲染错误、残留 $、空公式
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_katex_audit.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))

const errKind = new Map()      // 错误信息 -> 例子列表
const errIds = new Map()       // 错误信息 -> Set(id)
const leftover = []            // 渲染后仍残留 $ 的字段
const emptyD = []              // 含 $$ 的字段
const affected = new Set()

function renderLatex(text) {
  let hadErr = false
  const html = text.replace(/\$([^$]+)\$/g, (match, formula) => {
    let out
    try {
      out = katex.renderToString(formula, { throwOnError: false, displayMode: false })
    } catch (e) {
      out = match
      hadErr = true
      return out
    }
    if (out.includes('katex-error')) {
      hadErr = true
      const m = /class="latex"[^>]*>([^<]*)</.exec(out) || /KaTeX parse error: ([^<&]*)/.exec(out)
      const msg = (m ? m[1] : '未知错误').trim() || '未知错误'
      if (!errKind.has(msg)) errKind.set(msg, [])
      if (!errIds.has(msg)) errIds.set(msg, new Set())
      errIds.get(msg).add(currentId)
      if (errKind.get(msg).length < 6) errKind.get(msg).push({ id: currentId, f: currentField, src: formula })
    }
    return out
  })
  return { html, hadErr }
}

let currentId = null, currentField = null
for (const q of data) {
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    currentId = q.id; currentField = f
    if (/\$\$/.test(t)) emptyD.push({ id: q.id, f, s: t })
    const dollarCount = (t.match(/\$/g) || []).length
    const { html, hadErr } = renderLatex(t)
    const stillDollar = (html.match(/\$/g) || []).length
    if (stillDollar > 0) leftover.push({ id: q.id, f, n: stillDollar, odd: dollarCount % 2 === 1, s: t })
    if (hadErr) affected.add(q.id)
  }
}

const L = []
L.push('题库总数: ' + data.length)
L.push('渲染出错涉及的题目数: ' + affected.size)
L.push('残留 $ 的字段数: ' + leftover.length + '  (其中 $ 个数为奇数: ' + leftover.filter(x => x.odd).length + ')')
L.push('含 $$ 的字段数: ' + emptyD.length)
L.push('')
L.push('===== KaTeX 错误信息 TOP =====')
;[...errIds.entries()].sort((a, b) => b[1].size - a[1].size).forEach(([msg, set]) => {
  L.push('[' + set.size + ' 题] ' + msg)
  for (const e of errKind.get(msg)) L.push('      id=' + e.id + ' ' + e.f + ': ' + e.src.slice(0, 110))
})
L.push('')
L.push('===== 残留 $ 明细(前 40) =====')
for (const x of leftover.slice(0, 40)) L.push('id=' + x.id + ' ' + x.f + ' 残留' + x.n + '个 奇数=' + x.odd + ' :: ' + x.s.replace(/\s+/g, ' ').slice(0, 150))
L.push('')
L.push('===== 含 $$ 明细(前 40) =====')
for (const x of emptyD.slice(0, 40)) L.push('id=' + x.id + ' ' + x.f + ' :: ' + x.s.replace(/\s+/g, ' ').slice(0, 150))

fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('written', OUT)

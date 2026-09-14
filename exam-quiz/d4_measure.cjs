// 收紧上下标塌陷判定：只保留"字母紧跟单个数字"，排除数字在前(合法系数)、
// 排除命令名尾部、排除单位/度数等常见语境，并抽样供人工核验
const fs = require('fs')
const path = require('path')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_formula_d4.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))
const L = []

// 已知命令名(去掉反斜杠)——其尾字母后的数字是合法写法，如 \sqrt3 \log2
const CMD = new Set(('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega'
  + ' Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega'
  + ' sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh log ln lg exp lim max min det dim gcd'
  + ' int sum prod oint iint iiint sqrt frac dfrac tfrac binom leq geq neq approx infty cdots ldots dots'
  + ' rightarrow leftarrow Rightarrow Leftarrow Leftrightarrow to mapsto sim simeq cong neq equiv'
  + ' partial nabla in notin subset supset cup cap emptyset varnothing forall exists'
  + ' mathrm mathbf mathbb mathcal mathit text operatorname begin end cases matrix pmatrix bmatrix'
  + ' left right big Big bigg Bigg overline underline hat bar vec dot ddot tilde circ degree'
  + ' times div cdot pm mp le lt gt ge ne langle rangle lbrack rbrack').split(' '))

const hits = []
for (const q of data) {
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    const spans = [...t.matchAll(/\$([^$]+)\$/g)].map(m => m[1])
    if (!spans.length) continue
    const found = []
    for (const body of spans) {
      // 把 \command 整体替换成占位符，避免命令尾字母误判
      let s = body.replace(/\\([a-zA-Z]+)/g, (m, n) => CMD.has(n) ? '\u0001'.repeat(n.length + 1) : m)
      // 已经是 _{..} 或 ^{..} 或 _x 的部分不算塌陷
      s = s.replace(/[_^]\{[^{}]*\}/g, '\u0002').replace(/[_^]\d/g, '\u0002')
      // 度数/百分比等
      s = s.replace(/\d\s*[{[]?\s*(?:circ|degree|deg)\s*[}]]?/g, '\u0002')
      for (const m of s.matchAll(/([A-Za-z])(\d)(?![\dA-Za-z.])/g)) {
        found.push(m[1] + m[2])
      }
    }
    if (found.length) hits.push({ id: q.id, f, big: q.bigSubject, yr: q.year, tok: [...new Set(found)].join(' '), s: t })
  }
}

const ids = new Set(hits.map(x => x.id))
const qIds = new Set(hits.filter(x => x.f !== 'analysis').map(x => x.id))
L.push('收紧后的"字母紧跟单数字"命中：字段=' + hits.length + '  题目=' + ids.size +
  '  题干/选项侧=' + qIds.size + '  仅解析侧=' + (ids.size - qIds.size))
L.push('')
L.push('--- 按 token 频次 TOP30 ---')
const freq = new Map()
for (const h of hits) for (const tk of h.tok.split(' ')) freq.set(tk, (freq.get(tk) || 0) + 1)
;[...freq.entries()].sort((a, b) => b[1] - a[1]).slice(0, 30).forEach(([k, v]) => L.push('  ' + k + '  ' + v))
L.push('')
L.push('--- 随机抽样 40 条供人工核验 ---')
const step = Math.max(1, Math.floor(hits.length / 40))
for (let i = 0; i < hits.length; i += step) {
  const h = hits[i]
  L.push('id=' + h.id + ' [' + h.big + ' ' + h.yr + '] ' + h.f + ' {' + h.tok + '} :: ' + h.s.replace(/\s+/g, ' ').slice(0, 140))
}
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('written', hits.length, ids.size)

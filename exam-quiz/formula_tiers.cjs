// 计算严重度分层并输出各层题号清单(含 year/yearQnum 便于回原卷定位)
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_formula_tiers.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))

const vis = h => h.replace(/<[^>]+>/g, '')
const render = t => t.replace(/\$([^$]+)\$/g, (m, f) => {
  try { return katex.renderToString(f, { throwOnError: false, displayMode: false, output: 'html' }) } catch (e) { return m }
})

const CMD = new Set(('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega '
  + 'Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh log ln lg exp lim max min det '
  + 'int sum prod oint iint iiint sqrt frac dfrac tfrac binom leq geq neq approx infty cdots ldots dots rightarrow leftarrow Rightarrow Leftarrow '
  + 'Leftrightarrow to mapsto sim simeq equiv partial nabla in notin subset supset cup cap emptyset forall exists mathrm mathbf mathbb mathcal '
  + 'text operatorname begin end cases matrix pmatrix left right big overline underline hat bar vec dot ddot tilde circ').split(' '))

const tiers = { T1: new Map(), T2: new Map(), T3: new Map(), T4: new Map() }
function put(tier, q, sig) {
  const m = tiers[tier]
  if (!m.has(q.id)) m.set(q.id, { q, sigs: new Set() })
  m.get(q.id).sigs.add(sig)
}

for (const q of data) {
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    const side = f === 'analysis' ? '解析' : f
    // T1: 页面上露出原始 LaTeX / 残留 $ / 积分求和限丢失
    if (/\$\$/.test(t)) put('T1', q, `相邻$$(${side})`)
    if (vis(render(t)).includes('$')) put('T1', q, `页面残留美元符(${side})`)
    const lk = vis(render(t)).match(/\\[a-zA-Z]{2,}/g)
    if (lk) put('T1', q, `泄漏命令${[...new Set(lk)].slice(0,3).join(',') }(${side})`)
    if (/\\(?:int|sum)\s*[:：]?\s*\\infty/.test(t)) put('T1', q, `积分/级数限丢失(${side})`)
    const outside = vis(t.replace(/\$([^$]+)\$/g, '\u0000').replace(/\u0000/g, ''))
    if (/\\[a-zA-Z]{2,}|(?<![A-Za-z0-9_])[A-Za-z]_\{?\d/.test(outside)) put('T1', q, `片段外裸LaTeX(${side})`)
    // T2: 片段内上下标塌陷(先对所有 \命令 与已有上下标等长打码,避免命令尾数字误判)
    for (const m of t.matchAll(/\$([^$]+)\$/g)) {
      let s = m[1].replace(/\\[a-zA-Z]+/g, mm => '#'.repeat(mm.length))
      s = s.replace(/[_^]\{[^{}]*\}/g, '##').replace(/[_^][A-Za-z0-9]/g, '##')
      if (/([A-Za-z])(\d{1,2})(?![\dA-Za-z.])/.test(s)) { put('T2', q, `上下标塌陷(${side})`); break }
    }
    // T3: 符号错映射
    if (/\\varsigma/.test(t)) put('T3', q, `反斜杠varsigma应为sigma(${side})`)
    if (/\\cdots\^|kN\$\\cdots\$|\$\\cdots\$\/m/.test(t)) put('T3', q, `cdots错用(${side})`)
    if (/E\$\\Theta|\$\\Theta\s*[<(]|\\Theta\(/.test(t)) put('T3', q, `Theta应为ominus(${side})`)
    // T4: 题干称"如图"却无配图（遗留项，供后续）
  }
}

// 高优先：T1 中题干/选项侧受影响的排前面
function rank(e) {
  const q = e.q
  const stemSide = [...e.sigs].some(s => !/\(解析\)$/.test(s))
  return [stemSide ? 0 : 1, q.bigSubject === '专业基础' ? 0 : 1, q.id]
}
const L = []
L.push('T1 定界符/裸LaTeX/积分限丢失（页面上直接露出源码，最刺眼）: ' + tiers.T1.size + ' 题')
L.push('T2 片段内上下标塌陷: ' + tiers.T2.size + ' 题')
L.push('T3 符号错映射: ' + tiers.T3.size + ' 题')
const t1only = [...tiers.T1.keys()].filter(i => !tiers.T2.has(i))
L.push('T1∩T2 同时命中: ' + [...tiers.T1.keys()].filter(i => tiers.T2.has(i)).length + ' 题; 仅T1: ' + t1only.length)
L.push('')
L.push('===== T1 清单（题干/选项侧优先）=====')
for (const e of [...tiers.T1.values()].sort((a, b) => { const r = rank(a), s = rank(b); return r[0] - s[0] || r[1] - s[1] || r[2] - s[2] })) {
  L.push('id=' + e.q.id + ' [' + e.q.bigSubject + ' ' + e.q.year + '-' + e.q.yearQnum + '] ' + [...e.sigs].join('; '))
}
L.push('')
L.push('===== T3 清单 =====')
for (const e of [...tiers.T3.values()]) L.push('id=' + e.q.id + ' [' + e.q.bigSubject + ' ' + e.q.year + '-' + e.q.yearQnum + '] ' + [...e.sigs].join('; '))
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('T1=%d T2=%d T3=%d', tiers.T1.size, tiers.T2.size, tiers.T3.size)

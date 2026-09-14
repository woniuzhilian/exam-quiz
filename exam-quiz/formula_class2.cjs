// 精确版公式损坏分桶：用 output:'html' 去掉 MathML/annotation 干扰，收紧误报规则
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_formula_class2.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))

function appRender(text) {
  return text.replace(/\$([^$]+)\$/g, (m, f) => {
    try {
      return katex.renderToString(f, { throwOnError: false, displayMode: false, output: 'html' })
    } catch (e) { return m }
  })
}
const visible = h => h.replace(/<[^>]+>/g, '')

const buckets = {}
const add = (k, r) => { (buckets[k] = buckets[k] || []).push(r) }

for (const q of data) {
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    const rec = { id: q.id, f, big: q.bigSubject, yr: q.year, s: t }

    // D1: $$ 相邻（定界符粘连）
    if (/\$\$/.test(t)) add('D1_相邻$$', rec)

    // D2: 应用渲染后页面上仍看得到 $
    const html = appRender(t)
    const vis = visible(html)
    if (vis.includes('$')) add('D2_页面残留$', rec)

    // D3: 页面上看得到原始 LaTeX 命令（真正的泄漏）
    const leak = vis.match(/\\[a-zA-Z]{2,}/g)
    if (leak) add('D3_页面泄漏LaTeX命令', { ...rec, extra: [...new Set(leak)].slice(0, 6).join(' ') })

    // D4: 数学片段内上下标塌陷 —— 先剔除所有 \command，再找 字母紧邻数字
    let subHit = null
    for (const m of t.matchAll(/\$([^$]+)\$/g)) {
      const stripped = m[1].replace(/\\[a-zA-Z]+/g, '\u0001')
      const hits = stripped.match(/(?<![{}\u0001\\])[a-zA-Z]\d|(?<![{}\u0001\\])\d[a-zA-Z](?![a-zA-Z])/g)
      if (hits && hits.length) { subHit = hits.slice(0, 8).join(' '); break }
    }
    if (subHit) add('D4_片段内上下标塌陷', { ...rec, extra: subHit })

    // D5: 积分/求和上下限丢失（只抓明确的粘连形态）
    const bound = t.match(/\\(?:int|sum|lim)(?:\s*[:：])?\s*(?:\\infty|\+\\infty|-\\infty|\\limits)/g)
    if (bound && /\\infty/.test(bound.join(''))) add('D5_积分求和限丢失', { ...rec, extra: bound.slice(0, 3).join(' | ') })

    // D6: 已知符号错映射
    if (/\\varsigma/.test(t)) add('D6a_\\varsigma应为\\sigma', rec)
    if (/\\cdots\^|kN\$\\cdots\$|\$\\cdots\$\/m/.test(t)) add('D6b_\\cdots错映射(应为\\cdot)', rec)
    if (/E\$\\Theta|\$\\Theta\s*[<(]|\\Theta\(/.test(t)) add('D6c_\\Theta应为\\ominus', rec)

    // D7: 数学片段外裸露的 LaTeX 碎片（该包进 $ 的没包）
    const outside = visible(t.replace(/\$([^$]+)\$/g, '\u0000').replace(/\u0000/g, ''))
      .replace(/<[^>]+>/g, '')
    const frag = outside.match(/\\[a-zA-Z]{2,}|(?<![A-Za-z0-9_])[A-Za-z]_\{?\d|_\{?\d\}/g)
    if (frag) add('D7_片段外裸露LaTeX碎片', { ...rec, extra: [...new Set(frag)].slice(0, 6).join(' ') })
  }
}

const L = []
L.push('题库 ' + data.length + ' 题。以下为收紧规则后的统计（同一字段可命中多类）')
L.push('')
let qAll = new Set()
for (const k of Object.keys(buckets).sort()) {
  const arr = buckets[k]
  const ids = new Set(arr.map(x => x.id))
  const qIds = new Set(arr.filter(x => x.f !== 'analysis').map(x => x.id))
  ids.forEach(i => qAll.add(i))
  L.push('===== ' + k + ' =====')
  L.push('  字段=' + arr.length + '  题目=' + ids.size + '  其中题干/选项侧题目=' + qIds.size + '  仅解析侧=' + (ids.size - qIds.size))
  for (const x of arr.slice(0, 6)) {
    L.push('    id=' + x.id + ' [' + x.big + ' ' + x.yr + '] ' + x.f + (x.extra ? ' {' + x.extra + '}' : '') + ' :: ' + x.s.replace(/\s+/g, ' ').slice(0, 120))
  }
  L.push('')
}
L.push('合计至少命中一类损坏的题目数: ' + qAll.size + ' / ' + data.length)
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('written')

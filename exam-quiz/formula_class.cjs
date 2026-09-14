// 精确分桶统计公式损坏类型，输出各类数量与代表样例
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_formula_class.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))

// 复刻应用的渲染逻辑，检测"原始 LaTeX 泄漏"
function appRender(text) {
  return text.replace(/\$([^$]+)\$/g, (m, f) => {
    try { return katex.renderToString(f, { throwOnError: false, displayMode: false }) } catch (e) { return m }
  })
}
function stripTags(h) { return h.replace(/<[^>]+>/g, '') }

const buckets = {}
function add(key, rec) {
  if (!buckets[key]) buckets[key] = []
  buckets[key].push(rec)
}

const spanRe = /\$([^$]+)\$/g
for (const q of data) {
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    const rec = { id: q.id, f, big: q.bigSubject, s: t }

    // S1 定界符损坏
    if (/\$\$/.test(t)) add('S1a_相邻$$', rec)
    const html = appRender(t)
    const residual = (stripTags(html).match(/\$/g) || []).length
    if (residual > 0) add('S1b_渲染后残留$', rec)

    // S2 渲染后正文里仍出现反斜杠命令 = 原始 LaTeX 泄漏
    const plain = stripTags(html)
    const leak = plain.match(/\\[a-zA-Z]{2,}/g)
    if (leak) add('S2_正文泄漏LaTeX命令', { ...rec, extra: [...new Set(leak)].slice(0, 5).join(' ') })

    // S3 数学片段内的下标塌陷：字母/命令后紧跟数字（无 _ 或 ^）
    let subHit = null
    for (const m of t.matchAll(spanRe)) {
      const body = m[1]
      const hits = body.match(/(?:\\[a-zA-Z]+|[a-zA-Z])\s*[0-9](?![{}._^a-zA-Z])/g)
      if (hits && hits.length) { subHit = hits.slice(0, 6).join(' '); break }
    }
    if (subHit) add('S3_片段内下标塌陷', { ...rec, extra: subHit })

    // S4 已知符号错映射
    if (/\\varsigma/.test(t)) add('S4a_\\varsigma(应为\\sigma)', rec)
    if (/\\cdots(?![a-zA-Z])/.test(t) && !/\\cdots\s*[.,;]/.test(t)) add('S4b_\\cdots(疑应为\\cdot)', rec)
    if (/\\Theta/.test(t)) add('S4c_\\Theta(疑应为\\ominus)', rec)

    // S5 极限/积分上下限塌陷
    if (/\\lim(?!_)/.test(t)) add('S5a_\\lim无下标', rec)
    if (/\\int(?![_^])/.test(t)) add('S5b_\\int无上下限', rec)
    if (/\\sum(?![_^])/.test(t)) add('S5c_\\sum无上下标', rec)

    // S6 数学片段外的裸公式文本（该包 $ 却没包）
    const outside = t.replace(spanRe, '\u0000')
    if (/[a-zA-Z]_\{?\d|\\frac|\\sqrt|\\leq|\\geq|\\times/.test(outside.replace(/\u0000/g, ''))) {
      add('S6_片段外含LaTeX碎片', { ...rec, extra: (outside.match(/\\[a-zA-Z]+|_\{?\d/g) || []).slice(0, 5).join(' ') })
    }
  }
}

const L = []
L.push('题库 ' + data.length + ' 题；按字段统计各类损坏命中数（同一字段可入多类）')
L.push('')
for (const k of Object.keys(buckets).sort()) {
  const arr = buckets[k]
  const ids = new Set(arr.map(x => x.id))
  const qside = new Set(arr.filter(x => x.f !== 'analysis').map(x => x.id))
  L.push('===== ' + k + ' =====')
  L.push('  字段数=' + arr.length + '  涉及题目=' + ids.size + '  其中题干/选项侧=' + qside.size)
  L.push('  样例:')
  for (const x of arr.slice(0, 8)) {
    L.push('    id=' + x.id + ' [' + x.big + '] ' + x.f + (x.extra ? ' {' + x.extra + '}' : '') + ' :: ' + x.s.replace(/\s+/g, ' ').slice(0, 130))
  }
  L.push('')
}
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('written')

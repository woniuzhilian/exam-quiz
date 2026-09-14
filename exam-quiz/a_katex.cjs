// 校验 a_apply.py 里手写的解析：逐段 $..$ 用 KaTeX 严格渲染，抓未知命令/括号不配对
const fs = require('fs')
const path = require('path')
const katex = require('katex')

const NEW = path.join(__dirname, '..', process.argv[2] || '_a_new.json')
const OUT = path.join(__dirname, '..', process.argv[3] || '_a_katex.txt')
const obj = JSON.parse(fs.readFileSync(NEW, 'utf8'))

const L = []
let nbad = 0, nfield = 0
for (const id of Object.keys(obj).sort((a, b) => a - b)) {
  for (const f of Object.keys(obj[id])) {
    const t = obj[id][f]
    nfield++
    const problems = []
    const dollars = (t.match(/\$/g) || []).length
    if (dollars % 2) problems.push('$ 个数为奇数(' + dollars + ')')
    if (/\$\$/.test(t)) problems.push('出现相邻 $$')
    if (/\\\s*\$/.test(t)) problems.push('转义 \\$')
    const frags = []
    t.replace(/\$([^$]*)\$/g, (m, x) => { frags.push(x); return m })
    frags.forEach((x, i) => {
      if (!x.trim()) { problems.push('第' + (i + 1) + '段为空'); return }
      try {
        katex.renderToString(x, { throwOnError: true, displayMode: false, strict: 'ignore', output: 'html' })
      } catch (e) {
        problems.push('第' + (i + 1) + '段渲染失败: ' + String(e.message || e).slice(0, 90) + ' <<' + x.slice(0, 70) + '>>')
      }
    })
    if (problems.length) {
      nbad++
      L.push('id=' + id + ' ' + f)
      for (const p of problems) L.push('    - ' + p)
    }
  }
}
L.unshift('待写入字段=' + nfield + '  不合格=' + nbad)
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
console.log('fields=' + nfield + ' bad=' + nbad)

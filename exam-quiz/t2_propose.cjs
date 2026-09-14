// 由量测结论生成 T2 改写提案(仅取 score>0 的 SUP/SUB 站点), 输出可人工审阅的字面替换表
const fs = require('fs')
const V = JSON.parse(fs.readFileSync('_t2_verdicts.json', 'utf8'))
const DB = JSON.parse(fs.readFileSync('exam-quiz/src/data/questions.json', 'utf8'))
const BYID = new Map(DB.map(q => [q.id, q]))

const groups = new Map()
for (const x of V) {
  if (x.v !== 'SUP' && x.v !== 'SUB') continue
  if (!(x.score > 0)) continue
  const key = x.id + '|' + x.f + '|' + x.letter + x.digits + '|' + x.v
  if (!groups.has(key)) groups.set(key, { id: x.id, f: x.f, letter: x.letter, digits: x.digits, v: x.v,
    n: 0, sc: 0, pdfBefore: '', pdfAfter: '', ctx: [] })
  const g = groups.get(key)
  const top = (x.sample && x.sample[0]) || {}
  if ((top.score || 0) >= g.sc) {
    g.sc = top.score || 0
    g.pdfBefore = top.before || ''
    g.pdfAfter = top.after || ''
  }
  g.n++
  g.ctx.push(JSON.stringify(x.sample[0].before) + ' <<' + x.letter + x.digits + '>> ' + JSON.stringify(x.sample[0].after))
}

const L = []
const rules = []
let flagged = 0
for (const g of [...groups.values()].sort((a, b) => a.id - b.id || a.f.localeCompare(b.f))) {
  const q = BYID.get(g.id)
  const field = q[g.f] || ''
  const old = g.letter + g.digits
  const occ = field.split(old).length - 1
  const mark = g.v === 'SUP' ? '^{' : '_{'
  const neu = g.letter + mark + g.digits + '}'
  const bad = []
  if (g.sc < 4) bad.push('LOWSCORE=' + g.sc)
  if (occ !== g.n) bad.push('OCC=' + occ + '!=SITES=' + g.n)
  if (g.digits === '1' && g.v === 'SUP') bad.push('上标1可疑')
  if (g.v === 'SUP' && /[01]/.test(g.digits.slice(-1))) bad.push('末位0/1需查')
  if (g.letter === 'W') bad.push('W疑为omega')
  L.push('id=' + g.id + ' ' + g.f + ' ' + JSON.stringify(old) + ' -> ' + JSON.stringify(neu) +
    ' sites=' + g.n + ' occ=' + occ + ' sc=' + g.sc +
    (bad.length ? '  !!' + bad.join(',') : ''))
  L.push('      pdf: ' + JSON.stringify(g.pdfBefore) + ' <<' + old + '>> ' + JSON.stringify(g.pdfAfter))
  if (!bad.length) rules.push({ id: g.id, f: g.f, old, neu, count: g.n })
  else flagged++
}
fs.writeFileSync('_t2_proposals.txt', L.join('\n'), 'utf8')
fs.writeFileSync('_t2_rules.json', JSON.stringify(rules, null, 1), 'utf8')
console.log('groups=' + groups.size + ' clean_rules=' + rules.length + ' flagged=' + flagged)

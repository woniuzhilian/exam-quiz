const fs = require('fs')
const V = JSON.parse(fs.readFileSync('_t2_verdicts.json', 'utf8'))
const order = ['SUP', 'SUB', 'SUP?', 'SUB?', 'INLINE', 'AMBIG', 'WEAK', 'NOMATCH', 'NOTLOCATED', 'NOBOOK']
const L = []
const by = new Map()
for (const v of V) { if (!by.has(v.v)) by.set(v.v, []); by.get(v.v).push(v) }
for (const k of order) {
  const arr = by.get(k) || []
  L.push('===== ' + k + '  站点=' + arr.length + ' 题数=' + new Set(arr.map(x => x.id)).size + ' =====')
  for (const x of arr) {
    L.push('  id=' + x.id + ' ' + x.f + ' [' + x.big + ' ' + x.y + '-' + x.yn + '] ' +
      x.letter + x.digits + ' ctx=' + JSON.stringify(x.ctx) +
      (x.pages ? ' pg=' + x.path.slice(0, 6) + ':' + x.pages.join(',') : '') +
      (x.score !== undefined ? ' sc=' + x.score : '') +
      (x.sample ? ' top=' + JSON.stringify(x.sample[0]) : '') +
      (x.all ? ' all=' + x.all.join(',') : ''))
  }
  L.push('')
}
fs.writeFileSync('_t2_report.txt', L.join('\n'), 'utf8')
console.log('written ' + V.length)

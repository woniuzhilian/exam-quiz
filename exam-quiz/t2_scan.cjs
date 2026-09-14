// T2 分型普查 v2：等长掩码(命令名/已有上下标整体打码，长度不变 => 下标可直接映射回原文)
const fs = require('fs')
const path = require('path')

const DB = path.join(__dirname, 'src', 'data', 'questions.json')
const OUT = path.join(__dirname, '..', '_t2_scan.txt')
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis']
const data = JSON.parse(fs.readFileSync(DB, 'utf8'))

const CMDS = new Set(('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega'
  + ' Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega varepsilon varsigma varphi vartheta'
  + ' sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh log ln lg exp lim max min det gcd'
  + ' int sum prod oint iint iiint sqrt frac dfrac tfrac binom leq geq neq approx infty cdots ldots dots'
  + ' rightarrow leftarrow Rightarrow Leftarrow Leftrightarrow to mapsto sim simeq equiv partial nabla'
  + ' in notin subset supset cup cap emptyset forall exists mathrm mathbf mathbb mathcal mathit text'
  + ' mbox operatorname begin end cases matrix pmatrix left right big Big bigg Bigg overline underline'
  + ' hat bar vec dot ddot tilde widetilde widehat circ odot oplus otimes infty lbrace rbrace'
  + ' Theta theta neq').split(' '))

// 掩码：\command 与 _{..} ^{..} _d ^d 用等长 # 替换，其余原样 => 位置不变
function mask(frag) {
  let s = frag.replace(/\\[a-zA-Z]+/g, m => (CMDS.has(m.slice(1)) || /^[a-zA-Z]+$/.test(m.slice(1)))
    ? '#'.repeat(m.length) : m)
  s = s.replace(/[_^]\{[^{}]*\}/g, m => '#'.repeat(m.length))
  s = s.replace(/[_^][A-Za-z0-9]/g, '##')
  return s
}

// 命中：字母紧跟数字；数字可 1~2 位
function hits(frag) {
  const s = mask(frag)
  const out = []
  const re = /([A-Za-z])(\d{1,2})(?![\dA-Za-z])/g
  let m
  while ((m = re.exec(s))) {
    const i = m.index
    out.push({
      i,
      letter: m[1],
      digits: m[2],
      // 原文上下文(用原始 frag 切片，位置一一对应)
      ctx: frag.slice(Math.max(0, i - 10), i + 1 + m[2].length + 10),
      // 字母前一个字符：判断是否 \command 尾部或另一字母
      prev: i > 0 ? frag[i - 1] : '',
      // 数字后面
      next: frag.slice(i + 1 + m[2].length, i + 1 + m[2].length + 1)
    })
  }
  return out
}

const NUMISH = new Set('0123456789')
function bucket(frag, h) {
  const c = h.ctx
  if (/\\cdots\s*[\^_{]/.test(c) || /\\cdots\^/.test(c)) return 'B-cdots当乘号'
  if (/[-−;]\s*$/.test(c.slice(0, 11)) && /^[12]/.test(h.digits)) return 'A-负指数丢失(^{1}应为^{-1})'
  if (h.digits.length === 1 && /[A-Za-z]$/.test(c.slice(0, 11)) === false) {
    // 单位类：字母是 m/g/s/J/K/P 等且紧跟 ^{n} 形式已丢
    if (/[{]\^?\d*[}]|\\mathrm/.test(c)) return 'D-单位或mathrm内数字'
  }
  if (/^\\pm|^\\times|^\\cdot/.test(c) ) return 'Z-命令尾误命中'
  return 'E-其它待判'
}

const rows = []
const byBucket = new Map()
let nfrag = 0, nhit = 0
for (const q of data) {
  const per = []
  for (const f of FIELDS) {
    const t = q[f] || ''
    if (!t) continue
    for (const m of t.matchAll(/\$([^$]+)\$/g)) {
      const hs = hits(m[1])
      if (!hs.length) continue
      nfrag++; nhit += hs.length
      const bs = []
      for (const h of hs) {
        const b = bucket(m[1], h)
        bs.push(b)
        if (!byBucket.has(b)) byBucket.set(b, new Set())
        byBucket.get(b).add(q.id)
      }
      per.push({ f, frag: m[1], hs, bs })
    }
  }
  if (per.length) rows.push({ id: q.id, y: q.year, yn: q.yearQnum, big: q.bigSubject, small: q.smallSubject, per })
}

const L = []
L.push('T2 v2  题数=' + rows.length + '  片段=' + nfrag + '  命中点=' + nhit)
L.push('')
L.push('===== 分桶(题数, 一题可多桶) =====')
for (const b of [...byBucket.keys()].sort()) L.push(b + ': ' + byBucket.get(b).size)
L.push('')
L.push('===== 明细 =====')
for (const r of rows) {
  L.push('id=' + r.id + ' [' + (r.big || '') + '/' + (r.small || '') + ' ' + r.y + '-' + r.yn + ']')
  for (const p of r.per) {
    L.push('  ' + p.f + ' <' + p.frag.slice(0, 130) + '>')
    p.hs.forEach((h, k) => L.push('      [' + p.bs[k] + '] @' + h.i + ' prev=' + JSON.stringify(h.prev) +
      ' next=' + JSON.stringify(h.next) + ' ctx=' + JSON.stringify(h.ctx)))
  }
}
fs.writeFileSync(OUT, L.join('\n'), 'utf8')
const sites = []
for (const r of rows) {
  for (const p of r.per) {
    for (const h of p.hs) {
      sites.push({ id: r.id, y: r.y, yn: r.yn, big: r.big, small: r.small, f: p.f, frag: p.frag,
                   i: h.i, letter: h.letter, digits: h.digits, prev: h.prev, next: h.next, ctx: h.ctx })
    }
  }
}
fs.writeFileSync(path.join(__dirname, '..', '_t2_sites.json'), JSON.stringify(sites, null, 1), 'utf8')
console.log('q=' + rows.length + ' frags=' + nfrag + ' hits=' + nhit + ' sites=' + sites.length)

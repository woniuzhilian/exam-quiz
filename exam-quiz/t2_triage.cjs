// T2 分诊：把"上下标塌陷"拆成可机械判定/必须重录两类，输出签名分布
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'src', 'data', 'questions.json'), 'utf8'));
const FIELDS = ['question', 'A', 'B', 'C', 'D', 'analysis'];

const CMD = new Set(('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega '
  + 'Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh log ln lg exp lim max min det '
  + 'int sum prod oint iint iiint sqrt frac dfrac tfrac binom leq geq neq approx infty cdots ldots dots rightarrow leftarrow Rightarrow Leftarrow '
  + 'Leftrightarrow to mapsto sim simeq equiv partial nabla in notin subset supset cup cap emptyset forall exists mathrm mathbf mathbb mathcal '
  + 'text operatorname begin end cases matrix pmatrix left right big overline underline hat bar vec dot ddot tilde circ').split(' '));

const stat = {};
const idsBy = {};
const detail = [];
function hit(sig, id, f, ctx) {
  stat[sig] = (stat[sig] || 0) + 1;
  (idsBy[sig] = idsBy[sig] || new Set()).add(id);
  detail.push([id, f, sig, ctx]);
}

for (const q of data) {
  for (const f of FIELDS) {
    const t = String(q[f] || '');
    if (!t) continue;
    const frags = t.match(/\$[^$]+\$/g) || [];
    for (const fr of frags) {
      const inner = fr.slice(1, -1);
      let m;
      // G2: \已知命令 紧跟数字   例 \sigma2  \omega2
      const r2 = /\\([a-zA-Z]+)([0-9])/g;
      while ((m = r2.exec(inner))) {
        if (CMD.has(m[1])) hit('G2 命令+数字', q.id, f, m[0]);
      }
      // G1: 字母紧跟数字，数字后不接字母/数字/点（先屏蔽命令与已带上下标的写法）
      let s = inner.replace(/\\([a-zA-Z]+)/g, (mm, n) => (CMD.has(n) ? ' ' : mm));
      s = s.replace(/[_^]\{[^{}]*\}/g, '#').replace(/[_^][A-Za-z0-9](?![A-Za-z0-9])/g, '#');
      s = s.replace(/[_^][0-9]/g, '#');
      const r1 = /([A-Za-z])([0-9])(?![0-9A-Za-z.])/g;
      while ((m = r1.exec(s))) hit('G1 字母+数字', q.id, f, s.slice(Math.max(0, m.index - 12), m.index + 12));
    }
    // G3: 字段尾部悬挂的下标串  例 ...$X$  1 2 n$   /  结尾 "$1 2 n$"
    const tail = t.slice(-30);
    if (/\$[0-9 ]{2,}[a-z]?[0-9 ]*\$[^\$]{0,3}$/.test(tail) || /[A-Za-z][0-9]? ?\$[0-9 ]{2,}\$[^\$]{0,3}$/.test(tail)) {
      hit('G3 尾部悬挂下标串', q.id, f, tail);
    }
  }
}

const out = [];
out.push('=== 签名分布（命中次数 / 题数）===');
for (const k of Object.keys(stat).sort()) out.push(k + ': ' + stat[k] + ' 次 / ' + idsBy[k].size + ' 题');
out.push('');
out.push('=== G2 按 token 聚合 ===');
const byCmd = {};
for (const d of detail) if (d[2] === 'G2 命令+数字') byCmd[d[3]] = (byCmd[d[3]] || 0) + 1;
for (const k of Object.keys(byCmd).sort((a, b) => byCmd[b] - byCmd[a])) out.push('  ' + JSON.stringify(k) + ' x' + byCmd[k]);
out.push('');
out.push('=== 各签名题号 ===');
for (const k of Object.keys(idsBy).sort()) out.push(k + ' => ' + [...idsBy[k]].join(','));
out.push('');
out.push('=== 样例 ===');
for (const g of Object.keys(stat).sort()) {
  out.push('--- ' + g);
  detail.filter((d) => d[2] === g).slice(0, 60).forEach((d) => out.push('  id=' + d[0] + ' ' + d[1] + ' :: ' + JSON.stringify(d[3])));
}
fs.writeFileSync(path.join(ROOT, '_t2_triage.txt'), out.join('\r\n'), 'utf8');
console.log(Object.keys(stat).sort().map((k) => k + '=' + idsBy[k].size + '题/' + stat[k] + '次').join('  '));

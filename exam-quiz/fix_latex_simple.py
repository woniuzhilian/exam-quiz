import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 1. 修复2013-15题
for q in questions:
    if q['year'] == '2013' and q.get('yearQnum') == 15:
        q['question'] = r'已知直线$L:\frac{x}{3}=\frac{y+1}{-1}=\frac{z-3}{2}$，平面$\pi:-2x+2y+z-1=0$，则：（　　）。'
        q['A'] = r'$L$与$\pi$垂直相交'
        q['B'] = r'$L$平行于$\pi$但$L$不在$\pi$上'
        q['C'] = r'$L$与$\pi$非垂直相交'
        q['D'] = r'$L$在$\pi$上'
        q['analysis'] = r'判定直线和平面位置关系。直线$L$的方向向量为$s=(3,-1,2)$，平面的法向量为$n=(-2,2,1)$。由于$s\cdot n=3\times(-2)+(-1)\times2+2\times1=-6\neq0$，且$s$与$n$不成比例，所以非垂直相交。答案选【C】'
        print('已修复2013-15')
        break

# 2. 批量修复选项中单独的 \pi, \alpha, \beta 等
# 常见的需要包裹的命令
simple_cmds = [
    r'\\pi', r'\\alpha', r'\\beta', r'\\gamma', r'\\delta', r'\\theta',
    r'\\lambda', r'\\mu', r'\\sigma', r'\\omega', r'\\rho', r'\\tau',
    r'\\phi', r'\\varphi', r'\\epsilon', r'\\varepsilon', r'\\infty',
    r'\\pm', r'\\mp', r'\\times', r'\\div', r'\\cdot', r'\\leq', r'\\geq',
    r'\\neq', r'\\approx', r'\\circ', r'\\degree', r'\\angle', r'\\perp',
    r'\\parallel', r'\\triangle', r'\\nabla', r'\\partial', r'\\sqrt',
    r'\\frac', r'\\int', r'\\sum', r'\\lim', r'\\sin', r'\\cos', r'\\tan',
    r'\\log', r'\\ln', r'\\rightarrow', r'\\leftarrow', r'\\Rightarrow',
    r'\\Leftarrow', r'\\leftrightarrow', r'\\Leftrightarrow', r'\\to',
    r'\\infty', r'\\pm', r'\\mp', r'\\times', r'\\div', r'\\cdot',
    r'\\leq', r'\\geq', r'\\neq', r'\\approx', r'\\equiv', r'\\sim',
    r'\\subset', r'\\supset', r'\\subseteq', r'\\supseteq', r'\\in',
    r'\\cup', r'\\cap', r'\\emptyset', r'\\forall', r'\\exists',
    r'\\neg', r'\\land', r'\\lor', r'\\dots', r'\\cdots', r'\\vdots',
    r'\\ddots', r'\\hat', r'\\bar', r'\\vec', r'\\dot', r'\\ddot',
    r'\\overline', r'\\underline', r'\\widehat', r'\\widetilde',
    r'\\Gamma', r'\\Delta', r'\\Theta', r'\\Lambda', r'\\Xi', r'\\Pi',
    r'\\Sigma', r'\\Upsilon', r'\\Phi', r'\\Psi', r'\\Omega',
    r'\\arcsin', r'\\arccos', r'\\arctan', r'\\sinh', r'\\cosh', r'\\tanh',
    r'\\arg', r'\\dim', r'\\hom', r'\\ker', r'\\sup', r'\\inf',
    r'\\limsup', r'\\liminf', r'\\max', r'\\min', r'\\det', r'\\gcd',
    r'\\Pr', r'\\bmod', r'\\pmod', r'\\deg', r'\\arg',
    r'\\le', r'\\ge', r'\\ne', r'\\ll', r'\\gg', r'\\prec', r'\\succ',
    r'\\preceq', r'\\succeq', r'\\subsetneq', r'\\supsetneq',
    r'\\sqsubset', r'\\sqsupset', r'\\sqsubseteq', r'\\sqsupseteq',
    r'\\sqcup', r'\\sqcap', r'\\vee', r'\\wedge', r'\\uplus', r'\\amalg',
    r'\\diamond', r'\\bullet', r'\\star', r'\\ast', r'\\circ',
    r'\\oplus', r'\\ominus', r'\\otimes', r'\\oslash', r'\\odot',
    r'\\dagger', r'\\ddagger', r'\\wr', r'\\amalg',
    r'\\triangleleft', r'\\triangleright',
    r'\\bigtriangleup', r'\\bigtriangledown',
    r'\\lhd', r'\\rhd', r'\\unlhd', r'\\unrhd',
    r'\\therefore', r'\\because', r'\\propto', r'\\asymp',
    r'\\bowtie', r'\\Join', r'\\smile', r'\\frown',
    r'\\models', r'\\vdash', r'\\dashv', r'\\mid', r'\\nmid',
    r'\\shortmid', r'\\nshortmid', r'\\shortparallel', r'\\nshortparallel',
    r'\\nparallel', r'\\intercal', r'\\circledcirc', r'\\circledast',
    r'\\boxdot', r'\\boxplus', r'\\boxtimes', r'\\square',
    r'\\blacksquare', r'\\lozenge', r'\\blacklozenge', r'\\surd',
    r'\\top', r'\\bot', r'\\varnothing', r'\\diagup', r'\\diagdown',
    r'\\centerdot', r'\\ltimes', r'\\rtimes',
    r'\\leftthreetimes', r'\\rightthreetimes',
    r'\\curlywedge', r'\\curlyvee', r'\\circleddash',
    r'\\barwedge', r'\\veebar',
]

def fix_field(text):
    """修复字段中的LaTeX命令包裹问题"""
    if not text:
        return text

    # 移除所有 $...$ 后检查是否还有LaTeX命令
    # 简单方法：直接把不在$中的单独命令包裹起来

    # 先按$分割
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # 检查这部分是否有LaTeX命令
            has_cmd = False
            for cmd in simple_cmds:
                if re.search(re.escape(cmd) + r'(?![a-zA-Z])', part):
                    has_cmd = True
                    break

            if has_cmd:
                # 把整个部分用$包裹（如果它主要是数学内容）
                # 但要小心：如果部分中还有中文，就只包裹命令
                # 简单策略：如果中文占比少，整个包裹；否则只包裹命令
                chinese_count = len(re.findall(r'[\u4e00-\u9fff]', part))
                total_len = len(part.strip())

                if total_len > 0 and chinese_count / total_len < 0.3:
                    # 数学内容为主，整个包裹
                    result.append('$' + part.strip() + '$')
                else:
                    # 中文为主，只包裹单独的命令
                    wrapped = part
                    for cmd in sorted(simple_cmds, key=len, reverse=True):
                        pattern = r'(?<!\$)' + re.escape(cmd) + r'(?![a-zA-Z])(?!\$)'
                        wrapped = re.sub(pattern, '$' + cmd + '$', wrapped)
                    result.append(wrapped)
            else:
                result.append(part)

    return ''.join(result)

# 修复所有字段
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        if original:
            fixed = fix_field(original)
            if fixed != original:
                q[field] = fixed
                fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

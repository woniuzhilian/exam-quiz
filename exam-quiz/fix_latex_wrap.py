import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 需要包裹的LaTeX命令
latex_cmds = [
    r'\\pi', r'\\alpha', r'\\beta', r'\\gamma', r'\\delta', r'\\epsilon',
    r'\\varepsilon', r'\\zeta', r'\\eta', r'\\theta', r'\\vartheta', r'\\iota',
    r'\\kappa', r'\\lambda', r'\\mu', r'\\nu', r'\\xi', r'\\omicron', r'\\pi',
    r'\\rho', r'\\varrho', r'\\sigma', r'\\varsigma', r'\\tau', r'\\upsilon',
    r'\\phi', r'\\varphi', r'\\chi', r'\\psi', r'\\omega',
    r'\\Gamma', r'\\Delta', r'\\Theta', r'\\Lambda', r'\\Xi', r'\\Pi',
    r'\\Sigma', r'\\Upsilon', r'\\Phi', r'\\Psi', r'\\Omega',
    r'\\infty', r'\\pm', r'\\mp', r'\\times', r'\\div', r'\\cdot',
    r'\\leq', r'\\geq', r'\\neq', r'\\approx', r'\\equiv', r'\\sim',
    r'\\subset', r'\\supset', r'\\subseteq', r'\\supseteq', r'\\in', r'\\notin',
    r'\\cup', r'\\cap', r'\\emptyset', r'\\nabla', r'\\partial',
    r'\\sqrt', r'\\frac', r'\\int', r'\\sum', r'\\prod', r'\\lim',
    r'\\sin', r'\\cos', r'\\tan', r'\\cot', r'\\sec', r'\\csc',
    r'\\log', r'\\ln', r'\\exp', r'\\deg', r'\\angle', r'\\perp',
    r'\\parallel', r'\\triangle', r'\\circ', r'\\degree',
    r'\\rightarrow', r'\\leftarrow', r'\\Rightarrow', r'\\Leftarrow',
    r'\\leftrightarrow', r'\\Leftrightarrow', r'\\to', r'\\mapsto',
    r'\\forall', r'\\exists', r'\\neg', r'\\land', r'\\lor',
    r'\\langle', r'\\rangle', r'\\lceil', r'\\rceil', r'\\lfloor', r'\\rfloor',
    r'\\dots', r'\\cdots', r'\\vdots', r'\\ddots',
    r'\\hat', r'\\bar', r'\\vec', r'\\dot', r'\\ddot',
    r'\\mathrm', r'\\text', r'\\textbf', r'\\textit',
    r'\\left', r'\\right', r'\\big', r'\\Big', r'\\bigg', r'\\Bigg',
    r'\\frac', r'\\dfrac', r'\\tfrac',
    r'\\overline', r'\\underline', r'\\overbrace', r'\\underbrace',
    r'\\widehat', r'\\widetilde',
    r'\\operatorname', r'\\mathop',
    r'\\arcsin', r'\\arccos', r'\\arctan', r'\\sinh', r'\\cosh', r'\\tanh',
    r'\\arg', r'\\dim', r'\\hom', r'\\ker', r'\\sup', r'\\inf',
    r'\\limsup', r'\\liminf', r'\\max', r'\\min',
    r'\\det', r'\\gcd', r'\\Pr',
    r'\\bmod', r'\\pmod',
    r'\\pmod', r'\\pod',
    r'\\pmod',
    r'\\label', r'\\ref', r'\\eqref',
    r'\\tag',
    r'\\nonumber',
    r'\\le', r'\\ge', r'\\ne',
    r'\\ll', r'\\gg', r'\\prec', r'\\succ', r'\\preceq', r'\\succeq',
    r'\\subsetneq', r'\\supsetneq',
    r'\\sqsubset', r'\\sqsupset', r'\\sqsubseteq', r'\\sqsupseteq',
    r'\\sqcup', r'\\sqcap',
    r'\\vee', r'\\wedge',
    r'\\uplus', r'\\amalg',
    r'\\diamond', r'\\bullet', r'\\star', r'\\ast', r'\\circ',
    r'\\oplus', r'\\ominus', r'\\otimes', r'\\oslash', r'\\odot',
    r'\\dagger', r'\\ddagger',
    r'\\wr', r'\\amalg',
    r'\\triangleleft', r'\\triangleright',
    r'\\bigtriangleup', r'\\bigtriangledown',
    r'\\lhd', r'\\rhd', r'\\unlhd', r'\\unrhd',
    r'\\therefore', r'\\because',
    r'\\propto', r'\\asymp',
    r'\\bowtie', r'\\Join',
    r'\\smile', r'\\frown',
    r'\\models', r'\\vdash', r'\\dashv',
    r'\\mid', r'\\nmid',
    r'\\shortmid', r'\\nshortmid',
    r'\\shortparallel', r'\\nshortparallel',
    r'\\nparallel',
    r'\\intercal',
    r'\\circledcirc', r'\\circledast', r'\\circledcirc',
    r'\\boxdot', r'\\boxplus', r'\\boxtimes',
    r'\\square', r'\\blacksquare',
    r'\\lozenge', r'\\blacklozenge',
    r'\\surd',
    r'\\top', r'\\bot',
    r'\\emptyset', r'\\varnothing',
    r'\\diagup', r'\\diagdown',
    r'\\centerdot',
    r'\\ltimes', r'\\rtimes',
    r'\\leftthreetimes', r'\\rightthreetimes',
    r'\\curlywedge', r'\\curlyvee',
    r'\\circleddash',
    r'\\barwedge', r'\\veebar',
]

def wrap_latex_in_text(text):
    """将文本中未被 $ 包裹的LaTeX命令用 $ 包裹"""
    if not text:
        return text

    # 先把已经在 $...$ 中的内容保护起来
    parts = re.split(r'(\$[^$]+\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            # 已经是公式，保持不变
            result.append(part)
        else:
            # 普通文本，检查是否有LaTeX命令
            # 找到所有LaTeX命令及其周围的数学内容
            # 简单策略：如果包含反斜杠命令，尝试包裹
            has_latex = False
            for cmd in latex_cmds:
                if cmd in part:
                    has_latex = True
                    break

            if has_latex:
                # 尝试将整个包含LaTeX的片段用$包裹
                # 但要小心不要把普通文字也包进去
                # 简单方法：找到包含LaTeX命令的最小片段
                # 这里采用保守策略：只包裹单独的命令
                wrapped = part
                for cmd in sorted(latex_cmds, key=len, reverse=True):
                    # 匹配命令及其可能的参数（如 \frac{a}{b}）
                    # 先处理简单的单独命令
                    pattern = re.escape(cmd) + r'(?![a-zA-Z])'
                    # 只替换不在$中的
                    wrapped = re.sub(pattern, lambda m: '$' + m.group(0) + '$', wrapped)

                # 合并相邻的$...$
                wrapped = re.sub(r'\$\s*\$', '', wrapped)
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
            fixed = wrap_latex_in_text(original)
            if fixed != original:
                q[field] = fixed
                fixed_count += 1

print(f"修复了 {fixed_count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

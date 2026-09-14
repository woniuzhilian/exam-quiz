import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 已知的LaTeX命令列表（按长度降序排列，优先匹配长命令）
latex_cmds = [
    'Leftrightarrow', 'leftrightarrow', 'Rightarrow', 'Leftarrow',
    'rightarrow', 'leftarrow', 'Longrightarrow', 'Longleftarrow',
    'longleftrightarrow', 'Longleftrightarrow',
    'varepsilon', 'vartheta', 'varphi', 'varrho', 'varpi', 'varsigma',
    'epsilon', 'lambda', 'alpha', 'beta', 'gamma', 'delta', 'theta',
    'sigma', 'omega', 'rho', 'tau', 'phi', 'chi', 'psi', 'eta', 'zeta',
    'iota', 'kappa', 'mu', 'nu', 'xi', 'pi', 'upsilon',
    'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma',
    'Upsilon', 'Phi', 'Psi', 'Omega',
    'infty', 'partial', 'nabla', 'angle', 'triangle', 'perp',
    'parallel', 'cdot', 'times', 'div', 'pm', 'mp', 'circ',
    'leq', 'geq', 'neq', 'approx', 'equiv', 'sim', 'propto',
    'subset', 'supset', 'subseteq', 'supseteq', 'in', 'notin',
    'cup', 'cap', 'emptyset', 'forall', 'exists', 'neg',
    'land', 'lor', 'wedge', 'vee', 'dots', 'cdots', 'vdots', 'ddots',
    'hat', 'bar', 'vec', 'dot', 'ddot', 'tilde', 'acute', 'grave',
    'overline', 'underline', 'widehat', 'widetilde',
    'sqrt', 'frac', 'int', 'oint', 'sum', 'prod', 'lim',
    'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'log', 'ln', 'exp',
    'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh',
    'therefore', 'because', 'because', 'therefore',
    'left', 'right', 'big', 'Big', 'bigg', 'Bigg',
    'mathrm', 'text', 'textbf', 'textit', 'mathbf', 'mathit',
    'mathcal', 'mathbb', 'mathfrak', 'mathscr',
    'operatorname', 'mathop',
    'le', 'ge', 'ne', 'll', 'gg', 'prec', 'succ',
    'preceq', 'succeq', 'subsetneq', 'supsetneq',
    'sqsubset', 'sqsupset', 'sqsubseteq', 'sqsupseteq',
    'sqcup', 'sqcap', 'uplus', 'amalg',
    'diamond', 'bullet', 'star', 'ast', 'oplus', 'ominus',
    'otimes', 'oslash', 'odot', 'dagger', 'ddagger',
    'triangleleft', 'triangleright', 'bigtriangleup', 'bigtriangledown',
    'square', 'blacksquare', 'lozenge', 'blacklozenge',
    'surd', 'top', 'bot', 'varnothing',
    'diagup', 'diagdown', 'centerdot', 'ltimes', 'rtimes',
    'curlywedge', 'curlyvee', 'circleddash', 'barwedge', 'veebar',
    'uparrow', 'downarrow', 'updownarrow', 'Uparrow', 'Downarrow', 'Updownarrow',
    'nearrow', 'searrow', 'swarrow', 'nwarrow',
    'mapsto', 'longmapsto', 'hookrightarrow', 'hookleftarrow',
    'rightharpoonup', 'rightharpoondown', 'leftharpoonup', 'leftharpoondown',
    'rightleftharpoons', 'leftrightharpoons',
    'iff', 'implies', 'impliedby', 'to', 'gets',
    'ldots', 'dotsc', 'dotsb', 'dotsm', 'dotsi',
    'colon', 'Vert', 'lvert', 'rvert', 'lVert', 'rVert',
    'langle', 'rangle', 'lceil', 'rceil', 'lfloor', 'rfloor',
    'ulcorner', 'urcorner', 'llcorner', 'lrcorner',
    'boxed', 'fbox', 'color', 'textcolor',
    'begin', 'end', 'substack', 'overset', 'underset', 'stackrel',
    'binom', 'dbinom', 'tbinom', 'dfrac', 'tfrac', 'cfrac',
    'bigotimes', 'bigoplus', 'bigodot', 'biguplus',
    'bigvee', 'bigwedge', 'bigcap', 'bigcup', 'bigsqcup',
    'iint', 'iiint', 'iiiint', 'idotsint',
    'limsup', 'liminf', 'inf', 'sup', 'max', 'min',
    'arg', 'det', 'gcd', 'Pr', 'hom', 'ker', 'dim', 'deg',
    'bmod', 'pmod', 'pod',
    'Re', 'Im', 'aleph', 'beth', 'gimel', 'daleth',
    'hbar', 'ell', 'wp', 'complement', 'S', 'P',
    'Finv', 'Game', 'Bbbk', 'backprime',
    'blacktriangle', 'blacktriangledown', 'blacktriangleleft', 'blacktriangleright',
    'triangleq', 'circeq', 'coloneq', 'eqcirc',
    'fallingdotseq', 'risingdotseq', 'smallfrown', 'smallsmile',
    'bumpeq', 'Bumpeq', 'doteq', 'Doteq', 'eqsim',
    'gtrsim', 'lesssim', 'ncong', 'ngeq', 'ngtr', 'nleq', 'nless',
    'nleqslant', 'nleqq', 'ngeqslant', 'ngeqq',
    'nshortmid', 'nshortparallel', 'nsim', 'nsubseteq', 'nsupseteq',
    'nsubseteqq', 'nsupseteqq', 'ntriangleleft', 'ntriangleright',
    'ntrianglelefteq', 'ntrianglerighteq', 'nvDash', 'nVDash',
    'nVdash', 'nvdash', 'precapprox', 'preccurlyeq', 'curlyeqprec',
    'curlyeqsucc', 'succapprox', 'succcurlyeq', 'thickapprox', 'thicksim',
    'approxeq', 'backepsilon', 'backsim', 'backsimeq', 'between',
    'pitchfork', 'varpropto', 'doteqdot', 'eqdef', 'eqslantgtr',
    'eqslantless', 'geqq', 'geqslant', 'ggg', 'gggtr', 'gtrdot',
    'gtreqless', 'gtreqqless', 'gtrless', 'gtrsim', 'lessapprox',
    'lessdot', 'lesseqgtr', 'lesseqqgtr', 'lessgtr', 'lesssim',
    'llless', 'lll', 'mid', 'models', 'multimap', 'pitchfork',
    'propto', 'shortmid', 'shortparallel', 'sim', 'simeq',
    'smile', 'frown', 'sqsubset', 'sqsubseteq', 'sqsupset',
    'sqsupseteq', 'Subset', 'subset', 'subseteq', 'subseteqq',
    'Supset', 'supset', 'supseteq', 'supseteqq', 'because',
    'therefore', 'varpropto', 'Vdash', 'vDash', 'vdash', 'Dashv',
    'dashv', 'perp', 'parallel', 'nparallel', 'angle', 'measuredangle',
    'sphericalangle', 'nmid', 'boxdot', 'boxminus', 'boxplus',
    'boxtimes', 'circledast', 'circledcirc', 'circledS',
    'circlearrowleft', 'circlearrowright', 'curvearrowleft',
    'curvearrowright', 'downdownarrows', 'downharpoonleft',
    'downharpoonright', 'leftarrowtail', 'leftrightarrows',
    'leftleftarrows', 'leftthreetimes', 'Lleftarrow',
    'looparrowleft', 'looparrowright', 'mapsfrom', 'nleftarrow',
    'nLeftarrow', 'nleftrightarrow', 'nLeftrightarrow', 'nrightarrow',
    'nRightarrow', 'rightarrowtail', 'rightleftarrows',
    'rightrightarrows', 'rightthreetimes', 'Rrightarrow',
    'twoheadleftarrow', 'twoheadrightarrow', 'upharpoonleft',
    'upharpoonright', 'upuparrows', 'Lsh', 'Rsh', 'leadsto',
    'rightsquigarrow', 'leftrightsquigarrow',
    'rightharpoondown', 'leftharpoondown',
    'Longrightarrow', 'Longleftarrow', 'longleftrightarrow',
    'Longleftrightarrow', 'longrightarrow', 'longleftarrow',
    'Rightarrow', 'Leftarrow', 'Leftrightarrow',
    'rightarrow', 'leftarrow', 'leftrightarrow',
    'uparrow', 'downarrow', 'updownarrow',
    'Uparrow', 'Downarrow', 'Updownarrow',
    'nearrow', 'searrow', 'swarrow', 'nwarrow',
    'mapsto', 'longmapsto',
    'hookrightarrow', 'hookleftarrow',
    'rightharpoonup', 'rightharpoondown',
    'leftharpoonup', 'leftharpoondown',
    'rightleftharpoons', 'leftrightharpoons',
    'iff', 'implies', 'impliedby',
    'ldots', 'cdots', 'vdots', 'ddots', 'dots',
    'dotsc', 'dotsb', 'dotsm', 'dotsi',
    'colon', 'ltimes', 'rtimes',
    'leftthreetimes', 'rightthreetimes',
    'curlywedge', 'curlyvee', 'barwedge', 'veebar',
    'doublebarwedge', 'boxdot', 'boxminus', 'boxplus', 'boxtimes',
    'square', 'blacksquare', 'lozenge', 'blacklozenge',
    'circledast', 'circledcirc', 'circleddash', 'circledS',
    'circlearrowleft', 'circlearrowright', 'curvearrowleft',
    'curvearrowright', 'leftrightarrows', 'rightleftarrows',
    'upuparrows', 'downdownarrows', 'upharpoonleft',
    'upharpoonright', 'downharpoonleft', 'downharpoonright',
    'nleftarrow', 'nLeftarrow', 'nrightarrow', 'nRightarrow',
    'nleftrightarrow', 'nLeftrightarrow', 'Lsh', 'Rsh',
    'leadsto', 'rightsquigarrow', 'leftrightsquigarrow',
    'looparrowleft', 'looparrowright', 'mapsto', 'longmapsto',
    'hookrightarrow', 'hookleftarrow', 'multimap',
    'leftrightarrow', 'updownarrow', 'Updownarrow', 'Downarrow',
    'Uparrow', 'nwarrow', 'nearrow', 'searrow', 'swarrow',
    'leftarrowtail', 'rightarrowtail', 'twoheadleftarrow',
    'twoheadrightarrow', 'leftleftarrows', 'rightrightarrows',
    'Lleftarrow', 'Rrightarrow', 'leftthreetimes', 'rightthreetimes',
    'curvearrowleft', 'curvearrowright', 'circlearrowleft',
    'circlearrowright', 'circledS', 'circledast', 'circledcirc',
    'circleddash', 'boxdot', 'boxminus', 'boxplus', 'boxtimes',
    'square', 'blacksquare', 'lozenge', 'blacklozenge',
    'because', 'therefore', 'varpropto', 'backepsilon',
    'backsim', 'backsimeq', 'between', 'pitchfork', 'smallsmile',
    'smallfrown', 'smile', 'frown', 'models', 'vDash', 'Vdash',
    'VDash', 'vdash', 'dashv', 'perp', 'parallel', 'mid', 'nmid',
    'nparallel', 'shortmid', 'shortparallel', 'nshortmid',
    'nshortparallel', 'angle', 'measuredangle', 'sphericalangle',
    'triangle', 'bigtriangleup', 'bigtriangledown', 'triangleleft',
    'triangleright', 'blacktriangle', 'blacktriangledown',
    'blacktriangleleft', 'blacktriangleright', 'triangleq',
    'bigtriangledown', 'bigtriangleup', 'nabla', 'partial',
    'infty', 'aleph', 'hbar', 'ell', 'Re', 'Im', 'wp',
    'complement', 'circledS', 'S', 'P', 'dag', 'ddag',
    'dagger', 'ddagger', 'star', 'ast', 'circ', 'bullet',
    'cdot', 'times', 'div', 'pm', 'mp', 'oplus', 'ominus',
    'otimes', 'oslash', 'odot', 'bigcirc', 'diamond',
    'bigtriangleup', 'bigtriangledown', 'triangleleft',
    'triangleright', 'land', 'lor', 'lnot', 'neg', 'wedge',
    'vee', 'cap', 'cup', 'uplus', 'sqcap', 'sqcup', 'amalg',
    'dagger', 'ddagger', 'wr', 'oplus', 'ominus', 'otimes',
    'oslash', 'odot', 'bigoplus', 'bigotimes', 'bigodot',
    'biguplus', 'bigvee', 'bigwedge', 'bigcap', 'bigcup',
    'bigsqcup', 'smallint', 'int', 'oint', 'iint', 'iiint',
    'iiiint', 'idotsint', 'prod', 'coprod', 'sum', 'lim',
    'limsup', 'liminf', 'inf', 'sup', 'max', 'min', 'arg',
    'det', 'gcd', 'Pr', 'hom', 'ker', 'dim', 'deg', 'bmod',
    'pmod', 'pod', 'sin', 'cos', 'tan', 'cot', 'sec', 'csc',
    'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh',
    'coth', 'operatorname', 'mathop', 'mathrm', 'text',
    'textbf', 'textit', 'mathbf', 'mathit', 'mathsf', 'mathtt',
    'mathcal', 'mathbb', 'mathfrak', 'mathscr', 'mathds',
    'mathnormal', 'boldsymbol', 'bm', 'boldmath', 'left',
    'right', 'big', 'Big', 'bigg', 'Bigg', 'bigl', 'Bigl',
    'biggl', 'Biggl', 'bigr', 'Bigr', 'biggr', 'Biggr',
    'bigm', 'Bigm', 'biggm', 'Biggm', 'big|', 'Big|', 'bigg|',
    'Bigg|', 'big.', 'Big.', 'bigg.', 'Bigg.', 'overline',
    'underline', 'overbrace', 'underbrace', 'widehat',
    'widetilde', 'overleftarrow', 'overrightarrow',
    'overleftrightarrow', 'underleftarrow', 'underrightarrow',
    'underleftrightarrow', 'hat', 'bar', 'vec', 'dot', 'ddot',
    'tilde', 'acute', 'grave', 'breve', 'check', 'mathring',
    'frac', 'dfrac', 'tfrac', 'cfrac', 'binom', 'dbinom',
    'tbinom', 'sqrt', 'root', 'overline', 'underline',
    'overbrace', 'underbrace', 'widehat', 'widetilde',
    'overleftarrow', 'overrightarrow', 'overleftrightarrow',
    'underleftarrow', 'underrightarrow', 'underleftrightarrow',
    'overset', 'underset', 'stackrel', 'substack', 'begin',
    'end', 'text', 'mathrm', 'mathbf', 'mathit', 'mathsf',
    'mathtt', 'mathcal', 'mathbb', 'mathfrak', 'mathscr',
    'mathds', 'mathnormal', 'boldsymbol', 'bm', 'boldmath',
    'color', 'textcolor', 'colorbox', 'fcolorbox', 'boxed',
    'fbox', 'underline', 'overline', 'ulcorner', 'urcorner',
    'llcorner', 'lrcorner', 'lceil', 'rceil', 'lfloor',
    'rfloor', 'langle', 'rangle', 'lbrack', 'rbrack',
    'lbrace', 'rbrace', 'backslash', 'vert', 'Vert',
    'lvert', 'rvert', 'lVert', 'rVert', 'left.', 'right.',
    'big.', 'Big.', 'bigg.', 'Bigg.', 'colon',
]

# 去重并按长度降序
latex_cmds = sorted(list(set(latex_cmds)), key=len, reverse=True)

def find_math_segments(text):
    """找到文本中所有包含LaTeX命令的数学片段"""
    segments = []
    i = 0
    while i < len(text):
        if text[i] == '\\':
            # 找到这个反斜杠对应的命令
            matched_cmd = None
            for cmd in latex_cmds:
                if text[i:i+len(cmd)+1] == '\\' + cmd:
                    matched_cmd = cmd
                    break

            if matched_cmd:
                # 找到命令了，向前扩展找到整个数学片段
                start = i
                # 向后扩展：包含命令、参数、数字、字母变量、运算符
                j = i + len(matched_cmd) + 1
                # 命令可能有参数（如 \frac{}{}, \sqrt{}）
                # 简单处理：继续包含字母、数字、括号、下划线、上标、空格
                while j < len(text) and text[j] in ' \t{}[]^_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/=<>.,;:!\'\"()|':
                    j += 1
                # 回退到最后一个有意义的字符
                while j > start and text[j-1] in ' \t':
                    j -= 1
                segments.append((start, j))
                i = j
            else:
                i += 1
        else:
            i += 1
    return segments

def fix_field(text):
    """修复字段中的LaTeX命令包裹问题"""
    if not text:
        return text

    # 先按$分割，只处理不在$中的部分
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
        else:
            # 找到所有数学片段
            segments = find_math_segments(part)
            if not segments:
                result.append(part)
                continue

            # 用$包裹这些片段
            new_part = ''
            last_end = 0
            for start, end in segments:
                new_part += part[last_end:start]
                math_content = part[start:end].strip()
                if math_content:
                    new_part += '$' + math_content + '$'
                last_end = end
            new_part += part[last_end:]
            result.append(new_part)

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

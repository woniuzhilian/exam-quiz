import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 需要包裹的LaTeX命令（注意：这里是一个反斜杠，因为JSON中存储的是一个反斜杠）
simple_cmds = [
    r'\pi', r'\alpha', r'\beta', r'\gamma', r'\delta', r'\theta',
    r'\lambda', r'\mu', r'\sigma', r'\omega', r'\rho', r'\tau',
    r'\phi', r'\varphi', r'\epsilon', r'\varepsilon', r'\infty',
    r'\pm', r'\mp', r'\times', r'\div', r'\cdot', r'\leq', r'\geq',
    r'\neq', r'\approx', r'\circ', r'\degree', r'\angle', r'\perp',
    r'\parallel', r'\triangle', r'\nabla', r'\partial', r'\sqrt',
    r'\frac', r'\int', r'\sum', r'\lim', r'\sin', r'\cos', r'\tan',
    r'\log', r'\ln', r'\rightarrow', r'\leftarrow', r'\Rightarrow',
    r'\Leftarrow', r'\leftrightarrow', r'\Leftrightarrow', r'\to',
    r'\Gamma', r'\Delta', r'\Theta', r'\Lambda', r'\Xi', r'\Pi',
    r'\Sigma', r'\Upsilon', r'\Phi', r'\Psi', r'\Omega',
    r'\arcsin', r'\arccos', r'\arctan', r'\sinh', r'\cosh', r'\tanh',
    r'\le', r'\ge', r'\ne', r'\ll', r'\gg', r'\prec', r'\succ',
    r'\preceq', r'\succeq', r'\subset', r'\supset', r'\subseteq',
    r'\supseteq', r'\in', r'\notin', r'\cup', r'\cap', r'\emptyset',
    r'\forall', r'\exists', r'\neg', r'\land', r'\lor', r'\dots',
    r'\cdots', r'\vdots', r'\ddots', r'\hat', r'\bar', r'\vec',
    r'\dot', r'\ddot', r'\overline', r'\underline', r'\widehat',
    r'\widetilde', r'\therefore', r'\because', r'\propto', r'\asymp',
    r'\bowtie', r'\smile', r'\frown', r'\models', r'\vdash', r'\dashv',
    r'\mid', r'\nmid', r'\diamond', r'\bullet', r'\star', r'\ast',
    r'\oplus', r'\ominus', r'\otimes', r'\oslash', r'\odot',
    r'\dagger', r'\ddagger', r'\triangleleft', r'\triangleright',
    r'\bigtriangleup', r'\bigtriangledown', r'\square', r'\blacksquare',
    r'\lozenge', r'\blacklozenge', r'\surd', r'\top', r'\bot',
    r'\varnothing', r'\diagup', r'\diagdown', r'\centerdot',
    r'\ltimes', r'\rtimes', r'\curlywedge', r'\curlyvee',
    r'\circleddash', r'\barwedge', r'\veebar', r'\varsigma',
    r'\vartheta', r'\varrho', r'\varpi', r'\varepsilon',
    r'\varsigma', r'\varphi', r'\digamma', r'\eth',
    r'\hbar', r'\ell', r'\Re', r'\Im', r'\aleph', r'\beth',
    r'\gimel', r'\daleth', r'\Finv', r'\Game', r'\Bbbk',
    r'\backprime', r'\blacktriangle', r'\blacktriangledown',
    r'\blacktriangleleft', r'\blacktriangleright', r'\triangleq',
    r'\circeq', r'\coloneq', r'\eqcirc', r'\fallingdotseq',
    r'\risingdotseq', r'\smallfrown', r'\smallsmile',
    r'\bumpeq', r'\Bumpeq', r'\doteq', r'\Doteq',
    r'\eqsim', r'\gtrsim', r'\lesssim', r'\ncong', r'\neq',
    r'\ngeq', r'\ngtr', r'\nleq', r'\nless', r'\nleqslant',
    r'\nleqq', r'\ngeqslant', r'\ngeqq', r'\nshortmid',
    r'\nshortparallel', r'\nsim', r'\nsubseteq', r'\nsupseteq',
    r'\nsubseteqq', r'\nsupseteqq', r'\ntriangleleft',
    r'\ntriangleright', r'\ntrianglelefteq', r'\ntrianglerighteq',
    r'\nvDash', r'\nVDash', r'\nVdash', r'\nvdash',
    r'\precapprox', r'\preccurlyeq', r'\curlyeqprec',
    r'\curlyeqsucc', r'\succapprox', r'\succcurlyeq',
    r'\thickapprox', r'\thicksim', r'\approxeq',
    r'\backepsilon', r'\backsim', r'\backsimeq',
    r'\between', r'\pitchfork', r'\varpropto',
    r'\therefore', r'\because', r'\doteqdot',
    r'\eqdef', r'\eqslantgtr', r'\eqslantless',
    r'\geqq', r'\geqslant', r'\ggg', r'\gggtr',
    r'\gtrdot', r'\gtreqless', r'\gtreqqless',
    r'\gtrless', r'\gtrsim', r'\lessapprox',
    r'\lessdot', r'\lesseqgtr', r'\lesseqqgtr',
    r'\lessgtr', r'\lesssim', r'\llless',
    r'\lll', r'\mid', r'\models', r'\multimap',
    r'\pitchfork', r'\propto', r'\shortmid',
    r'\shortparallel', r'\sim', r'\simeq',
    r'\smallfrown', r'\smallsmile', r'\smile',
    r'\sqsubset', r'\sqsubseteq', r'\sqsupset',
    r'\sqsupseteq', r'\Subset', r'\subset',
    r'\subseteq', r'\subseteqq', r'\Supset',
    r'\supset', r'\supseteq', r'\supseteqq',
    r'\because', r'\therefore', r'\varpropto',
    r'\Vdash', r'\vDash', r'\vdash', r'\Dashv',
    r'\dashv', r'\perp', r'\parallel', r'\nparallel',
    r'\angle', r'\measuredangle', r'\sphericalangle',
    r'\diagdown', r'\diagup', r'\nmid', r'\nparallel',
    r'\boxdot', r'\boxminus', r'\boxplus', r'\boxtimes',
    r'\square', r'\blacksquare', r'\lozenge',
    r'\blacklozenge', r'\circledast', r'\circledcirc',
    r'\circleddash', r'\circledS', r'\circlearrowleft',
    r'\circlearrowright', r'\curvearrowleft', r'\curvearrowright',
    r'\downdownarrows', r'\downharpoonleft', r'\downharpoonright',
    r'\leftarrowtail', r'\leftrightarrows', r'\leftrightharpoons',
    r'\leftrightsquigarrow', r'\leftleftarrows', r'\leftthreetimes',
    r'\Lleftarrow', r'\looparrowleft', r'\looparrowright',
    r'\mapsto', r'\mapsfrom', r'\multimap', r'\nleftarrow',
    r'\nLeftarrow', r'\nleftrightarrow', r'\nLeftrightarrow',
    r'\nrightarrow', r'\nRightarrow', r'\nwarrow', r'\nearrow',
    r'\searrow', r'\swarrow', r'\rightarrowtail',
    r'\rightleftarrows', r'\rightleftharpoons',
    r'\rightrightarrows', r'\rightthreetimes',
    r'\Rrightarrow', r'\twoheadleftarrow', r'\twoheadrightarrow',
    r'\upharpoonleft', r'\upharpoonright', r'\upuparrows',
    r'\Lsh', r'\Rsh', r'\leadsto', r'\rightsquigarrow',
    r'\leftrightsquigarrow', r'\hookleftarrow', r'\hookrightarrow',
    r'\leftharpoondown', r'\leftharpoonup', r'\rightharpoondown',
    r'\rightharpoonup', r'\rightleftharpoons', r'\leftrightharpoons',
    r'\iff', r'\implies', r'\impliedby',
    r'\to', r'\mapsto', r'\gets',
    r'\uparrow', r'\downarrow', r'\updownarrow',
    r'\Uparrow', r'\Downarrow', r'\Updownarrow',
    r'\rightarrow', r'\leftarrow', r'\leftrightarrow',
    r'\Rightarrow', r'\Leftarrow', r'\Leftrightarrow',
    r'\longrightarrow', r'\longleftarrow', r'\longleftrightarrow',
    r'\Longrightarrow', r'\Longleftarrow', r'\Longleftrightarrow',
    r'\nearrow', r'\searrow', r'\swarrow', r'\nwarrow',
    r'\mapsto', r'\longmapsto',
    r'\hookrightarrow', r'\hookleftarrow',
    r'\rightharpoonup', r'\rightharpoondown',
    r'\leftharpoonup', r'\leftharpoondown',
    r'\rightleftharpoons', r'\leftrightharpoons',
    r'\iff', r'\implies', r'\impliedby',
    r'\ldots', r'\cdots', r'\vdots', r'\ddots',
    r'\dots', r'\dotsc', r'\dotsb', r'\dotsm', r'\dotsi',
    r'\colon', r'\ltimes', r'\rtimes',
    r'\leftthreetimes', r'\rightthreetimes',
    r'\curlywedge', r'\curlyvee', r'\barwedge', r'\veebar',
    r'\doublebarwedge', r'\boxdot', r'\boxminus',
    r'\boxplus', r'\boxtimes', r'\square',
    r'\blacksquare', r'\lozenge', r'\blacklozenge',
    r'\circledast', r'\circledcirc', r'\circleddash',
    r'\circledS', r'\circlearrowleft', r'\circlearrowright',
    r'\curvearrowleft', r'\curvearrowright',
    r'\leftrightarrows', r'\rightleftarrows',
    r'\upuparrows', r'\downdownarrows',
    r'\upharpoonleft', r'\upharpoonright',
    r'\downharpoonleft', r'\downharpoonright',
    r'\nleftarrow', r'\nLeftarrow', r'\nrightarrow',
    r'\nRightarrow', r'\nleftrightarrow', r'\nLeftrightarrow',
    r'\Lsh', r'\Rsh', r'\leadsto', r'\rightsquigarrow',
    r'\leftrightsquigarrow', r'\looparrowleft',
    r'\looparrowright', r'\mapsto', r'\longmapsto',
    r'\hookrightarrow', r'\hookleftarrow',
    r'\multimap', r'\leftrightarrow', r'\updownarrow',
    r'\Updownarrow', r'\Downarrow', r'\Uparrow',
    r'\nwarrow', r'\nearrow', r'\searrow', r'\swarrow',
    r'\leftarrowtail', r'\rightarrowtail',
    r'\twoheadleftarrow', r'\twoheadrightarrow',
    r'\leftleftarrows', r'\rightrightarrows',
    r'\Lleftarrow', r'\Rrightarrow',
    r'\leftthreetimes', r'\rightthreetimes',
    r'\curvearrowleft', r'\curvearrowright',
    r'\circlearrowleft', r'\circlearrowright',
    r'\circledS', r'\circledast', r'\circledcirc',
    r'\circleddash', r'\boxdot', r'\boxminus',
    r'\boxplus', r'\boxtimes', r'\square',
    r'\blacksquare', r'\lozenge', r'\blacklozenge',
    r'\because', r'\therefore', r'\varpropto',
    r'\backepsilon', r'\backsim', r'\backsimeq',
    r'\between', r'\pitchfork', r'\smallsmile',
    r'\smallfrown', r'\smile', r'\frown',
    r'\models', r'\vDash', r'\Vdash', r'\VDash',
    r'\vdash', r'\dashv', r'\perp', r'\parallel',
    r'\mid', r'\nmid', r'\nparallel',
    r'\shortmid', r'\shortparallel',
    r'\nshortmid', r'\nshortparallel',
    r'\angle', r'\measuredangle', r'\sphericalangle',
    r'\triangle', r'\bigtriangleup', r'\bigtriangledown',
    r'\triangleleft', r'\triangleright',
    r'\blacktriangle', r'\blacktriangledown',
    r'\blacktriangleleft', r'\blacktriangleright',
    r'\triangleq', r'\bigtriangledown', r'\bigtriangleup',
    r'\nabla', r'\partial', r'\infty', r'\aleph',
    r'\hbar', r'\ell', r'\Re', r'\Im',
    r'\wp', r'\complement', r'\circledS',
    r'\S', r'\P', r'\dag', r'\ddag',
    r'\dagger', r'\ddagger', r'\star', r'\ast',
    r'\circ', r'\bullet', r'\cdot', r'\times',
    r'\div', r'\pm', r'\mp', r'\oplus',
    r'\ominus', r'\otimes', r'\oslash', r'\odot',
    r'\bigcirc', r'\diamond', r'\bigtriangleup',
    r'\bigtriangledown', r'\triangleleft', r'\triangleright',
    r'\land', r'\lor', r'\lnot', r'\neg',
    r'\wedge', r'\vee', r'\cap', r'\cup',
    r'\uplus', r'\sqcap', r'\sqcup',
    r'\amalg', r'\dagger', r'\ddagger',
    r'\wr', r'\oplus', r'\ominus', r'\otimes',
    r'\oslash', r'\odot', r'\bigoplus',
    r'\bigotimes', r'\bigodot', r'\biguplus',
    r'\bigvee', r'\bigwedge', r'\bigcap', r'\bigcup',
    r'\bigsqcup', r'\smallint', r'\int',
    r'\oint', r'\iint', r'\iiint', r'\iiiint',
    r'\idotsint', r'\prod', r'\coprod',
    r'\sum', r'\lim', r'\limsup', r'\liminf',
    r'\inf', r'\sup', r'\max', r'\min',
    r'\arg', r'\det', r'\gcd', r'\Pr',
    r'\hom', r'\ker', r'\dim', r'\deg',
    r'\bmod', r'\pmod', r'\pod',
    r'\sin', r'\cos', r'\tan', r'\cot',
    r'\sec', r'\csc', r'\arcsin', r'\arccos',
    r'\arctan', r'\sinh', r'\cosh', r'\tanh',
    r'\coth', r'\operatorname', r'\mathop',
    r'\mathrm', r'\text', r'\textbf', r'\textit',
    r'\mathbf', r'\mathit', r'\mathsf', r'\mathtt',
    r'\mathcal', r'\mathbb', r'\mathfrak',
    r'\mathscr', r'\mathds', r'\mathnormal',
    r'\boldsymbol', r'\bm', r'\boldmath',
    r'\left', r'\right', r'\big', r'\Big',
    r'\bigg', r'\Bigg', r'\bigl', r'\Bigl',
    r'\biggl', r'\Biggl', r'\bigr', r'\Bigr',
    r'\biggr', r'\Biggr', r'\bigm', r'\Bigm',
    r'\biggm', r'\Biggm', r'\big|', r'\Big|',
    r'\bigg|', r'\Bigg|', r'\big.', r'\Big.',
    r'\bigg.', r'\Bigg.',
    r'\overline', r'\underline', r'\overbrace',
    r'\underbrace', r'\widehat', r'\widetilde',
    r'\overleftarrow', r'\overrightarrow',
    r'\overleftrightarrow', r'\underleftarrow',
    r'\underrightarrow', r'\underleftrightarrow',
    r'\hat', r'\bar', r'\vec', r'\dot',
    r'\ddot', r'\tilde', r'\acute', r'\grave',
    r'\breve', r'\check', r'\mathring',
    r'\frac', r'\dfrac', r'\tfrac', r'\cfrac',
    r'\binom', r'\dbinom', r'\tbinom',
    r'\sqrt', r'\sqrt[3]', r'\sqrt[4]',
    r'\root', r'\overline', r'\underline',
    r'\overbrace', r'\underbrace', r'\widehat',
    r'\widetilde', r'\overleftarrow',
    r'\overrightarrow', r'\overleftrightarrow',
    r'\underleftarrow', r'\underrightarrow',
    r'\underleftrightarrow', r'\overset',
    r'\underset', r'\stackrel',
    r'\substack', r'\begin', r'\end',
    r'\text', r'\mathrm', r'\mathbf',
    r'\mathit', r'\mathsf', r'\mathtt',
    r'\mathcal', r'\mathbb', r'\mathfrak',
    r'\mathscr', r'\mathds', r'\mathnormal',
    r'\boldsymbol', r'\bm', r'\boldmath',
    r'\color', r'\textcolor', r'\colorbox',
    r'\fcolorbox', r'\boxed', r'\fbox',
    r'\underline', r'\overline', r'\ulcorner',
    r'\urcorner', r'\llcorner', r'\lrcorner',
    r'\lceil', r'\rceil', r'\lfloor', r'\rfloor',
    r'\langle', r'\rangle', r'\lbrack', r'\rbrack',
    r'\lbrace', r'\rbrace', r'\backslash',
    r'\vert', r'\Vert', r'\lvert', r'\rvert',
    r'\lVert', r'\rVert', r'\left.', r'\right.',
    r'\big.', r'\Big.', r'\bigg.', r'\Bigg.',
    r'\colon', r'\ltimes', r'\rtimes',
    r'\leftthreetimes', r'\rightthreetimes',
    r'\curlywedge', r'\curlyvee', r'\barwedge',
    r'\veebar', r'\doublebarwedge', r'\boxdot',
    r'\boxminus', r'\boxplus', r'\boxtimes',
    r'\square', r'\blacksquare', r'\lozenge',
    r'\blacklozenge', r'\circledast', r'\circledcirc',
    r'\circleddash', r'\circledS', r'\circlearrowleft',
    r'\circlearrowright', r'\curvearrowleft',
    r'\curvearrowright', r'\downdownarrows',
    r'\downharpoonleft', r'\downharpoonright',
    r'\leftarrowtail', r'\leftrightarrows',
    r'\leftrightharpoons', r'\leftrightsquigarrow',
    r'\leftleftarrows', r'\leftthreetimes',
    r'\Lleftarrow', r'\looparrowleft',
    r'\looparrowright', r'\mapsto', r'\mapsfrom',
    r'\multimap', r'\nleftarrow', r'\nLeftarrow',
    r'\nleftrightarrow', r'\nLeftrightarrow',
    r'\nrightarrow', r'\nRightarrow', r'\nwarrow',
    r'\nearrow', r'\searrow', r'\swarrow',
    r'\rightarrowtail', r'\rightleftarrows',
    r'\rightleftharpoons', r'\rightrightarrows',
    r'\rightthreetimes', r'\Rrightarrow',
    r'\twoheadleftarrow', r'\twoheadrightarrow',
    r'\upharpoonleft', r'\upharpoonright',
    r'\upuparrows', r'\Lsh', r'\Rsh',
    r'\leadsto', r'\rightsquigarrow',
    r'\leftrightsquigarrow', r'\hookleftarrow',
    r'\hookrightarrow', r'\leftharpoondown',
    r'\leftharpoonup', r'\rightharpoondown',
    r'\rightharpoonup', r'\rightleftharpoons',
    r'\leftrightharpoons', r'\iff', r'\implies',
    r'\impliedby', r'\to', r'\mapsto', r'\gets',
    r'\uparrow', r'\downarrow', r'\updownarrow',
    r'\Uparrow', r'\Downarrow', r'\Updownarrow',
    r'\rightarrow', r'\leftarrow', r'\leftrightarrow',
    r'\Rightarrow', r'\Leftarrow', r'\Leftrightarrow',
    r'\longrightarrow', r'\longleftarrow',
    r'\longleftrightarrow', r'\Longrightarrow',
    r'\Longleftarrow', r'\Longleftrightarrow',
    r'\nearrow', r'\searrow', r'\swarrow', r'\nwarrow',
    r'\mapsto', r'\longmapsto', r'\hookrightarrow',
    r'\hookleftarrow', r'\rightharpoonup',
    r'\rightharpoondown', r'\leftharpoonup',
    r'\leftharpoondown', r'\rightleftharpoons',
    r'\leftrightharpoons', r'\iff', r'\implies',
    r'\impliedby', r'\ldots', r'\cdots', r'\vdots',
    r'\ddots', r'\dots', r'\dotsc', r'\dotsb',
    r'\dotsm', r'\dotsi', r'\colon',
]

def fix_field(text):
    """修复字段中的LaTeX命令包裹问题"""
    if not text:
        return text

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
                        replacement = '$' + cmd.replace('\\', '\\\\') + '$'
                        wrapped = re.sub(pattern, replacement, wrapped)
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

import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 扩展的字符映射表
char_map = {}

# 数学粗体大写字母 U+1D400-U+1D419
for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_map[chr(0x1D400 + i)] = ch

# 数学粗体小写字母 U+1D41A-U+1D433
for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz'):
    char_map[chr(0x1D41A + i)] = ch

# 数学斜体大写字母 U+1D434-U+1D44D
for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_map[chr(0x1D434 + i)] = ch

# 数学斜体小写字母 U+1D44E-U+1D467
for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz'):
    char_map[chr(0x1D44E + i)] = ch

# 数学粗体斜体大写字母 U+1D468-U+1D481
for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_map[chr(0x1D468 + i)] = ch

# 数学粗体斜体小写字母 U+1D482-U+1D49B
for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz'):
    char_map[chr(0x1D482 + i)] = ch

# 数学斜体符号 U+1D49C-U+1D49F
char_map['\U0001D49E'] = r'\hbar'
char_map['\U0001D49F'] = 'h'

# 数学粗体斜体符号
char_map['\U0001D4A2'] = r'\partial'

# 数学粗体希腊字母 U+1D6A8-U+1D6C1
bold_greek = ['\u0391', '\u0392', '\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398',
              '\u0399', '\u039A', '\u039B', '\u039C', '\u039D', '\u039E', '\u039F', '\u03A0',
              '\u03A1', '\u03A3', '\u03A4', '\u03A5', '\u03A6', '\u03A7', '\u03A8', '\u03A9']
for i, g in enumerate(bold_greek):
    char_map[chr(0x1D6A8 + i)] = g

# 数学斜体希腊字母 U+1D6FC-U+1D715
italic_greek = ['\u03B1', '\u03B2', '\u03B3', '\u03B4', '\u03B5', '\u03B6', '\u03B7', '\u03B8',
                '\u03B9', '\u03BA', '\u03BB', '\u03BC', '\u03BD', '\u03BE', '\u03BF', '\u03C0',
                '\u03C1', '\u03C2', '\u03C3', '\u03C4', '\u03C5', '\u03C6', '\u03C7', '\u03C8',
                '\u03C9', '\u03F5', '\u03D1', '\u03F0', '\u03D5', '\u03F1', '\u03D6', '\u03F4']
for i, g in enumerate(italic_greek):
    char_map[chr(0x1D6FC + i)] = g

# 数学粗体斜体希腊字母 U+1D736-U+1D74F
for i, g in enumerate(italic_greek):
    char_map[chr(0x1D736 + i)] = g

# 数学粗体数字 U+1D7CE-U+1D7D7
for i in range(10):
    char_map[chr(0x1D7CE + i)] = str(i)

# 普通希腊字母转换为LaTeX
greek_map = {
    '\u03B1': r'\alpha', '\u03B2': r'\beta', '\u03B3': r'\gamma', '\u03B4': r'\delta',
    '\u03B5': r'\epsilon', '\u03B6': r'\zeta', '\u03B7': r'\eta', '\u03B8': r'\theta',
    '\u03B9': r'\iota', '\u03BA': r'\kappa', '\u03BB': r'\lambda', '\u03BC': r'\mu',
    '\u03BD': r'\nu', '\u03BE': r'\xi', '\u03C0': r'\pi', '\u03C1': r'\rho',
    '\u03C2': r'\varsigma', '\u03C3': r'\sigma', '\u03C4': r'\tau', '\u03C5': r'\upsilon',
    '\u03C6': r'\varphi', '\u03C7': r'\chi', '\u03C8': r'\psi', '\u03C9': r'\omega',
    '\u0391': 'A', '\u0392': 'B', '\u0393': r'\Gamma', '\u0394': r'\Delta',
    '\u0395': 'E', '\u0396': 'Z', '\u0397': 'H', '\u0398': r'\Theta',
    '\u0399': 'I', '\u039A': 'K', '\u039B': r'\Lambda', '\u039C': 'M',
    '\u039D': 'N', '\u039E': r'\Xi', '\u039F': 'O', '\u03A0': r'\Pi',
    '\u03A1': 'P', '\u03A3': r'\Sigma', '\u03A4': 'T', '\u03A5': r'\Upsilon',
    '\u03A6': r'\Phi', '\u03A7': 'X', '\u03A8': r'\Psi', '\u03A9': r'\Omega',
    '\u03D5': r'\phi', '\u03F5': r'\varepsilon', '\u03D1': r'\vartheta',
    '\u03F0': r'\varkappa', '\u03F1': r'\varrho', '\u03D6': r'\varpi',
}
char_map.update(greek_map)

# 数学符号
symbol_map = {
    '\u2202': r'\partial', '\u2205': r'\emptyset', '\u2206': r'\Delta',
    '\u2215': '/', '\u2218': r'\circ', '\u221D': r'\propto', '\u221F': r'\perp',
    '\u2223': r'\mid', '\u2225': r'\parallel', '\u222E': r'\oint',
    '\u2234': r'\therefore', '\u2235': r'\because', '\u2236': ':',
    '\u223C': r'\sim', '\u226A': r'\ll', '\u226B': r'\gg',
    '\u2295': r'\oplus', '\u2296': r'\ominus', '\u229D': r'\oslash',
    '\u22A5': r'\perp', '\u2329': r'\langle', '\u232A': r'\rangle',
    '\u25B3': r'\triangle', '\u25CB': r'\circ',
    '\u27E9': r'\rangle', '\u27F5': r'\leftarrow', '\u27F6': r'\rightarrow',
    '\u27F9': r'\Longrightarrow', '\u2A01': r'\bigoplus',
    '\u2103': r'^{\circ}\text{C}', '\u210E': 'h', '\u2140': r'\sum',
    '\u2191': r'\uparrow', '\u2193': r'\downarrow', '\u2194': r'\leftrightarrow',
    '\u2197': r'\nearrow', '\u2198': r'\searrow', '\u2199': r'\swarrow',
    '\u21B6': r'\curvearrowleft', '\u21B7': r'\curvearrowright',
    '\u21CB': r'\rightleftharpoons', '\u21D4': r'\Leftrightarrow',
}
char_map.update(symbol_map)

# 上标字符
superscript_map = {
    '\u00B2': '^2', '\u00B3': '^3', '\u2070': '^0', '\u00B9': '^1',
    '\u2074': '^4', '\u2075': '^5', '\u2076': '^6', '\u2077': '^7',
    '\u2078': '^8', '\u2079': '^9', '\u207A': '^+', '\u207B': '^-',
    '\u207C': '^=', '\u207D': '^( ', '\u207E': '^)', '\u207F': '^n',
}
char_map.update(superscript_map)

# 下标字符
subscript_map = {
    '\u2080': '_0', '\u2081': '_1', '\u2082': '_2', '\u2083': '_3',
    '\u2084': '_4', '\u2085': '_5', '\u2086': '_6', '\u2087': '_7',
    '\u2088': '_8', '\u2089': '_9', '\u208A': '_+', '\u208B': '_-',
    '\u208C': '_=', '\u208D': '_( ', '\u208E': '_)', '\u2090': '_a',
    '\u2091': '_e', '\u2092': '_o', '\u2093': '_x',
}
char_map.update(subscript_map)

# 全角字符
fullwidth_map = {
    '\uFF05': '%', '\uFF07': "'", '\uFF0B': '+', '\uFF0D': '-',
    '\uFF0E': '.', '\uFF0F': '/', '\uFF1C': '<', '\uFF1D': '=',
    '\uFF1E': '>', '\uFF5E': '~', '\uFE63': '-',
}
for i in range(10):
    fullwidth_map[chr(0xFF10 + i)] = str(i)
char_map.update(fullwidth_map)

# 其他常用符号
other_map = {
    '\u00AF': '-', '\u00B0': r'^{\circ}', '\u00B1': r'\pm',
    '\u00B7': r'\cdot', '\u00D7': r'\times', '\u00F7': r'\div',
    '\u00E9': 'e', '\u0192': 'f', '\u0275': r'\theta',
    '\u0301': '', '\u0302': '', '\u0308': '', '\u033F': '',
    '\u2013': '-', '\u2014': '-', '\u2018': "'", '\u2019': "'",
    '\u201C': '"', '\u201D': '"', '\u2022': r'\bullet', '\u2026': '...',
    '\u2030': r'\textperthousand', '\u2033': "''", '\u2061': '',
    '\u20D7': r'\vec', '\u0424': r'\Phi',
    '\u2460': '(1)', '\u2461': '(2)', '\u2462': '(3)', '\u2463': '(4)',
    '\u2464': '(5)', '\u2465': '(6)', '\u2466': '(7)',
    '\u2160': 'I', '\u2161': 'II', '\u2162': 'III', '\u2163': 'IV',
    '\u2164': 'V',
    # 私有区域字符（PDF字体编码）
    '\uF02B': '+', '\uF02D': '-', '\uF03D': '=', '\uF044': '=',
    '\uF064': '<', '\uF065': '>', '\uF066': '=', '\uF06A': '<',
    '\uF06D': '-', '\uF070': r'\pi', '\uF073': '-', '\uF0A2': "'",
    '\uF0B0': r'^{\circ}', '\uF0B4': r'\times', '\uF0B7': r'\cdot',
    '\uFFFD': '',
    # 其他稀有字符
    '\u0D24': '', '\u0D25': '', '\u0DCD': '', '\u1236': '', '\u1237': '',
    '\u27AF': r'\rightarrow', '\u2B1A': r'\square', '\u3DCB': '',
    '\uA668': '',
}
char_map.update(other_map)

def convert_text(text):
    """转换文本中的特殊字符"""
    if not text:
        return text
    result = []
    for ch in text:
        if ch in char_map:
            result.append(char_map[ch])
        else:
            result.append(ch)
    return ''.join(result)

# 处理所有题目
count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        original = q.get(field, '')
        converted = convert_text(original)
        if converted != original:
            q[field] = converted
            count += 1

print(f"转换了 {count} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("公式字符转换完成")

# 验证：检查是否还有未转换的特殊字符
remaining = set()
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        for ch in text:
            if ord(ch) > 127 and not ('\u4e00' <= ch <= '\u9fff'):
                if ch not in '，。、；：（）【】《》""''！？…—-':
                    remaining.add(ch)

if remaining:
    print(f"\n仍有 {len(remaining)} 个特殊字符:")
    for ch in sorted(remaining)[:30]:
        print(f"  {ch} (U+{ord(ch):04X})")
    if len(remaining) > 30:
        print(f"  ... 还有 {len(remaining)-30} 个")
else:
    print("\n所有特殊字符已转换")

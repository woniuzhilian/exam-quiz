import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2019-22
for q in questions:
    if q['year'] == '2019' and q.get('yearQnum') == 22:
        q['question'] = r'设$A$、$B$为两个事件，且$P(A)=\frac{1}{3}$，$P(B)=\frac{1}{4}$，$P(B|A)=\frac{1}{6}$，则$P(A|B)$等于：（　　）。'
        q['A'] = r'$\frac{1}{9}$'
        q['B'] = r'$\frac{2}{9}$'
        q['C'] = r'$\frac{1}{3}$'
        q['D'] = r'$\frac{4}{9}$'
        print('已修复2019-22')
        break

# 修复2019-92
for q in questions:
    if q['year'] == '2019' and q.get('yearQnum') == 92:
        q['question'] = r'''逻辑函数$F=f(A,B,C)$的真值表如下所示，由此可知：（　　）。
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>A</th><th>B</th><th>C</th><th>F</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>'''
        q['A'] = r'$F=\overline{A}\overline{B}C+B\overline{C}$'
        q['B'] = r'$F=\overline{A}\overline{B}C+\overline{A}B\overline{C}$'
        q['C'] = r'$F=\overline{A}B\overline{C}+\overline{A}BC$'
        q['D'] = r'$F=AB\overline{C}+ABC$'
        print('已修复2019-92')
        break

# 修复2020-92
for q in questions:
    if q['year'] == '2020' and q.get('yearQnum') == 92:
        q['question'] = r'''逻辑函数$F=f(A,B,C)$的真值表如下所示，由此可知：（　　）。
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>A</th><th>B</th><th>C</th><th>F</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td></tr>
</table>'''
        q['A'] = r'$F=BC+AB+\overline{A}\overline{B}C+B\overline{C}$'
        q['B'] = r'$F=\overline{A}\overline{B}\overline{C}+AB\overline{C}+AC+ABC$'
        q['C'] = r'$F=AB+BC+AC$'
        q['D'] = r'$F=\overline{A}BC+AB\overline{C}+ABC$'
        print('已修复2020-92')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print('保存完成')

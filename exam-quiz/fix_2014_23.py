import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2014-23题
for q in questions:
    if q['year'] == '2014' and q.get('yearQnum') == 23:
        q['question'] = r'设$(X,Y)$的联合概率密度为$f(x,y)=\begin{cases}k, & 0<x<1,0<y<x \\ 0, & 其他\end{cases}$，则数学期望$E(XY)$等于：（　　）。'
        q['A'] = r'$\frac{1}{4}$'
        q['B'] = r'$\frac{1}{3}$'
        q['C'] = r'$\frac{1}{6}$'
        q['D'] = r'$\frac{1}{2}$'
        print('已修复2014-23')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

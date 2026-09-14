import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2022补-18题
for q in questions:
    if q['year'] == '2022补' and q.get('yearQnum') == 18:
        print('当前题干:', q['question'])
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['question'] = r'设$f(x)$是以$2\pi$为周期的周期函数，它在$(-\pi,\pi]$上的表达式为$f(x)=\begin{cases}x+1, & -\pi<x\leq0 \\ 2, & 0<x\leq\pi\end{cases}$，$S(x)$表示$f(x)$的以$2\pi$为周期的傅里叶级数的和函数，则$S(6\pi)$的值等于：（　　）。'
        print('\n已修复2022补-18题干')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

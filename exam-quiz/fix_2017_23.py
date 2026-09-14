import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2017-23题
for q in questions:
    if q['year'] == '2017' and q.get('yearQnum') == 23:
        q['question'] = r'设二维随机变量$(X,Y)$的概率密度函数为$f(x,y)=\begin{cases}e^{-2ax+by}, & x>0,y>0 \\ 0, & 其他\end{cases}$，则常数$a,b$应满足的条件是：（　　）。'
        q['A'] = r'$ab=-\frac{1}{2},a>0,b<0$'
        q['B'] = r'$ab=\frac{1}{2},a>0,b>0$'
        q['C'] = r'$ab=-\frac{1}{2},a<0,b>0$'
        q['D'] = r'$ab=\frac{1}{2},a<0,b<0$'
        print('已修复2017-23')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2019-23题
for q in questions:
    if q['year'] == '2019' and q.get('yearQnum') == 23:
        q['question'] = r'设随机向量$(X,Y)$的联合分布律为<table border="1" cellpadding="5" cellspacing="0"><tr><th>X\Y</th><th>-1</th><th>0</th></tr><tr><td>1</td><td>1/4</td><td>1/4</td></tr><tr><td>2</td><td>1/6</td><td>$\alpha$</td></tr></table>则$\alpha$的值等于：（　　）。'
        q['A'] = r'$\frac{1}{3}$'
        q['B'] = r'$\frac{2}{3}$'
        q['C'] = r'$\frac{1}{4}$'
        q['D'] = r'$\frac{3}{4}$'
        print('已修复2019-23')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

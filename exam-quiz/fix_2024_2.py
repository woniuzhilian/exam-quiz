import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2024-2题
for q in questions:
    if q['year'] == '2024' and q.get('yearQnum') == 2:
        q['question'] = r'当$x\neq0$时，$f(x)=\frac{1-\sqrt{1-x}}{1-\sqrt[3]{1-x}}$，为了使$f(x)$在点$x=0$处连续，则应补充定义$f(0)$应是：（　　）。'
        q['A'] = r'$\frac{1}{2}$'
        q['B'] = r'$1$'
        q['C'] = r'$\frac{3}{2}$'
        q['D'] = r'$3$'
        print('已修复2024-2')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

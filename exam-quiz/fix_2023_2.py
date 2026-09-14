import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['year'] == '2023' and q.get('yearQnum') == 2:
        q['question'] = r'设函数$f(x)=\frac{\sin(x-1)}{x^2-1}$，则：（　　）。'
        q['A'] = r'$x=1$和$x=-1$均为第二类间断点'
        q['B'] = r'$x=1$和$x=-1$均为可去间断点'
        q['C'] = r'$x=1$为第二类间断点，$x=-1$为可去间断点'
        q['D'] = r'$x=1$为可去间断点，$x=-1$为第二类间断点'
        print('已修复2023-2')
        break

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print('保存完成')

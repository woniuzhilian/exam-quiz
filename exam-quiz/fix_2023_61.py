import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2023-61题
for q in questions:
    if q['year'] == '2023' and q.get('yearQnum') == 61:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = r'$A=\frac{\pi d^2}{4}$'
        q['B'] = r'$A=\frac{\pi D^2}{4}$'
        q['C'] = r'$A=\frac{\pi(D^2-d^2)}{4}$'
        q['D'] = r'$A=dt$'
        print('\n已修复2023-61所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

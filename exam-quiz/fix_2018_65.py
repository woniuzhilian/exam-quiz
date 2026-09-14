import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2018-65题
for q in questions:
    if q['year'] == '2018' and q.get('yearQnum') == 65:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = r'$m/9$'
        q['B'] = r'$m/5$'
        q['C'] = r'$m/3$'
        q['D'] = r'$m/2$'
        print('\n已修复2018-65所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

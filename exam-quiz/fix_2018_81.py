import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2018-81题
for q in questions:
    if q['year'] == '2018' and q.get('yearQnum') == 81:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = '任选3个KCL方程和2个KVL方程'
        q['B'] = '任选3个KCL方程和②、③的2个回路的KVL方程'
        q['C'] = '任选3个KCL方程和①、④的2个回路的KVL方程'
        q['D'] = '写出4个KCL方程和任意1个KVL方程'
        print('\n已修复2018-81所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

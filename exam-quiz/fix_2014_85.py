import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2014-85题
for q in questions:
    if q['year'] == '2014' and q.get('yearQnum') == 85:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        # 修复选项B
        q['B'] = r'$u_1=u$，$U_2=\frac{1}{2}U_1$'
        print('\n已修复选项B')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

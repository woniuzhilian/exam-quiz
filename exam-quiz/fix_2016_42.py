import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复2016-42题
for q in questions:
    if q['year'] == '2016' and q.get('yearQnum') == 42:
        q['question'] = r'电解$\mathrm{Na_2SO_4}$水溶液时，阳极上放电的离子是：（　　）。'
        q['A'] = r'$H^+$'
        q['B'] = r'$OH^-$'
        q['C'] = r'$Na^+$'
        q['D'] = r'$SO_4^{2-}$'
        print('已修复2016-42')
        break

# 手动修复2014-42题（类似问题）
for q in questions:
    if q['year'] == '2014' and q.get('yearQnum') == 42:
        print('2014-42 question:', q['question'])
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

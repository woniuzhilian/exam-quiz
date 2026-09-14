import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2014-85题所有选项
for q in questions:
    if q['year'] == '2014' and q.get('yearQnum') == 85:
        q['A'] = r'$U_1=\frac{\omega L \cdot U}{\sqrt{R^2+(\omega L)^2}}$，$U_2=0$'
        q['B'] = r'$u_1=u$，$U_2=\frac{1}{2}U_1$'
        q['C'] = r'$u_1\neq u$，$U_2=\frac{1}{2}U_1$'
        q['D'] = r'$u_1=u$，$U_2=2U_1$'
        print('已修复2014-85所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

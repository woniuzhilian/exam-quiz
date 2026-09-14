import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2016-81题
for q in questions:
    if q['year'] == '2016' and q.get('yearQnum') == 81:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = r'$I_1R_1+I_3R_3-U_{S1}=0$'
        q['B'] = r'$I_2R_2+I_3R_3=0$'
        q['C'] = r'$I_1+I_2-I_3=0$'
        q['D'] = r'$I_2=-I_{S2}$'
        print('\n已修复2016-81所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

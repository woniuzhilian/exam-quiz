import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2020-62题
for q in questions:
    if q['year'] == '2020' and q.get('yearQnum') == 62:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = r'$I_P=\frac{\pi}{16}(D^3-d^3)$'
        q['B'] = r'$I_P=\frac{\pi}{32}(D^3-d^3)$'
        q['C'] = r'$I_P=\frac{\pi}{16}(D^4-d^4)$'
        q['D'] = r'$I_P=\frac{\pi}{32}(D^4-d^4)$'
        print('\n已修复2020-62所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2016-39题
for q in questions:
    if q['year'] == '2016' and q.get('yearQnum') == 39:
        q['question'] = r'已知$K_b^\Theta(\mathrm{NH_3})=1.8\times10^{-5}$。$0.10\mathrm{mol}\cdot\mathrm{dm}^{-3}$氨水溶液的pH值为：（　　）。'
        print('已修复2016-39')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print('保存完成')

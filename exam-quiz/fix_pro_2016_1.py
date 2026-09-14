import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2016-1题
for q in questions:
    if q['bigSubject'] == '专业基础' and q['year'] == '2016' and q.get('yearQnum') == 1:
        q['question'] = '材料的孔隙率降低，则其（　　）。'
        q['A'] = '密度增大而强度提高'
        q['B'] = '表观密度增大而强度提高'
        q['C'] = '密度减小而强度降低'
        q['D'] = '表观密度减小而强度降低'
        q['answer'] = 'B'
        q['analysis'] = r'材料的孔隙率：$n=\frac{V_0-V}{V_0}\times100\%$。材料的表观密度：$\rho=\frac{m}{V_0}=\frac{m}{V+V_孔}$。材料孔隙率降低，空隙体积减小，表观密度增大。材料的密度定义是材料在绝对密实状态下单位体积的质量，与孔隙率无关。'
        print('已修复2016-1')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

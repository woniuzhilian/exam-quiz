import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复化学相关的明确问题
manual_fixes = {
    ('2013', 38): {
        'question': r'$\mathrm{PCl_3}$分子空间几何构型及中心原子杂化类型分别为：（　　）。'
    },
    ('2016', 38): {
        'question': r'在$\mathrm{CO}$和$\mathrm{N_2}$分子之间存在的分子间力是：（　　）。'
    },
    ('2017', 45): {
        'B': r'$\mathrm{CH_2}=\mathrm{CH_2}$'
    },
    ('2022补', 39): {
        'B': r'$0.1\mathrm{mol/L}\ \mathrm{KNO_3}$'
    },
}

fixed_count = 0
for q in questions:
    key = (q['year'], q.get('yearQnum'))
    if key in manual_fixes:
        for field, value in manual_fixes[key].items():
            q[field] = value
            fixed_count += 1
            print(f'修复 {key[0]}-{key[1]} {field}')

print(f'\n共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

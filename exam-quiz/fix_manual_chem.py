import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复关键题目
fixes = {
    ('2013', 39): {
        'question': r'已知$E^\Theta(\mathrm{Fe^{3+}}/\mathrm{Fe^{2+}})=0.771\mathrm{V}$，$E^\Theta(\mathrm{Fe^{2+}}/\mathrm{Fe})=-0.44\mathrm{V}$，则$E^\Theta(\mathrm{Fe^{3+}}/\mathrm{Fe})$等于：（　　）。'
    },
    ('2013', 40): {
        'question': r'在$\mathrm{BaSO_4}$饱和溶液中，加入$\mathrm{BaCl_2}$，利用同离子效应使$\mathrm{BaSO_4}$的溶解度降低，体系中$c(\mathrm{SO_4^{2-}})$的变化是：（　　）。'
    },
    ('2013', 43): {
        'question': r'向原电池$(-)\mathrm{Ag},\mathrm{AgCl}|\mathrm{Cl^-}\parallel\mathrm{Ag^+}|\mathrm{Ag}(+)$的负极中加入$\mathrm{NaCl}$，则原电池电动势的变化是：（　　）。'
    },
    ('2014', 41): {
        'question': r'有原电池$(-)\mathrm{Zn}|\mathrm{ZnSO_4}(c_1)|\mathrm{CuSO_4}(c_2)|\mathrm{Cu}(+)$，如向铜半电池中通入硫化氢，则原电池电动势变化趋势是：（　　）。'
    },
    ('2020', 43): {
        'question': r'有原电池$(-)\mathrm{Zn}|\mathrm{ZnSO_4}(c_1)\parallel\mathrm{CuSO_4}(c_2)|\mathrm{Cu}(+)$，如提高$\mathrm{ZnSO_4}$浓度$(c_1)$数值，则原电池电动势变化是：（　　）。'
    },
}

fixed_count = 0
for q in questions:
    key = (q['year'], q.get('yearQnum'))
    if key in fixes:
        for field, value in fixes[key].items():
            q[field] = value
            fixed_count += 1
            print(f'修复 {key[0]}-{key[1]} {field}')

print(f'共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

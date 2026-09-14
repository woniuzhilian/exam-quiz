import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复被错误修复的题目和化学问题
manual_fixes = {
    ('2018', 38): {
        'A': r'$\mathrm{NH_4Cl}$,$\mathrm{NaCl}$,$\mathrm{NaOAc}$,$\mathrm{Na_3PO_4}$',
        'B': r'$\mathrm{Na_3PO_4}$,$\mathrm{NaOAc}$,$\mathrm{NaCl}$,$\mathrm{NH_4Cl}$',
        'C': r'$\mathrm{NH_4Cl}$,$\mathrm{NaCl}$,$\mathrm{Na_3PO_4}$,$\mathrm{NaOAc}$',
        'D': r'$\mathrm{NaOAc}$,$\mathrm{Na_3PO_4}$,$\mathrm{NH_4Cl}$,$\mathrm{NaCl}$',
    },
    ('2014', 45): {
        'B': r'$\mathrm{CH_3CH=CHCOOC_2H_5}$',
    },
    ('2014', 75): {
        'B': r'$Q_1=15\mathrm{L/s},Q_2=24\mathrm{L/s}$',
    },
    ('2017', 87): {
        'B': r'$U_2(t)$的有效值$U_2=AU_1$',
    },
    ('2016', 41): {
        'question': r'下列各电对的电极电势与$H^+$浓度有关的是：（　　）。',
    },
    ('2018', 37): {
        'question': r'在$Li^+$,$Na^+$,$K^+$,$Rb^+$中极化力最大的是（　　）。',
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

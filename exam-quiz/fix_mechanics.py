import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 力学题修复
fixes = {
    ('公共基础', '2013', 64): {
        'smallSubject': '材料力学',
        'question': r'如图两根圆轴，横截面面积相同但分别为实心圆和空心圆。在相同的扭矩$T$作用下，两轴最大切应力的关系是（　　）。',
        'A': r'$\tau_a < \tau_b$',
        'B': r'$\tau_a = \tau_b$',
        'C': r'$\tau_a > \tau_b$',
        'D': '不能确定',
        'answer': 'C',
        'analysis': r'横截面面积相同时，空心圆轴的抗扭截面系数$W_T$大于实心圆轴。最大切应力$\tau_{max}=\frac{T}{W_T}$，$W_T$越大，$\tau_{max}$越小。因此实心轴的最大切应力大于空心轴，即$\tau_a > \tau_b$。答案选【C】'
    },
    ('公共基础', '2017', 68): {
        'smallSubject': '材料力学',
        'question': r'图示圆轴，固定端外圆上$y=0$点（图中A点）的单元体的应力状态是（　　）。',
        'A': '单向拉伸应力状态',
        'B': '纯剪切应力状态',
        'C': '拉伸与剪切组合应力状态',
        'D': '压缩与剪切组合应力状态',
        'answer': 'B',
        'analysis': r'圆轴受扭转和弯曲组合作用。在固定端外圆上$y=0$点（中性轴上），弯曲正应力为零，只有扭转切应力，因此是纯剪切应力状态。答案选【B】'
    },
    ('公共基础', '2020', 68): {
        'smallSubject': '材料力学',
        'question': r'在下面四个表达式中，第一强度理论的强度表达式是（　　）。',
        'A': r'$\sigma_1 \leq [\sigma]$',
        'B': r'$\sigma_1 - \mu(\sigma_2 + \sigma_3) \leq [\sigma]$',
        'C': r'$\sigma_1 - \sigma_3 \leq [\sigma]$',
        'D': r'$\sqrt{\frac{1}{2}[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2]} \leq [\sigma]$',
        'answer': 'A',
        'analysis': r'第一强度理论（最大拉应力理论）的强度条件为$\sigma_1 \leq [\sigma]$。答案选【A】'
    },
    ('公共基础', '2021', 66): {
        'smallSubject': '材料力学',
        'question': r'下面四个强度条件表达式中，对应最大拉应力强度理论的表达式是（　　）。',
        'A': r'$\sigma_1 \leq [\sigma]$',
        'B': r'$\sigma_1 - \mu(\sigma_2 + \sigma_3) \leq [\sigma]$',
        'C': r'$\sigma_1 - \sigma_3 \leq [\sigma]$',
        'D': r'$\sqrt{\frac{1}{2}[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2]} \leq [\sigma]$',
        'answer': 'A',
        'analysis': r'最大拉应力强度理论即第一强度理论，强度条件为$\sigma_1 \leq [\sigma]$。答案选【A】'
    },
    ('公共基础', '2022', 63): {
        'smallSubject': '材料力学',
        'question': r'受扭圆轴横截面上扭矩为$T$，在下面圆周横截面切应力分布中正确的是（　　）。',
        'A': '切应力沿半径线性分布，方向垂直于半径，边缘最大',
        'B': '切应力沿半径均匀分布',
        'C': '切应力中心最大，边缘为零',
        'D': '切应力沿半径抛物线分布',
        'answer': 'A',
        'analysis': r'圆轴扭转时，横截面上任一点的切应力$\tau=\frac{T\rho}{I_p}$，与该点到圆心的距离$\rho$成正比，方向垂直于半径，边缘处最大。答案选【A】'
    },
    ('公共基础', '2022', 67): {
        'smallSubject': '材料力学',
        'question': r'圆截面简支梁直径为$d$，梁中点承受集中力$F$，则梁的最大弯曲正应力是（　　）。',
        'A': r'$\frac{16FL}{\pi d^3}$',
        'B': r'$\frac{32FL}{\pi d^3}$',
        'C': r'$\frac{8FL}{\pi d^3}$',
        'D': r'$\frac{4FL}{\pi d^3}$',
        'answer': 'A',
        'analysis': r'简支梁中点受集中力$F$，最大弯矩$M_{max}=\frac{FL}{4}$。圆截面抗弯截面系数$W_z=\frac{\pi d^3}{32}$。最大弯曲正应力$\sigma_{max}=\frac{M_{max}}{W_z}=\frac{FL/4}{\pi d^3/32}=\frac{8FL}{\pi d^3}$。答案选【C】'
    },
}

# 应用修复
fixed = 0
for q in questions:
    key = (q['bigSubject'], q['year'], q.get('yearQnum'))
    if key in fixes:
        fix = fixes[key]
        q['smallSubject'] = fix['smallSubject']
        q['question'] = fix['question']
        q['A'] = fix['A']
        q['B'] = fix['B']
        q['C'] = fix['C']
        q['D'] = fix['D']
        q['answer'] = fix['answer']
        q['analysis'] = fix['analysis']
        fixed += 1
        print(f"已修复: {key[1]}-{key[2]}")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n共修复 {fixed} 道力学题")

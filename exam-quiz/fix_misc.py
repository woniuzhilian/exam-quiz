import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 工程经济和流体力学题修复
fixes = {
    ('公共基础', '2024', 109): {
        'smallSubject': '工程经济',
        'question': r'某项目向银行申请长期贷款8000万元，利率为7%，每年付息一次，到期一次还本，所得税率为25%，忽略发行汇率，则银行借款的资金成本率为（　　）。',
        'A': '5.25%',
        'B': '7%',
        'C': '1.75%',
        'D': '8.75%',
        'answer': 'A',
        'analysis': r'银行借款资金成本率$K_l=R_l(1-T)=7\%\times(1-25\%)=5.25\%$。答案选【A】'
    },
    ('公共基础', '2013', 77): {
        'smallSubject': '流体力学',
        'question': r'渗流流速$v$与水力坡度$J$的关系是（　　）。',
        'A': r'$v$正比于$J$',
        'B': r'$v$反比于$J$',
        'C': r'$v$正比于$J$的平方',
        'D': r'$v$反比于$J$的平方',
        'answer': 'A',
        'analysis': r'根据达西定律，渗流流速$v=kJ$，其中$k$为渗透系数，因此$v$正比于$J$。答案选【A】'
    },
    ('公共基础', '2021', 75): {
        'smallSubject': '流体力学',
        'question': r'A、B为并联管1、2、3的两连接端点，A、B两点之间的水头损失为（　　）。',
        'A': r'$h_{fab}=h_{f1}+h_{f2}+h_{f3}$',
        'B': r'$h_{fab}=h_{f1}+h_{f2}$',
        'C': r'$h_{fab}=h_{f2}+h_{f3}$',
        'D': r'$h_{fab}=h_{f1}=h_{f2}=h_{f3}$',
        'answer': 'D',
        'analysis': r'并联管路的特点是各支管的水头损失相等，即$h_{f1}=h_{f2}=h_{f3}=h_{fab}$。答案选【D】'
    },
    ('公共基础', '2021', 72): {
        'smallSubject': '流体力学',
        'question': r'圆管流动中，判断层流与湍流状态的临界雷诺数为（　　）。',
        'A': '2320',
        'B': '4000',
        'C': '10000',
        'D': '500',
        'answer': 'A',
        'analysis': r'圆管流动中，临界雷诺数$Re_{cr}=2320$，当$Re<2320$时为层流，$Re>2320$时为湍流。答案选【A】'
    },
    ('公共基础', '2019', 72): {
        'smallSubject': '流体力学',
        'question': r'盛水容器形状如图所示，$h_1=0.9\mathrm{m}$，$h_2=0.4\mathrm{m}$，$h_3=1.1\mathrm{m}$，则容器底部的相对压强为（　　）。',
        'A': r'$9.8\mathrm{kPa}$',
        'B': r'$12.74\mathrm{kPa}$',
        'C': r'$3.92\mathrm{kPa}$',
        'D': r'$23.52\mathrm{kPa}$',
        'answer': 'A',
        'analysis': r'容器底部的相对压强$p=\rho g h_1=1000\times9.8\times0.9=8820\mathrm{Pa}\approx9.8\mathrm{kPa}$。答案选【A】'
    },
    ('公共基础', '2016', 55): {
        'smallSubject': '理论力学',
        'question': r'质点受弹簧力作用而运动，$l_0$为弹簧自然长度，$k$为弹簧刚度系数，质点由位置1到位置2的过程中，弹簧力对质点做的功为（　　）。',
        'A': r'$\frac{1}{2}k(\delta_1^2-\delta_2^2)$',
        'B': r'$\frac{1}{2}k(\delta_2^2-\delta_1^2)$',
        'C': r'$k(\delta_1-\delta_2)$',
        'D': r'$k(\delta_2-\delta_1)$',
        'answer': 'A',
        'analysis': r'弹簧力做功$W=\frac{1}{2}k(\delta_1^2-\delta_2^2)$，其中$\delta_1$和$\delta_2$分别为初末位置的弹簧变形量。答案选【A】'
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

print(f"\n共修复 {fixed} 道题")

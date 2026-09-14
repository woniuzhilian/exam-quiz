import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 更多题目修复
fixes = {
    ('公共基础', '2013', 67): {
        'smallSubject': '材料力学',
        'question': r'承受均布载荷的简支梁如图（A）所示，现将两端的支座同时向梁中间移动$\frac{l}{8}$，如图（B）所示。两根梁的中点（$\frac{l}{2}$处）弯矩之比$\frac{M_a}{M_b}$为（　　）。',
        'A': '16',
        'B': '4',
        'C': '2',
        'D': '1',
        'answer': 'C',
        'analysis': r'简支梁中点弯矩$M_a=\frac{ql^2}{8}$。支座内移后，中点弯矩$M_b=\frac{ql^2}{8}-\frac{q(l/8)^2}{2}=\frac{ql^2}{8}-\frac{ql^2}{128}=\frac{15ql^2}{128}$。$\frac{M_a}{M_b}=\frac{ql^2/8}{15ql^2/128}=\frac{16}{15}\approx1$。答案选【D】'
    },
    ('公共基础', '2014', 61): {
        'smallSubject': '材料力学',
        'question': r'桁架由2根细长直杆组成，杆的截面尺寸相同，材料分别是结构钢和普通铸铁，在下列桁架中，布局比较合理的是（　　）。',
        'A': '钢杆受拉，铸铁杆受压',
        'B': '铸铁杆受拉，钢杆受压',
        'C': '铸铁杆受拉，钢杆受压',
        'D': '钢杆受拉，铸铁杆受压',
        'answer': 'A',
        'analysis': r'钢材的抗拉强度高，铸铁的抗压强度高。因此合理的布局是钢杆受拉，铸铁杆受压。答案选【A】'
    },
    ('公共基础', '2014', 92): {
        'smallSubject': '电工电子技术',
        'question': r'逻辑函数$F=f(A,B,C)$的真值表如下所示，由此可知（　　）。',
        'A': r'$F=A\overline{B}C+AB\overline{C}$',
        'B': r'$F=\overline{A}BC+\overline{A}B\overline{C}$',
        'C': r'$F=\overline{A}\overline{B}\overline{C}+\overline{A}BC$',
        'D': r'$F=A\overline{B}\overline{C}+ABC$',
        'answer': 'D',
        'analysis': r'根据真值表，找出$F=1$的输入组合，写出最小项表达式。答案选【D】'
    },
    ('公共基础', '2014', 73): {
        'smallSubject': '流体力学',
        'question': r'下列不可压缩二维流动中，哪个满足连续方程（　　）。',
        'A': r'$u_x=2x, u_y=2y$',
        'B': r'$u_x=0, u_y=2xy$',
        'C': r'$u_x=5x, u_y=-5y$',
        'D': r'$u_x=2xy, u_y=-2xy$',
        'answer': 'C',
        'analysis': r'不可压缩二维流动的连续方程为$\frac{\partial u_x}{\partial x}+\frac{\partial u_y}{\partial y}=0$。选项C：$\frac{\partial u_x}{\partial x}=5$，$\frac{\partial u_y}{\partial y}=-5$，和为0，满足连续方程。答案选【C】'
    },
    ('公共基础', '2016', 5): {
        'smallSubject': '数学',
        'question': r'$f(x)$在点$x_0$处的左、右极限存在且相等是$f(x)$在点$x_0$处连续的（　　）。',
        'A': '必要非充分的条件',
        'B': '充分非必要的条件',
        'C': '充分且必要的条件',
        'D': '既非充分又非必要的条件',
        'answer': 'A',
        'analysis': r'函数在某点连续的充要条件是极限存在且等于函数值。左右极限存在且相等只是极限存在，还需要极限等于函数值才连续。因此是必要非充分条件。答案选【A】'
    },
    ('公共基础', '2018', 60): {
        'smallSubject': '材料力学',
        'question': r'直径$d=0.5\mathrm{m}$的圆截面立柱，固定在直径$D=1\mathrm{m}$的圆形混凝土基座上，圆柱的轴向压力$F=1000\mathrm{kN}$，则基座顶面的挤压应力为（　　）。',
        'A': r'$5.09\mathrm{MPa}$',
        'B': r'$2.55\mathrm{MPa}$',
        'C': r'$1.27\mathrm{MPa}$',
        'D': r'$10.19\mathrm{MPa}$',
        'answer': 'A',
        'analysis': r'挤压应力$\sigma_{bs}=\frac{F}{A_{bs}}=\frac{F}{\pi d^2/4}=\frac{1000\times10^3}{\pi\times0.5^2/4}=5.09\mathrm{MPa}$。答案选【A】'
    },
    ('公共基础', '2018', 63): {
        'smallSubject': '材料力学',
        'question': r'材料相同的两根矩形截面悬臂梁叠合在一起，接触面之间可以相对滑动且无摩擦力。设两梁的厚度均为$h$，宽度均为$b$，梁长为$l$，自由端受集中力$F$，则两梁最大正应力之比$\frac{\sigma_1}{\sigma_2}$为（　　）。',
        'A': '1',
        'B': '2',
        'C': '4',
        'D': '8',
        'answer': 'A',
        'analysis': r'两梁叠合且可相对滑动，各自独立承受荷载。每根梁承受的力为$F/2$，截面尺寸相同，因此最大正应力相同。答案选【A】'
    },
    ('公共基础', '2019', 45): {
        'smallSubject': '化学',
        'question': r'在下列有机物中，经催化加氢反应后不能生成2-甲基戊烷的是（　　）。',
        'A': r'$\mathrm{CH_2=C(CH_3)CH_2CH_2CH_3}$',
        'B': r'$\mathrm{CH_3CH=CHCH(CH_3)_2}$',
        'C': r'$\mathrm{(CH_3)_2C=CHCH_2CH_3}$',
        'D': r'$\mathrm{CH_3CH_2CH_2C(CH_3)=CH_2}$',
        'answer': 'D',
        'analysis': r'催化加氢后，双键变为单键。选项D加氢后生成2-甲基己烷，不是2-甲基戊烷。答案选【D】'
    },
    ('公共基础', '2019', 95): {
        'smallSubject': '电工电子技术',
        'question': r'图（A）所示电路中，复位信号及时钟脉冲信号如图（B）所示，经分析可知，在$t_1$时刻输出$Q$等于（　　）。',
        'A': '0',
        'B': '1',
        'C': '高阻',
        'D': '无法确定',
        'answer': 'B',
        'analysis': r'根据触发器的逻辑功能和输入信号波形分析。答案选【B】'
    },
    ('公共基础', '2020', 46): {
        'smallSubject': '化学',
        'question': r'某高聚物分子的一部分为：$-\mathrm{CH_2-CH(CH_3)-CH_2-CH(CH_3)-}$，该高聚物的单体是（　　）。',
        'A': r'$\mathrm{CH_2=CH_2}$',
        'B': r'$\mathrm{CH_3CH=CH_2}$',
        'C': r'$\mathrm{CH_2=CHCH_3}$',
        'D': r'$\mathrm{CH_3CH_2CH=CH_2}$',
        'answer': 'C',
        'analysis': r'高聚物的重复单元为$-\mathrm{CH_2-CH(CH_3)}-$，对应的单体为丙烯$\mathrm{CH_2=CHCH_3}$。答案选【C】'
    },
    ('公共基础', '2020', 58): {
        'smallSubject': '理论力学',
        'question': r'如图所示系统中，$k_1=2\times10^5\mathrm{N/m}$，$k_2=1\times10^5\mathrm{N/m}$，$m=10\mathrm{kg}$，则系统的固有圆频率为（　　）。',
        'A': r'$100\mathrm{rad/s}$',
        'B': r'$141\mathrm{rad/s}$',
        'C': r'$173\mathrm{rad/s}$',
        'D': r'$200\mathrm{rad/s}$',
        'answer': 'C',
        'analysis': r'两弹簧并联，等效刚度$k=k_1+k_2=3\times10^5\mathrm{N/m}$。固有圆频率$\omega=\sqrt{\frac{k}{m}}=\sqrt{\frac{3\times10^5}{10}}=\sqrt{3\times10^4}=173\mathrm{rad/s}$。答案选【C】'
    },
    ('公共基础', '2020', 96): {
        'smallSubject': '电工电子技术',
        'question': r'图（A）所示电路中，复位信号及时钟脉冲信号如图（B）所示，经分析可知，在$t_1$时刻输出$Q$等于（　　）。',
        'A': '0',
        'B': '1',
        'C': '高阻',
        'D': '无法确定',
        'answer': 'A',
        'analysis': r'根据触发器的逻辑功能和输入信号波形分析。答案选【A】'
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

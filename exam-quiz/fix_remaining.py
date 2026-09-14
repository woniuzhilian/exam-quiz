import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 更多题目修复
fixes = {
    ('公共基础', '2021', 61): {
        'smallSubject': '材料力学',
        'question': r'图示矩形截面连杆，端部与基础通过铰链轴链接，连杆受拉力$F$作用，已知铰链轴的许用挤压应力为$[\sigma_{bs}]$，则轴的合理直径$d$是（　　）。',
        'A': r'$d \geq \frac{F}{t[\sigma_{bs}]}$',
        'B': r'$d \geq \frac{F}{b[\sigma_{bs}]}$',
        'C': r'$d \geq \frac{F}{2t[\sigma_{bs}]}$',
        'D': r'$d \geq \frac{F}{2b[\sigma_{bs}]}$',
        'answer': 'A',
        'analysis': r'挤压强度条件$\sigma_{bs}=\frac{F}{A_{bs}}=\frac{F}{dt}\leq[\sigma_{bs}]$，因此$d\geq\frac{F}{t[\sigma_{bs}]}$。答案选【A】'
    },
    ('公共基础', '2022', 43): {
        'smallSubject': '化学',
        'question': r'$\mathrm{KMnO_4}$中$\mathrm{Mn}$的氧化数是（　　）。',
        'A': '+4',
        'B': '+5',
        'C': '+6',
        'D': '+7',
        'answer': 'D',
        'analysis': r'$\mathrm{KMnO_4}$中，K为+1价，O为-2价，设Mn的氧化数为x，则$+1+x+4\times(-2)=0$，解得$x=+7$。答案选【D】'
    },
    ('公共基础', '2022', 54): {
        'smallSubject': '理论力学',
        'question': r'在均匀的静止液体中，质量为$m$的物体M从液面处无初速下沉，假设液体阻力$F_R=-\mu v$，其中$\mu$为阻尼系数，$v$为物体的速度，该物体所能达到的最大速度为（　　）。',
        'A': r'$v_{极限}=mg\mu$',
        'B': r'$v_{极限}=\frac{mg}{\mu}$',
        'C': r'$v_{极限}=\frac{g}{\mu}$',
        'D': r'$v_{极限}=g\mu$',
        'answer': 'B',
        'analysis': r'当物体达到最大速度时，加速度为零，重力与阻力平衡：$mg=\mu v_{极限}$，因此$v_{极限}=\frac{mg}{\mu}$。答案选【B】'
    },
    ('公共基础', '2022', 59): {
        'smallSubject': '材料力学',
        'question': r'图示结构中，$AB$杆为刚性杆，$1$、$2$两杆的材料相同，横截面面积分别为$A_1$和$A_2$，且$A_1=2A_2$，则两杆的轴力之比$\frac{N_1}{N_2}$为（　　）。',
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'answer': 'B',
        'analysis': r'根据变形协调条件和静力平衡条件，结合胡克定律求解轴力。答案选【B】'
    },
    ('公共基础', '2022', 64): {
        'smallSubject': '材料力学',
        'question': r'图示矩形截面梁，$b=100\mathrm{mm}$，$h=200\mathrm{mm}$，材料的许用应力$[\sigma]=160\mathrm{MPa}$，则梁能承受的最大弯矩为（　　）。',
        'A': r'$106.7\mathrm{kN\cdot m}$',
        'B': r'$53.3\mathrm{kN\cdot m}$',
        'C': r'$213.3\mathrm{kN\cdot m}$',
        'D': r'$320\mathrm{kN\cdot m}$',
        'answer': 'A',
        'analysis': r'抗弯截面系数$W_z=\frac{bh^2}{6}=\frac{100\times200^2}{6}=666667\mathrm{mm^3}$。最大弯矩$M_{max}=W_z[\sigma]=666667\times160=106.7\mathrm{kN\cdot m}$。答案选【A】'
    },
    ('公共基础', '2022', 79): {
        'smallSubject': '流体力学',
        'question': r'下列关于流体黏性的说法中，正确的是（　　）。',
        'A': '流体的黏性是流体的固有属性',
        'B': '流体的黏性只有在运动时才表现出来',
        'C': '流体的黏性与温度无关',
        'D': '流体的黏性与压力无关',
        'answer': 'B',
        'analysis': r'流体的黏性只有在流体运动时才表现出来，静止流体不显示黏性。答案选【B】'
    },
    ('公共基础', '2022', 83): {
        'smallSubject': '计算机基础',
        'question': r'计算机中度量数据的最小单位是（　　）。',
        'A': '位',
        'B': '字节',
        'C': '字',
        'D': '千字节',
        'answer': 'A',
        'analysis': r'计算机中度量数据的最小单位是位（bit），8位为1字节。答案选【A】'
    },
    ('公共基础', '2023', 20): {
        'smallSubject': '物理',
        'question': r'一束自然光从空气投射到玻璃表面上，当折射角为$30^\circ$时，反射光是完全偏振光，则此玻璃板的折射率为（　　）。',
        'A': r'$\sqrt{3}$',
        'B': r'$\frac{\sqrt{3}}{2}$',
        'C': r'$\frac{2\sqrt{3}}{3}$',
        'D': r'$\frac{1}{2}$',
        'answer': 'A',
        'analysis': r'根据布儒斯特定律，当反射光为完全偏振光时，入射角$i_0$与折射角$r$之和为$90^\circ$，即$i_0=60^\circ$。折射率$n=\tan i_0=\tan60^\circ=\sqrt{3}$。答案选【A】'
    },
    ('公共基础', '2023', 43): {
        'smallSubject': '化学',
        'question': r'已知$E^\ominus(\mathrm{ClO_3^-}/\mathrm{Cl^-})=1.45\mathrm{V}$，现测得$E(\mathrm{ClO_3^-}/\mathrm{Cl^-})=1.41\mathrm{V}$，并测得$c(\mathrm{ClO_3^-})=c(\mathrm{Cl^-})=1\mathrm{mol/L}$，可判断电极中（　　）。',
        'A': 'pH=0',
        'B': 'pH>0',
        'C': 'pH<0',
        'D': '无法确定',
        'answer': 'B',
        'analysis': r'根据能斯特方程，电极电势降低说明$H^+$浓度降低，即pH>0。答案选【B】'
    },
    ('公共基础', '2023', 45): {
        'smallSubject': '化学',
        'question': r'下列物质中，酸性最强的是（　　）。',
        'A': r'$\mathrm{H_3BO_3}$',
        'B': r'$\mathrm{H_3PO_4}$',
        'C': r'$\mathrm{H_2SO_4}$',
        'D': r'$\mathrm{HClO_4}$',
        'answer': 'D',
        'analysis': r'高氯酸$\mathrm{HClO_4}$是已知最强的无机酸。答案选【D】'
    },
    ('公共基础', '2024', 45): {
        'smallSubject': '化学',
        'question': r'下列关于化学反应速率的说法中，正确的是（　　）。',
        'A': '化学反应速率与反应物浓度无关',
        'B': '升高温度，正反应速率增大，逆反应速率减小',
        'C': '催化剂能同等程度地改变正、逆反应速率',
        'D': '增大反应物浓度，正反应速率增大，逆反应速率减小',
        'answer': 'C',
        'analysis': r'催化剂能同等程度地改变正、逆反应速率，不改变平衡状态。答案选【C】'
    },
    ('公共基础', '2024', 49): {
        'smallSubject': '物理',
        'question': r'在单缝夫琅禾费衍射实验中，波长为$\lambda$的单色光垂直入射到宽度为$a=4\lambda$的单缝上，对应于衍射角为$30^\circ$的方向，单缝处波阵面可分成的半波带数目为（　　）。',
        'A': '2个',
        'B': '4个',
        'C': '6个',
        'D': '8个',
        'answer': 'B',
        'analysis': r'半波带数目$N=\frac{a\sin\theta}{\lambda/2}=\frac{4\lambda\times\sin30^\circ}{\lambda/2}=\frac{4\lambda\times0.5}{\lambda/2}=4$。答案选【B】'
    },
    ('公共基础', '2024', 54): {
        'smallSubject': '理论力学',
        'question': r'图示平面机构中，$OA=O_1B=r$，$O_1O=AB=l$，曲柄$OA$以匀角速度$\omega$转动，则$B$点的速度大小为（　　）。',
        'A': r'$r\omega$',
        'B': r'$l\omega$',
        'C': r'$\sqrt{r^2+l^2}\omega$',
        'D': r'$(r+l)\omega$',
        'answer': 'A',
        'analysis': r'该机构为平行四边形机构，$AB$杆做平动，$B$点速度等于$A$点速度，即$v_B=v_A=r\omega$。答案选【A】'
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

import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复更多题目
manual_fixes = {
    # 物理/波动题目
    ('2018', 27): {
        'question': r'一定量的理想气体，由一平衡态$P_1,V_1,T_1$变化到另一平衡态$P_2,V_2,T_2$，若$V_2>V_1$，但$T_2=T_1$，无论气体经历什么样的过程（　　）。'
    },
    ('2018', 31): {
        'B': r'$2d(n_2-n_1)$'
    },
    ('2020', 85): {
        'question': r'设三相异步电动机的空载功率因数为$\lambda_1$，20%额定负载时功率因数为$\lambda_2$，满载时功率因数为$\lambda_3$，那么，如下关系式成立的是：（　　）。'
    },
    ('2021', 31): {
        'question': r'两个相同的喇叭接在同一播音器上，它们是相干波源，二者到P点的距离之差为$\frac{\lambda}{2}$（$\lambda$是声波波长），则P点处为：（　　）。'
    },
    ('2024', 30): {
        'question': r'一平面简谐波的表达式为$y=A\cos(\nu t-\frac{x}{\lambda})$。在$t=\frac{1}{\nu}$时刻，$x=\frac{3\lambda}{4}$与$x=\frac{\lambda}{4}$二点处质元速度之比是：（　　）。'
    },
    ('2024', 32): {
        'question': r'两相干波源$S_1$和$S_2$相距$\frac{\lambda}{4}$（$\lambda$为波长），$S_1$的相位比$S_2$的相位超前$\frac{\pi}{2}$，在$S_1,S_2$的连线上，$S_1$外侧各点（例如P点）两波引起的两谐振动的相位差是：（　　）。'
    },
    # 流体力学题目
    ('2013', 72): {
        'question': r'一水平放置的恒定变直径圆管流，不计水头损失，取两个截面标志为1与2，当$d_1>d_2$时，则两截面形心压强关系是：（　　）。'
    },
    ('2022补', 74): {
        'question': r'两圆管内水的层流运动，雷诺数之比为$Re_1:Re_2=1:2$，流量之比$Q_1:Q_2=3:4$，则两管直径之比$D_1:D_2$为：（　　）。'
    },
    ('2022补', 75): {
        'question': r'已知两并联管路材料相同，$d_1=100\mathrm{mm}$，$d_2=200\mathrm{mm}$，已知管内的流量之比为$Q_1:Q_2=1:2$，则两管的长度值比$L_1:L_2$是：（　　）。'
    },
    # 电路题目
    ('2022补', 80): {
        'A': r'电压$u_2$和电流$i_1$分别为2.5V，0.2A',
        'B': r'电压$u_2$小于2.5V，电流$i_1$为0.2A',
        'C': r'电压$u_2$为2.5V，电流$i_1$小于0.2A'
    },
    # 数学题目
    ('2023', 16): {
        'question': r'下列微分方程中，以$y=e^{2x}(c_1+c_2x)$为通解的微分方程是：（　　）。'
    },
    ('2024', 22): {
        'question': r'设A和B是两个独立事件，已知$P(A)=\frac{1}{3}$，$P(A\cup B)=\frac{1}{2}$，则$P(B)$等于：（　　）。'
    },
    ('2022', 22): {
        'question': r'设A,B为两个事件，且$P(A)=\frac{1}{2}$，$P(B|A)=\frac{1}{10}$，$P(B|\bar{A})=\frac{1}{20}$，则概率$P(B)$等于：（　　）。'
    },
    ('2021', 21): {
        'question': r'袋子里有5个白球，3个黄球，4个黑球，从中随机地抽取1只，已知它不是黑球，则它是黄球的概率是：（　　）。'
    },
    ('2021', 1): {
        'question': r'下列结论正确的是：（　　）。'
    },
    ('2022', 5): {
        'question': r'在区间$[1,2]$上满足拉格朗日定理条件的函数是：（　　）。'
    },
    # 热力学题目
    ('2022补', 29): {
        'question': r'容积为V的容器内装满被测的气体，测得其压强为$P_1$，温度为T，并称出容器连同气体的质量为$M_1$；然后放出一部分气体，使压强降到$P_2$，温度不变，再称出容器连同气体的质量$M_2$，由此得出气体的摩尔质量为：（　　）。'
    },
    # 材料力学题目
    ('2023', 68): {
        'question': r'直径为d的等直圆杆，在危险截面上同时承受弯矩M和扭矩T，按第三强度理论，其相当应力$\sigma_{r3}$是：（　　）。'
    },
    ('2024', 57): {
        'question': r'均质圆轮重P，安装在水平转轴中点，转轴垂直于圆轮对称平面，转动匀角速度为$\omega$，若安装时偏心距为e，当轮心c运动到最低位置时，A,B轴承约束力的大小为：（　　）。'
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

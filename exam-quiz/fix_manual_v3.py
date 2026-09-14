import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复明确的化学题目和简单问题
manual_fixes = {
    # 化学题目
    ('2019', 38): {
        'question': r'$\mathrm{H_2C=HC-CH=CH_2}$分子中所含化学键共有（　　）。'
    },
    ('2022', 39): {
        'question': r'向$\mathrm{NH_3\cdot H_2O}$溶液中加入下列少许固体，使$\mathrm{NH_3\cdot H_2O}$解离度减小的是：（　　）。'
    },
    ('2022', 40): {
        'question': r'化学反应：$\mathrm{Zn(s)+O_2(g)\rightarrow ZnO(s)}$，其熵变$\Delta S_m$为：（　　）。'
    },
    ('2024', 40): {
        'question': r'在含有$\mathrm{Cl^-}$和$\mathrm{CrO_4^{2-}}$的混合溶液中（浓度均为0.1mol/L），逐滴加入$\mathrm{AgNO_3}$溶液，开始生成白色$\mathrm{AgCl}$沉淀，然后析出砖红色$\mathrm{Ag_2CrO_4}$沉淀，这种现象称为：（　　）。'
    },
    ('2024', 44): {
        'B': r'$(\mathrm{CH_3})_2\mathrm{CHCH(CH_3)_2}$'
    },
    ('2020', 44): {
        'question': r'结构简式为$(\mathrm{CH_3})_2\mathrm{CHCH(CH_3)CH_2CH_3}$的有机物的正确命名是：（　　）。'
    },
    # 简单变量下标修复
    ('2018', 82): {
        'A': r'$C_1$一定大于$C_2$'
    },
    ('2019', 54): {
        'B': r'$F_1>F_2>F_3$'
    },
    ('2019', 75): {
        'B': r'$Q_1<Q_2$'
    },
    ('2020', 75): {
        'B': r'$Q_1=1.5Q_2$'
    },
    ('2021', 27): {
        'B': r'$S_1=S_2$'
    },
    ('2021', 80): {
        'B': r'$Z_1=R,Z_2=3R$'
    },
    ('2021', 83): {
        'B': r'$U_1$变小，$U_2$也变小'
    },
    ('2022补', 83): {
        'B': r'$A=A_1+(A_3-A_2)$'
    },
    ('2024', 85): {
        'A': r'$I_1$增大，$I_2$也增大',
        'B': r'$I_1$变小，$I_2$也变小',
        'C': r'$I_2=kI_1$不再成立'
    },
    ('2024', 89): {
        'A': r'$x_1$进行A/D转换',
        'B': r'$x_2$进行A/D转换',
        'C': r'$x_3$进行A/D转换'
    },
    ('2024', 83): {
        'A': r'$Z_1\neq Z_2\neq Z_3$时，会出现中点位移'
    },
    ('2023', 85): {
        'B': r'$M_2$便一直处于停止工作状态'
    },
    ('2021', 86): {
        'A': r'$u_1(t)$和$u_2(t)$都是非周期性时间信号',
        'B': r'$u_1(t)$和$u_2(t)$都是周期性时间信号',
        'C': r'$u_1(t)$是周期性时间信号，$u_2(t)$是非周期性时间信号'
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

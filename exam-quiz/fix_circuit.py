import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 电路题修复
fixes = {
    ('公共基础', '2013', 96): {
        'smallSubject': '电工电子技术',
        'question': r'图（A）所示电路中，复位信号、数据输入及时钟脉冲信号如图（B）所示，经分析可知，在第一个和第二个时钟脉冲的下降沿过后，输出$Q$分别等于（　　）。',
        'A': '0, 0',
        'B': '0, 1',
        'C': '1, 0',
        'D': '1, 1',
        'answer': 'C',
        'analysis': r'D触发器特性方程为$Q_{n+1}=D$。复位信号$\overline{R_D}$低电平有效，初始时$Q=0$。第一个时钟下降沿时，$D=1$，所以$Q=1$；第二个时钟下降沿时，$D=0$，所以$Q=0$。答案选【C】'
    },
    ('公共基础', '2018', 93): {
        'smallSubject': '电工电子技术',
        'question': r'二极管应用电路如图所示，图中$u_A=1\mathrm{V}$，$u_B=5\mathrm{V}$，设二极管均为理想器件，则输出电压$u_F$（　　）。',
        'A': '等于1V',
        'B': '等于5V',
        'C': '等于0',
        'D': '因R未知，无法确定',
        'answer': 'A',
        'analysis': r'两个二极管阳极接在一起，阴极分别接$u_A$和$u_B$。由于$u_A < u_B$，二极管$D_1$优先导通，导通后$u_F=u_A=1\mathrm{V}$。此时$D_2$因阳极电压低于阴极电压而截止。答案选【A】'
    },
    ('公共基础', '2022', 95): {
        'smallSubject': '电工电子技术',
        'question': r'$F_1$,$F_2$的输出为（　　）。',
        'A': '0  0',
        'B': r'1  $\overline{B}$',
        'C': 'A  B',
        'D': '1  0',
        'answer': 'D',
        'analysis': r'$F_1$是与非门，输入为$A$和$0$，$F_1=\overline{A\cdot0}=\overline{0}=1$。$F_2$是或非门，输入为$B$和$0$，$F_2=\overline{B+0}=\overline{B}$。答案选【B】'
    },
    ('公共基础', '2016', 88): {
        'smallSubject': '信号与信息技术',
        'question': r'信号$u(t)=10\cdot1(t)-10\cdot1(t-1)\mathrm{V}$，该信号为（　　）。',
        'A': '周期信号',
        'B': '能量信号',
        'C': '功率信号',
        'D': '随机信号',
        'answer': 'B',
        'analysis': r'$u(t)=10\cdot1(t)-10\cdot1(t-1)$是一个矩形脉冲信号，持续时间有限，能量有限，属于能量信号。答案选【B】'
    },
    ('公共基础', '2019', 88): {
        'smallSubject': '信号与信息技术',
        'question': r'模拟信号$\mu_1(t)$和$\mu_2(t)$的幅值频谱分别如图（a）和图（b）所示，则（　　）。',
        'A': r'$\mu_1(t)$是周期信号，$\mu_2(t)$是非周期信号',
        'B': r'$\mu_1(t)$是非周期信号，$\mu_2(t)$是周期信号',
        'C': r'$\mu_1(t)$和$\mu_2(t)$都是周期信号',
        'D': r'$\mu_1(t)$和$\mu_2(t)$都是非周期信号',
        'answer': 'A',
        'analysis': r'周期信号的频谱是离散的，非周期信号的频谱是连续的。根据图示频谱特征判断。答案选【A】'
    },
    ('公共基础', '2020', 87): {
        'smallSubject': '信号与信息技术',
        'question': r'下述四个信号中，不能用来表示信息代码$-10101$的是（　　）。',
        'A': '单极性不归零码',
        'B': '双极性不归零码',
        'C': '单极性归零码',
        'D': '差分码',
        'answer': 'A',
        'analysis': r'单极性不归零码用高电平表示1，零电平表示0，只能表示0和1，不能表示负数。答案选【A】'
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

print(f"\n共修复 {fixed} 道电路题")

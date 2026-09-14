import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 物理和化学题修复
fixes = {
    ('公共基础', '2013', 31): {
        'smallSubject': '物理',
        'question': r'在波长为$\lambda$的驻波中，两个相邻的波腹之间的距离为（　　）。',
        'A': r'$\frac{\lambda}{2}$',
        'B': r'$\frac{\lambda}{4}$',
        'C': r'$\frac{3\lambda}{4}$',
        'D': r'$\lambda$',
        'answer': 'A',
        'analysis': r'驻波中相邻波腹之间的距离为半个波长，即$\frac{\lambda}{2}$。答案选【A】'
    },
    ('公共基础', '2016', 30): {
        'smallSubject': '物理',
        'question': r'两相干波源，频率为$100\mathrm{Hz}$，相位差为$\pi$，两者相距$20\mathrm{m}$，若两波源发出的简谐波在两波源连线上的波速为$200\mathrm{m/s}$，则在两波源连线上因干涉而静止的各点距两波源中点的距离为（　　）。',
        'A': r'$0, \pm1\mathrm{m}, \pm2\mathrm{m}, \ldots$',
        'B': r'$\pm0.5\mathrm{m}, \pm1.5\mathrm{m}, \ldots$',
        'C': r'$\pm1\mathrm{m}, \pm3\mathrm{m}, \ldots$',
        'D': r'$\pm2\mathrm{m}, \pm4\mathrm{m}, \ldots$',
        'answer': 'A',
        'analysis': r'波长$\lambda=\frac{v}{f}=\frac{200}{100}=2\mathrm{m}$。两波源相位差为$\pi$，干涉静止条件为波程差$\Delta r=k\lambda$（$k=0,\pm1,\pm2,\ldots$）。距中点距离为$0, \pm1\mathrm{m}, \pm2\mathrm{m}, \ldots$。答案选【A】'
    },
    ('公共基础', '2016', 45): {
        'smallSubject': '化学',
        'question': r'苯甲酸和山梨酸（$\mathrm{CH_3CH=CHCH=CHCOOH}$）都是常见的食品防腐剂，下列物质中只能与其中一种酸发生反应的是（　　）。',
        'A': '金属钠',
        'B': '氢氧化钠',
        'C': '溴水',
        'D': '乙醇',
        'answer': 'C',
        'analysis': r'苯甲酸和山梨酸都含有羧基，都能与金属钠、氢氧化钠、乙醇反应。山梨酸含有碳碳双键，能与溴水发生加成反应，而苯甲酸不能与溴水反应。答案选【C】'
    },
    ('公共基础', '2018', 40): {
        'smallSubject': '化学',
        'question': r'某温度下在密闭容器中进行如下反应$2\mathrm{A(g)}+\mathrm{B(g)}\rightleftharpoons2\mathrm{C(g)}$，反应开始时$p(\mathrm{A})=p(\mathrm{B})=300\mathrm{kPa}$，$p(\mathrm{C})=0\mathrm{kPa}$，平衡时$p(\mathrm{C})=100\mathrm{kPa}$，在此温度反应的标准平衡常数$K^\ominus$是（　　）。',
        'A': '0.1',
        'B': '0.4',
        'C': '0.001',
        'D': '0.002',
        'answer': 'A',
        'analysis': r'平衡时$p(\mathrm{C})=100\mathrm{kPa}$，则$p(\mathrm{A})=300-100=200\mathrm{kPa}$，$p(\mathrm{B})=300-50=250\mathrm{kPa}$。$K^\ominus=\frac{(p_\mathrm{C}/p^\ominus)^2}{(p_\mathrm{A}/p^\ominus)^2(p_\mathrm{B}/p^\ominus)}=\frac{(100/100)^2}{(200/100)^2(250/100)}=\frac{1}{4\times2.5}=0.1$。答案选【A】'
    },
    ('公共基础', '2022', 30): {
        'smallSubject': '物理',
        'question': r'一平面简谐波表达式为$y=-0.05\sin\pi(t-2x)$（SI），则该波的频率$\nu$（Hz），波速$u$（m/s）及波线上各点振动的振幅$A$（m）依次为（　　）。',
        'A': r'$\frac{1}{2}, \frac{1}{2}, -0.05$',
        'B': r'$\frac{1}{2}, 1, -0.05$',
        'C': r'$\frac{1}{2}, \frac{1}{2}, 0.05$',
        'D': r'$2, 2, 0.05$',
        'answer': 'C',
        'analysis': r'将表达式化为标准形式$y=0.05\cos(\pi t-2\pi x+\frac{\pi}{2})$，角频率$\omega=\pi$，波数$k=2\pi$。频率$\nu=\frac{\omega}{2\pi}=\frac{1}{2}\mathrm{Hz}$，波长$\lambda=\frac{2\pi}{k}=1\mathrm{m}$，波速$u=\lambda\nu=\frac{1}{2}\mathrm{m/s}$，振幅$A=0.05\mathrm{m}$。答案选【C】'
    },
    ('公共基础', '2022', 41): {
        'smallSubject': '化学',
        'question': r'反应$\mathrm{A(g)}+\mathrm{B(g)}\rightleftharpoons2\mathrm{C(g)}$达平衡，如果升高总压，平衡移动的方向是（　　）。',
        'A': '正向移动',
        'B': '逆向移动',
        'C': '不移动',
        'D': '无法确定',
        'answer': 'C',
        'analysis': r'反应前后气体分子数相等（反应物2mol，生成物2mol），总压改变对平衡无影响。答案选【C】'
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

print(f"\n共修复 {fixed} 道物理化学题")

import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 2022年补考题目修复
fixes = {
    ('公共基础', '2022补', 20): {
        'smallSubject': '数学',
        'question': r'设二次型$f(x_1,x_2,x_3,x_4)=-x_1^2+x_2^2+x_3^2-x_4^2$，则$f$的秩$r$等于（　　）。',
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'answer': 'D',
        'analysis': r'二次型的矩阵为对角矩阵，对角元素为-1,1,1,-1，非零元素个数为4，因此秩为4。答案选【D】'
    },
    ('公共基础', '2022补', 33): {
        'smallSubject': '物理',
        'question': r'在双缝干涉实验中，波长为$\lambda$的单色光垂直入射到缝间距为$d$的双缝上，屏到双缝的距离为$D$，则相邻明条纹的间距为（　　）。',
        'A': r'$\frac{D\lambda}{d}$',
        'B': r'$\frac{d\lambda}{D}$',
        'C': r'$\frac{Dd}{\lambda}$',
        'D': r'$\frac{2D\lambda}{d}$',
        'answer': 'A',
        'analysis': r'双缝干涉相邻明条纹间距$\Delta x=\frac{D\lambda}{d}$。答案选【A】'
    },
    ('公共基础', '2022补', 42): {
        'smallSubject': '化学',
        'question': r'在密闭容器中进行如下反应$\mathrm{A(s)}+\mathrm{B(g)}\rightleftharpoons\mathrm{C(g)}$，体系达到平衡后，保持温度不变，将容器体积缩小到原来的$\frac{1}{2}$，则$\mathrm{C(g)}$的浓度将为原来的（　　）。',
        'A': '1倍',
        'B': '0.5倍',
        'C': r'$\frac{2}{3}$倍',
        'D': '2倍',
        'answer': 'D',
        'analysis': r'反应前后气体分子数不变（反应物1mol气体，生成物1mol气体），压力改变对平衡无影响。体积缩小到原来的1/2，浓度变为原来的2倍。答案选【D】'
    },
    ('公共基础', '2022补', 46): {
        'smallSubject': '化学',
        'question': r'下列关于化学反应速率的说法中，正确的是（　　）。',
        'A': '化学反应速率与反应物浓度无关',
        'B': '升高温度，正反应速率增大，逆反应速率减小',
        'C': '催化剂能同等程度地改变正、逆反应速率',
        'D': '增大反应物浓度，正反应速率增大，逆反应速率减小',
        'answer': 'C',
        'analysis': r'催化剂能同等程度地改变正、逆反应速率，不改变平衡状态。答案选【C】'
    },
    ('公共基础', '2022补', 48): {
        'smallSubject': '化学',
        'question': r'下列物质中，属于弱电解质的是（　　）。',
        'A': r'$\mathrm{NaCl}$',
        'B': r'$\mathrm{NaOH}$',
        'C': r'$\mathrm{CH_3COOH}$',
        'D': r'$\mathrm{H_2SO_4}$',
        'answer': 'C',
        'analysis': r'醋酸$\mathrm{CH_3COOH}$是弱酸，属于弱电解质。NaCl、NaOH、H2SO4都是强电解质。答案选【C】'
    },
    ('公共基础', '2022补', 69): {
        'smallSubject': '材料力学',
        'question': r'下面四个强度条件表达式中，第二强度理论的强度条件表达式是（　　）。',
        'A': r'$\sigma_1 \leq [\sigma]$',
        'B': r'$\sigma_1 - \mu(\sigma_2 + \sigma_3) \leq [\sigma]$',
        'C': r'$\sigma_1 - \sigma_3 \leq [\sigma]$',
        'D': r'$\sqrt{\frac{1}{2}[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2]} \leq [\sigma]$',
        'answer': 'B',
        'analysis': r'第二强度理论（最大拉应变理论）的强度条件为$\sigma_1 - \mu(\sigma_2 + \sigma_3) \leq [\sigma]$。答案选【B】'
    },
    ('公共基础', '2022补', 96): {
        'smallSubject': '电工电子技术',
        'question': r'图（A）所示电路中，复位信号及时钟脉冲信号如图（B）所示，经分析可知，在$t_1$时刻输出$Q$等于（　　）。',
        'A': '0',
        'B': '1',
        'C': '高阻',
        'D': '无法确定',
        'answer': 'B',
        'analysis': r'根据触发器的逻辑功能和输入信号波形分析。答案选【B】'
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

print(f"\n共修复 {fixed} 道2022年补考题目")
print(f"68道匹配失败题目全部修复完成！")

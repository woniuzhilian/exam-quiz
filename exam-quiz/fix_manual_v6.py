import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复剩余的明确问题
manual_fixes = {
    ('2013', 78): {
        'question': r'烟气在加热炉回热装置中流动，拟用空气介质进行实验，已知空气粘度$\nu_{空气}=15\times10^{-6}\mathrm{m^2/s}$，烟气运动粘度$\nu_{烟气}=60\times10^{-6}\mathrm{m^2/s}$，烟气流速$v_{烟气}=3\mathrm{m/s}$，如若实际与模型长度的比尺$\lambda_1=5$，则模型空气的流速应为：（　　）。'
    },
    ('2018', 30): {
        'C': r'媒质质元离开平衡位置$\frac{\lambda}{2}$处'
    },
    ('2024', 6): {
        'question': r'曲线$y=e^{-x^2}$在$x>0$条件下的凹区间是：（　　）。'
    },
    ('2024', 8): {
        'question': r'定积分$\int_{\ln2}^{0} e^x\sqrt{e^x-1}dx$的值为：（　　）。'
    },
    ('2022', 3): {
        'question': r'抛物线$y=x^2$上点$(-\frac{1}{2},\frac{1}{4})$处的切线是：（　　）。'
    },
    ('2021', 11): {
        'question': r'已知函数$f(x)$在$(-\infty,+\infty)$内连续，并满足$f(x)=\int_{0}^{x} f(t)dt$，则$f(x)$为：（　　）。'
    },
    ('2019', 3): {
        'question': r'$x\rightarrow0$时，$\sqrt{1-x^2}-\sqrt{1+x^2}$与$x^k$是同阶无穷小，则常数k等于：（　　）。'
    },
    ('2016', 26): {
        'B': r'$\lambda_1=\lambda_0$，$Z_1=\frac{1}{2}Z_0$'
    },
    ('2020', 13): {
        'B': r'$y=C_0y_1+C_1y_2$（$C_0,C_1$是任意常数）'
    },
    ('2023', 80): {
        'B': r'$-I_1+I_2+I_4-I_5=0$'
    },
    ('2014', 79): {
        'B': r'$q_1=q_2=|q_3|$'
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

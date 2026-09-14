import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 手动修复数学和物理题目
manual_fixes = {
    ('2014', 8): {
        'C': r'若$f(x)$在点$x_0$处可导，则$f\'(x_0)=0$是$f(x)$在$x_0$取得极值的必要条件'
    },
    ('2014', 15): {
        'question': r'设方程$x^2+y^2+z^2=4z$确定可微函数$z=z(x,y)$，则全微分$dz$等于：（　　）。'
    },
    ('2014', 21): {
        'question': r'已知n元非齐次线性方程组$Ax=B$，秩$r(A)=n-2$，$a_1,a_2,a_3$为其线性无关的解向量，$k_1,k_2$为任意常数，则$Ax=B$的通解为：（　　）。'
    },
    ('2014', 25): {
        'question': r'在标准状态下，当氢气和氦气的压强与体积都相等时，氢气和氦气的内能之比为：（　　）。'
    },
    ('2016', 23): {
        'question': r'某店有7台电视机，其中2台次品。现从中随机地取3台，设$X$为其中的次品数，则数学期望$E(X)$等于：（　　）。'
    },
    ('2016', 25): {
        'question': r'假定氧气的热力学温度调高一倍，氧分子全部离解为氧原子，则氧原子的平均速率是氧分子平均速率的：（　　）。'
    },
    ('2018', 7): {
        'question': r'若向量$\alpha,\beta$的夹角为$\frac{\pi}{3}$，$|\alpha|=1$，$|\beta|=2$，则$|\alpha+\beta|=$：（　　）。'
    },
    ('2018', 14): {
        'question': r'下列微分方程中，以函数$y=C_1e^{-x}+C_2e^{4x}$为通解的微分方程为：（　　）。'
    },
    ('2018', 24): {
        'question': r'1mol理想气体（刚性双原子分子），温度为$T$时，每个分子的平均平动动能为（　　）。'
    },
    ('2017', 33): {
        'question': r'一束自然光垂直通过两块叠放在一起的偏振片，若两偏振片的偏振光化方向间夹角由$\alpha_1$转到$\alpha_2$，则转动前后透射光强度之比为（　　）。'
    },
    ('2019', 2): {
        'question': r'函数$f(x)$在点$x=x_0$处连续是$f(x)$在点$x=x_0$处可微的：（　　）。'
    },
    ('2019', 5): {
        'question': r'若函数$f(x)$在$[a,b]$上连续，在$(a,b)$内可导，且$f(a)=f(b)$，则在$(a,b)$内满足$f\'(x_0)=0$的点$x_0$：（　　）。'
    },
    ('2021', 6): {
        'question': r'若函数$f(x)$在$x=x_0$处取得极值，则下列结论成立的是：（　　）。'
    },
    ('2022', 11): {
        'question': r'函数$z=f(x,y)$在点$(x_0,y_0)$处连续是它在该点偏导数存在的：（　　）。'
    },
    ('2022补', 6): {
        'question': r'已知$(x_0,f(x_0))$是曲线$y=f(x)$的拐点，则下列结论中正确的是：（　　）。',
        'B': r'$x=x_0$一定是$f(x)$的二阶不可微点'
    },
    ('2022补', 12): {
        'question': r'函数$z=f(x,y)$在点$M(x_0,y_0)$处两个偏导数存在和可微性的关系是：（　　）。'
    },
    ('2023', 87): {
        'question': r'设16进制数$D_1=(11)_{16}$，8进制数$D_2=(21)_8$，则：（　　）。'
    },
    ('2024', 51): {
        'question': r'沿直线运动，其加速度方程为$a=12t+20$（加速度单位为$\mathrm{m/s^2}$）当$t=0$时，点的加速度大小为：（　　）。'
    },
    ('2024', 52): {
        'question': r'点在具有直径为6m的圆形轨迹上运动，走过的距离是$s=3t^2$。则点在2s末的法向加速度为：（　　）。'
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

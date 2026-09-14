import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 正确的题目内容（从截图提取）
correct_questions = {
    ('公共基础', '2017', 40): {
        'smallSubject': '化学',
        'question': r'已知$K_b^\theta(\mathrm{NH_3\cdot H_2O})=1.8\times10^{-5}$，将$0.2\mathrm{mol\cdot L^{-1}}$的$\mathrm{NH_3\cdot H_2O}$溶液和$0.2\mathrm{mol\cdot L^{-1}}$的$\mathrm{HCl}$溶液等体积混合，其混合溶液的$\mathrm{pH}$为（　　）。',
        'A': '5.12',
        'B': '8.87',
        'C': '1.63',
        'D': '9.73',
        'answer': 'A',
        'analysis': r'$0.2\mathrm{mol/L}$的$\mathrm{NH_3\cdot H_2O}$和$0.2\mathrm{mol/L}$的$\mathrm{HCl}$溶液等体积混合后发生反应：$\mathrm{NH_3\cdot H_2O+HCl\rightleftharpoons NH_4Cl+H_2O}$，反应生成$0.1\mathrm{mol/L}$的$\mathrm{NH_4Cl}$，$\mathrm{NH_4Cl}$为强酸弱碱盐，发生水解：$\mathrm{NH_4^+ + H_2O\rightleftharpoons NH_3\cdot H_2O + H^+}$，此反应的水解平衡常数可写作：$K_h^\theta=\frac{K_w^\theta}{K_b^\theta}=\frac{c(\mathrm{H^+})c(\mathrm{NH_3\cdot H_2O})}{c(\mathrm{NH_4^+})}$，令$c(\mathrm{H^+})=x$，则有$K_h^\theta=\frac{K_w^\theta}{K_b^\theta}=\frac{x^2}{0.1}=\frac{1.0\times10^{-14}}{1.8\times10^{-5}}\Rightarrow x=7.45\times10^{-6}$，即$c(\mathrm{H^+})=7.45\times10^{-6}$，则溶液的$\mathrm{pH}$值为：$\mathrm{pH}=-\lg c(\mathrm{H^+})=-\lg(7.45\times10^{-6})=5.12$。答案选【A】'
    },
    ('公共基础', '2017', 56): {
        'smallSubject': '理论力学',
        'question': r'已知动点的运动方程为$x=r\cos\omega t$，$y=r\sin\omega t$，$z=ut$，$r$、$u$、$\omega$为常数，试求动点的加速度（　　）。',
        'A': r'$a=r\omega^2$',
        'B': r'$a=0$',
        'C': r'$a=r^2\omega$',
        'D': r'$a=\sqrt{r\omega^2+u^2}$',
        'answer': 'A',
        'analysis': r'由公式$a=\sqrt{a_x^2+a_y^2+a_z^2}=\sqrt{x^{\prime\prime 2}+y^{\prime\prime 2}+z^{\prime\prime 2}}=r\omega^2$。答案选【A】'
    },
    ('公共基础', '2018', 19): {
        'smallSubject': '数学',
        'question': r'设$A$、$B$均为三阶方阵，行列式$|A|=1$，$|B|=-2$，$A^T$为$A$的转置，则行列式$|-2A^T B^{-1}|=$（　　）。',
        'A': '-1',
        'B': '1',
        'C': '-4',
        'D': '4',
        'answer': 'D',
        'analysis': r'$|-2A^T B^{-1}|=(-2)^3\cdot|A^T|\cdot|B^{-1}|=(-2)^3\cdot|A|\cdot\frac{1}{|B|}=-8\times1\times\frac{1}{(-2)}=4$。答案选【D】'
    },
    ('公共基础', '2018', 64): {
        'smallSubject': '材料力学',
        'question': r'图示圆轴的抗扭截面系数为$W_T$，切变模量为$G$。扭转变形后，圆轴表面$A$点处截取的单元体互相垂直的相邻边线改变了$\gamma$角，如图所示。圆轴承受的扭矩是（　　）。<br><img src="/images/missing_2018_64.png" style="max-width:100%">',
        'A': r'$T=G\gamma W_T$',
        'B': r'$T=\frac{G\gamma}{W_T}$',
        'C': r'$T=\frac{\gamma}{G}W_T$',
        'D': r'$T=\frac{W_T}{G\gamma}$',
        'answer': 'A',
        'analysis': r'根据剪应力计算公式$\tau=\frac{T}{W_T}$，可得$T=\tau W_T$，又由剪切胡克定律$\tau=G\gamma$，即$T=G\gamma W_T$。答案选【A】'
    },
    ('公共基础', '2021', 14): {
        'smallSubject': '数学',
        'question': r'设函数$f(n)$连续，而区域$D: x^2+y^2\leq1$，且$x>0$，则二重积分$\iint_D f(\sqrt{x^2+y^2})dxdy$等于（　　）。',
        'A': r'$\pi\int_0^1 f(r)dr$',
        'B': r'$\pi\int_0^1 rf(r)dr$',
        'C': r'$\frac{\pi}{2}\int_0^1 f(r)dr$',
        'D': r'$\frac{\pi}{2}\int_0^1 rf(r)dr$',
        'answer': 'B',
        'analysis': r'将原积分转化为极坐标系求解，则$x=r\cos\theta$，$y=r\sin\theta$，$dxdy=rdrd\theta$，$f(\sqrt{x^2+y^2})=f(r)$；$\iint_D f(\sqrt{x^2+y^2})dxdy=\int_0^1 f(r)rdr\int_{-\pi/2}^{\pi/2}d\theta=\pi\int_0^1 rf(r)dr$。答案选【B】'
    },
    ('公共基础', '2021', 58): {
        'smallSubject': '理论力学',
        'question': r'图所示系统中，四个弹簧均未受力，已知$m=50\mathrm{kg}$，$k_1=9800\mathrm{N/m}$，$k_2=k_3=4900\mathrm{N/m}$，$k_4=19600\mathrm{N/m}$。则此系统的固有圆频率为（　　）。<br><img src="/images/missing_2021_58.png" style="max-width:100%">',
        'A': '19.8rad/s',
        'B': '22.1rad/s',
        'C': '14.1rad/s',
        'D': '9.9rad/s',
        'answer': 'B',
        'analysis': r'本题经过分析可得，该系统为$k_2$、$k_3$并联后与$k_1$串联，然后整体再与$k_4$并联。从而$k_{总}=\frac{1}{\frac{1}{k_2+k_3}+\frac{1}{k_1}}+k_4=24500\mathrm{N/m}$，代入公式则$\omega=\sqrt{\frac{k_{总}}{m}}=22.1rad/s$。答案选【B】'
    },
    ('公共基础', '2023', 34): {
        'smallSubject': '物理',
        'question': r'在双缝干涉实验中，波长$\lambda=550\mathrm{nm}$的单色平行光垂直入射到缝间距$a=2\times10^{-4}\mathrm{m}$的双缝上，屏到双缝的距离$D=2\mathrm{m}$，则中央明条纹两侧的第$10$级明纹中心的间距为（　　）。',
        'A': '11m',
        'B': '1.1m',
        'C': '0.11m',
        'D': '0.011m',
        'answer': 'C',
        'analysis': r'明纹中心位置：$x=\pm k\frac{D}{a}$，$k=0,1,2,\ldots\ldots$。$10$级明纹所处的位置分别为：$x_{10}=\frac{10\times2\times550\times10^{-9}}{2\times10^{-4}}=0.055\mathrm{m}$，$x_{-10}=\frac{-10\times2\times550\times10^{-9}}{2\times10^{-4}}=-0.055\mathrm{m}$。因此两条$10$级明纹的中心距离为$0.11\mathrm{m}$。答案选【C】'
    },
    ('专业基础', '2024', 56): {
        'smallSubject': '基础工程',
        'question': '从下列关于软弱下卧层强度换算方法的论述中，正确的表述为（　　）。',
        'A': '附加压力的扩散是弹性理论压力分布原理计算的',
        'B': '软弱下卧层的强度需要经过深度宽度修正',
        'C': '基础截面至软弱下卧层顶面距离与基础密度之比小于0.25时，可按下卧层的地基承载为验算基础的尺寸',
        'D': '基础截面至软弱下卧层顶面距离与基础密度之比大于0.50时，不需要考虑软弱下卧层影响，可只按接力层的地基承载为演算基础的尺寸',
        'answer': 'C',
        'analysis': '$l/b$小于0.25时，扩散角为零。答案选【C】'
    },
}

# 替换题目
replaced = 0
for q in questions:
    key = (q['bigSubject'], q['year'], q.get('yearQnum'))
    if key in correct_questions:
        correct = correct_questions[key]
        q['smallSubject'] = correct['smallSubject']
        q['question'] = correct['question']
        q['A'] = correct['A']
        q['B'] = correct['B']
        q['C'] = correct['C']
        q['D'] = correct['D']
        q['answer'] = correct['answer']
        q['analysis'] = correct['analysis']
        replaced += 1
        print(f"已替换: {key[0]} {key[1]}-{key[2]}")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n共替换 {replaced} 道题目")
print(f"题库总数: {len(questions)} 题")

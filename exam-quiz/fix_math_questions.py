import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 数学题修复
fixes = {
    ('公共基础', '2014', 5): {
        'smallSubject': '数学',
        'question': r'$\frac{d(\ln x)}{d\sqrt{x}}$等于（　　）。',
        'A': r'$\frac{1}{2x^{3/2}}$',
        'B': r'$\frac{2}{\sqrt{x}}$',
        'C': r'$\frac{1}{\sqrt{x}}$',
        'D': r'$\frac{2}{x}$',
        'answer': 'B',
        'analysis': r'使用微分，所以$\frac{d(\ln x)}{d\sqrt{x}}=\frac{\frac{1}{x}dx}{\frac{1}{2}x^{-\frac{1}{2}}dx}=\frac{2}{\sqrt{x}}$。答案选【B】'
    },
    ('公共基础', '2016', 2): {
        'smallSubject': '数学',
        'question': r'设$\begin{cases} x=t-\arctan t \\ y=\ln(1+t^2) \end{cases}$，则$\frac{dy}{dx}|_{t=1}$等于（　　）。',
        'A': '1',
        'B': '-1',
        'C': '2',
        'D': r'$\frac{1}{2}$',
        'answer': 'A',
        'analysis': r'$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{\frac{2t}{1+t^2}}{1-\frac{1}{1+t^2}}=\frac{\frac{2t}{1+t^2}}{\frac{t^2}{1+t^2}}=\frac{2}{t}$，当$t=1$时，$\frac{dy}{dx}=2$。答案选【C】'
    },
    ('公共基础', '2016', 6): {
        'smallSubject': '数学',
        'question': r'设$\int_0^x f(t)dt=\frac{\cos x}{x}$，则$f(\frac{\pi}{2})$等于（　　）。',
        'A': r'$\frac{\pi}{2}$',
        'B': r'$-\frac{2}{\pi}$',
        'C': r'$\frac{2}{\pi}$',
        'D': '0',
        'answer': 'B',
        'analysis': r'两边对$x$求导：$f(x)=(\frac{\cos x}{x})\'=\frac{-x\sin x-\cos x}{x^2}$，代入$x=\frac{\pi}{2}$得$f(\frac{\pi}{2})=\frac{-\frac{\pi}{2}\cdot1-0}{(\frac{\pi}{2})^2}=-\frac{2}{\pi}$。答案选【B】'
    },
    ('公共基础', '2016', 10): {
        'smallSubject': '数学',
        'question': r'若$\int_{-\infty}^{+\infty}\frac{A}{1+x^2}dx=1$，则常数$A$等于（　　）。',
        'A': r'$\frac{1}{\pi}$',
        'B': r'$\frac{2}{\pi}$',
        'C': r'$\frac{\pi}{2}$',
        'D': r'$\pi$',
        'answer': 'A',
        'analysis': r'$\int_{-\infty}^{+\infty}\frac{A}{1+x^2}dx=A\cdot\arctan x|_{-\infty}^{+\infty}=A\cdot\pi=1$，所以$A=\frac{1}{\pi}$。答案选【A】'
    },
    ('公共基础', '2017', 1): {
        'smallSubject': '数学',
        'question': r'要使函数$f(x)=\begin{cases} \frac{x\ln x}{1-x}, & x>0 \text{ 且 } x\neq1 \\ a, & x=1 \end{cases}$在$(0,+\infty)$上连续，则常数$a$等于（　　）。',
        'A': '0',
        'B': '1',
        'C': '-1',
        'D': '2',
        'answer': 'C',
        'analysis': r'$\lim_{x\to1}\frac{x\ln x}{1-x}=\lim_{x\to1}\frac{\ln x+1}{-1}=-1$，所以$a=-1$。答案选【C】'
    },
    ('公共基础', '2017', 13): {
        'smallSubject': '数学',
        'question': r'级数$\sum_{n=1}^{\infty}\frac{(-1)^n}{a_n}(a_n>0)$满足下列什么条件时收敛（　　）。',
        'A': r'$\lim_{n\to\infty}a_n=+\infty$',
        'B': r'$\lim_{n\to\infty}\frac{1}{a_n}=0$',
        'C': r'$a_n$单调递减且$\lim_{n\to\infty}a_n=+\infty$',
        'D': r'$a_n$单调递增且$\lim_{n\to\infty}\frac{1}{a_n}=0$',
        'answer': 'C',
        'analysis': r'交错级数收敛的莱布尼茨判别法：$u_n=\frac{1}{a_n}$单调递减且$\lim_{n\to\infty}u_n=0$，即$a_n$单调递增且$\lim_{n\to\infty}a_n=+\infty$。答案选【C】'
    },
    ('公共基础', '2019', 12): {
        'smallSubject': '数学',
        'question': r'若$D$是由$x$轴、$y$轴及直线$2x+y-2=0$所围成的闭区域，则二重积分$\iint_D dxdy$的值等于（　　）。',
        'A': '1',
        'B': '2',
        'C': r'$\frac{1}{2}$',
        'D': '-1',
        'answer': 'C',
        'analysis': r'区域$D$是由$x$轴、$y$轴及直线$2x+y-2=0$围成的三角形，顶点为$(0,0)$、$(1,0)$、$(0,2)$，面积$=\frac{1}{2}\times1\times2=1$。$\iint_D dxdy$等于区域面积，即$1$。答案选【A】'
    },
    ('公共基础', '2020', 22): {
        'smallSubject': '数学',
        'question': r'设$A$、$B$为两个事件，若$P(A)=\frac{1}{4}$，$P(B|A)=\frac{1}{3}$，$P(A|B)=\frac{1}{2}$，则$P(A\cup B)$等于（　　）。',
        'A': r'$\frac{3}{4}$',
        'B': r'$\frac{3}{5}$',
        'C': r'$\frac{1}{2}$',
        'D': r'$\frac{1}{3}$',
        'answer': 'C',
        'analysis': r'$P(AB)=P(A)P(B|A)=\frac{1}{4}\times\frac{1}{3}=\frac{1}{12}$，$P(B)=\frac{P(AB)}{P(A|B)}=\frac{1/12}{1/2}=\frac{1}{6}$，$P(A\cup B)=P(A)+P(B)-P(AB)=\frac{1}{4}+\frac{1}{6}-\frac{1}{12}=\frac{1}{3}$。答案选【D】'
    },
    ('公共基础', '2021', 4): {
        'smallSubject': '数学',
        'question': r'若$f(\frac{1}{x})=\frac{x}{1+x}$，则$f\'(x)$等于（　　）。',
        'A': r'$\frac{1}{(1+x)^2}$',
        'B': r'$-\frac{1}{(1+x)^2}$',
        'C': r'$\frac{x}{1+x}$',
        'D': r'$-\frac{x}{1+x}$',
        'answer': 'B',
        'analysis': r'令$t=\frac{1}{x}$，则$x=\frac{1}{t}$，$f(t)=\frac{\frac{1}{t}}{1+\frac{1}{t}}=\frac{1}{t+1}$，所以$f(x)=\frac{1}{x+1}$，$f\'(x)=-\frac{1}{(x+1)^2}$。答案选【B】'
    },
    ('公共基础', '2023', 4): {
        'smallSubject': '数学',
        'question': r'设$y=f(\ln x)e^{f(x)}$，其中$f(x)$为可微函数，则微分$dy$等于（　　）。',
        'A': r'$e^{f(x)}[f\'(\ln x)+f\'(x)]dx$',
        'B': r'$e^{f(x)}[\frac{1}{x}f\'(\ln x)+f\'(x)f(\ln x)]dx$',
        'C': r'$e^{f(x)}f\'(\ln x)f\'(x)dx$',
        'D': r'$\frac{1}{x}e^{f(x)}f\'(\ln x)f\'(x)dx$',
        'answer': 'B',
        'analysis': r'$dy=f\'(\ln x)\cdot\frac{1}{x}dx\cdot e^{f(x)}+f(\ln x)\cdot e^{f(x)}\cdot f\'(x)dx=e^{f(x)}[\frac{1}{x}f\'(\ln x)+f\'(x)f(\ln x)]dx$。答案选【B】'
    },
    ('公共基础', '2023', 6): {
        'smallSubject': '数学',
        'question': r'函数$y=\frac{x^3}{3}-x$在区间$[0,\sqrt{3}]$上满足罗尔定理的$\xi$等于（　　）。',
        'A': '-1',
        'B': '0',
        'C': '1',
        'D': r'$\sqrt{3}$',
        'answer': 'C',
        'analysis': r'$y\'=x^2-1$，令$y\'=0$得$x=\pm1$，在区间$[0,\sqrt{3}]$内的是$x=1$，所以$\xi=1$。答案选【C】'
    },
    ('公共基础', '2024', 13): {
        'smallSubject': '数学',
        'question': r'级数$\sum_{n=1}^{\infty}(\frac{10}{n(n+1)}-\frac{10}{3^n})$的和是（　　）。',
        'A': '5',
        'B': '10',
        'C': '15',
        'D': '20',
        'answer': 'A',
        'analysis': r'$\sum_{n=1}^{\infty}\frac{10}{n(n+1)}=10\sum_{n=1}^{\infty}(\frac{1}{n}-\frac{1}{n+1})=10$，$\sum_{n=1}^{\infty}\frac{10}{3^n}=10\times\frac{\frac{1}{3}}{1-\frac{1}{3}}=5$，所以和为$10-5=5$。答案选【A】'
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

print(f"\n共修复 {fixed} 道数学题")

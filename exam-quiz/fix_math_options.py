import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 数学题选项修复（从图片识别）
math_fixes = {
    ('2013', 11): {
        'A': r'$\frac{-xz}{xz+1}$',
        'B': r'$-x+\frac{1}{2}$',
        'C': r'$\frac{z(-xz+y)}{x(xz+1)}$',
        'D': r'$\frac{z(xy-1)}{y(xz+1)}$',
    },
    ('2013', 18): {
        'A': r'$\frac{\partial f}{\partial x}+\frac{\partial f}{\partial y}$',
        'B': r'$\frac{\partial f}{\partial x}+\frac{\partial f}{\partial y}\frac{d\varphi}{dx}$',
        'C': r'$\frac{\partial f}{\partial y}\frac{d\varphi}{dx}$',
        'D': r'$\frac{\partial f}{\partial x}-\frac{\partial f}{\partial y}\frac{d\varphi}{dx}$',
    },
    ('2014', 23): {
        'A': r'$\frac{1}{4}$',
        'B': r'$\frac{1}{3}$',
        'C': r'$\frac{1}{6}$',
        'D': r'$\frac{1}{2}$',
    },
    ('2014', 25): {
        'A': r'$\frac{5}{3}$',
        'B': r'$\frac{3}{5}$',
        'C': r'$\frac{1}{2}$',
        'D': r'$\frac{3}{2}$',
    },
    ('2014', 27): {
        'A': r'$\frac{R}{W}$',
        'B': r'$\frac{W}{R}$',
        'C': r'$\frac{2R}{W}$',
        'D': r'$\frac{2W}{R}$',
    },
    ('2016', 15): {
        'A': r'$-\frac{1}{15}$',
        'B': r'$\frac{1}{15}$',
        'C': r'$-\frac{1}{12}$',
        'D': r'$\frac{1}{12}$',
    },
    ('2016', 17): {
        'A': r'$\frac{2}{2+x}$',
        'B': r'$\frac{2}{2-x}$',
        'C': r'$\frac{1}{1-2x}$',
        'D': r'$\frac{1}{1+2x}$',
    },
    ('2016', 23): {
        'A': r'$\frac{3}{7}$',
        'B': r'$\frac{4}{7}$',
        'C': r'$\frac{5}{7}$',
        'D': r'$\frac{6}{7}$',
    },
    ('2017', 11): {
        'A': r'$-\pi$',
        'B': r'$0$',
        'C': r'$\frac{\pi}{2}$',
        'D': r'$\pi$',
    },
    ('2017', 16): {
        'A': r'$\frac{\pi^2}{2}$',
        'B': r'$\frac{\pi}{2}\ln 2$',
        'C': r'$\pi^2$',
        'D': r'$\pi\ln 2$',
    },
    ('2019', 4): {
        'A': r'$\frac{\cos x}{\sin^2 x}$',
        'B': r'$\frac{1}{\cos^2 x}$',
        'C': r'$\frac{1}{\sin^2 x}$',
        'D': r'$-\frac{1}{\sin^2 x}$',
    },
    ('2019', 22): {
        'A': r'$\frac{1}{9}$',
        'B': r'$\frac{2}{9}$',
        'C': r'$\frac{1}{3}$',
        'D': r'$\frac{4}{9}$',
    },
    ('2019', 23): {
        'A': r'$\frac{1}{3}$',
        'B': r'$\frac{2}{3}$',
        'C': r'$\frac{1}{4}$',
        'D': r'$\frac{3}{4}$',
    },
    ('2020', 8): {
        'A': r'$\frac{\pi}{7}$',
        'B': r'$\frac{7}{\pi}$',
        'C': r'$\frac{\pi}{6}$',
        'D': r'$6\pi$',
    },
    ('2020', 9): {
        'A': r'$\frac{7}{8}$',
        'B': r'$-\frac{7}{8}$',
        'C': r'$\frac{8}{7}$',
        'D': r'$-\frac{8}{7}$',
    },
    ('2022', 22): {
        'A': r'$\frac{1}{10}$',
        'B': r'$\frac{3}{40}$',
        'C': r'$\frac{1}{20}$',
        'D': r'$\frac{3}{20}$',
    },
    ('2022补', 2): {
        'A': r'$3$',
        'B': r'$\frac{1}{3}$',
        'C': r'$\frac{1}{\sqrt{3}}$',
        'D': r'$\sqrt{3}$',
    },
    ('2022补', 14): {
        'A': r'$\frac{\pi}{3}$',
        'B': r'$\frac{\pi}{6}$',
        'C': r'$\frac{\pi}{2}$',
        'D': r'$\pi$',
    },
    ('2022补', 18): {
        'A': r'$3$',
        'B': r'$2$',
        'C': r'$\frac{3}{2}$',
        'D': r'$1$',
    },
    ('2024', 2): {
        'A': r'$\frac{1}{2}$',
        'B': r'$1$',
        'C': r'$\frac{3}{2}$',
        'D': r'$3$',
    },
    ('2024', 10): {
        'A': r'$\frac{\pi}{2}$',
        'B': r'$\frac{\pi}{3}$',
        'C': r'$\frac{\pi}{4}$',
        'D': r'$\frac{\pi}{6}$',
    },
}

# 2022-4题需要特殊处理，先查看题干
for q in questions:
    if str(q.get('year')) == '2022' and q.get('yearQnum') == 4:
        print(f"2022-4 题干: {q['question']}")
        print(f"2022-4 答案: {q['answer']}")
        print(f"2022-4 解析: {q['analysis'][:200]}")
        break

fixed_count = 0
for (year, qnum), fix in math_fixes.items():
    for q in questions:
        if str(q.get('year')) == year and q.get('yearQnum') == qnum:
            for key, value in fix.items():
                q[key] = value
            fixed_count += 1
            print(f"已修复 {year}-{qnum}")
            break

print(f"\n共修复 {fixed_count} 道数学题的选项")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# 统计剩余选项配图
remaining = 0
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        if '见本题选项配图' in q.get(field, ''):
            remaining += 1
            break
print(f"剩余选项配图题目: {remaining} 道")

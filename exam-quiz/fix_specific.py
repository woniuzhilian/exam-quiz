import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复特定题目
fixes = {
    # 2019-1: 极限题
    ('2019', 1): {
        'question': r'极限$\lim_{x \to 0} \frac{3+e^{1/x}}{1-e^{2/x}}$：（   ）。',
        'A': '值为3',
        'B': '值为-1',
        'C': '值为0',
        'D': '不存在',
        'analysis': r'用左右极限判别。当$x \to 0^-$时，$\frac{1}{x} \to -\infty$，$e^{1/x} \to 0$，$e^{2/x} \to 0$，故$\lim_{x \to 0^-} \frac{3+e^{1/x}}{1-e^{2/x}} = 3$。当$x \to 0^+$时，$\frac{1}{x} \to +\infty$，令$t=\frac{1}{x}$，则$\lim_{x \to 0^+} \frac{3+e^{1/x}}{1-e^{2/x}} = \lim_{t \to +\infty} \frac{3+e^t}{1-e^{2t}} = \lim_{t \to +\infty} \frac{e^t}{-2e^{2t}} = \lim_{t \to +\infty} \frac{1}{-2e^t} = 0$。左右极限不相等，故极限不存在，选D。'
    },
    # 2016-4: 向量题，修复选项B的$包裹
    ('2016', 4): {
        'B': r'$2\sqrt{2}$',
    },
    # 2014-9: 直线夹角题，选项应该是角度
    ('2014', 9): {
        'question': r'设有直线$L_1: \frac{x-1}{1} = \frac{y-2}{-2} = \frac{z-1}{1}$与$L_2: \begin{cases} x=2-t \\ y=1-t \\ z=1+2t \end{cases}$，则$L_1$与$L_2$的夹角$\theta$等于（   ）。',
        'A': r'$\frac{\pi}{2}$',
        'B': r'$\frac{\pi}{3}$',
        'C': r'$\frac{\pi}{4}$',
        'D': r'$\frac{\pi}{6}$',
        'analysis': r'直线间的夹角，内积公式的逆用。$L_1$的方向向量为$s_1=(1,-2,1)$，$L_2$的方向向量为$s_2=(-1,-1,2)$。由内积公式知$\cos\theta = \frac{|1 \times (-1)+(-2) \times (-1)+1 \times 2|}{\sqrt{1^2+(-2)^2+1^2} \cdot \sqrt{(-1)^2+(-1)^2+2^2}} = \frac{3}{\sqrt{6} \cdot \sqrt{6}} = \frac{1}{2}$，$\theta = \frac{\pi}{3}$，所以夹角$\theta = \frac{\pi}{3}$，选B。'
    },
}

for (year, qnum), fix in fixes.items():
    for q in questions:
        if str(q.get('year')) == year and q.get('yearQnum') == qnum:
            for key, value in fix.items():
                q[key] = value
            print(f"已修复 {year}-{qnum}")
            break

# 统计选项中包含"见本题选项配图"的题目
print("\n=== 选项包含'见本题选项配图'的题目统计 ===")
img_option_count = 0
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        if '见本题选项配图' in q.get(field, ''):
            img_option_count += 1
            break
print(f"共 {img_option_count} 道题的选项包含配图标记")

# 统计question中包含$但可能格式不对的
print("\n=== 公式格式问题统计 ===")
bad_formula = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        # 检查是否有未配对的$
        if text.count('$') % 2 != 0:
            bad_formula += 1
            print(f"  {q['year']}-{q.get('yearQnum', q['id'])} {field}: $数量为奇数")
            break
print(f"共 {bad_formula} 道题有$配对问题")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n修复完成")

import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 修复空字段的题目
fixes = {
    ('2021', 22): {  # 袋子里有5个白球
        'A': '$\\frac{1}{8}$',
        'B': '$\\frac{3}{8}$',
        'C': '$\\frac{5}{8}$',
        'D': '$\\frac{7}{8}$',
    },
    ('2021', 23): {  # 设X服从泊松分布P(3)
        'A': '3',
        'B': '$\\frac{1}{3}$',
        'C': '1',
        'D': '9',
    },
    ('2022', 58): {  # 将一刚度系数为k
        'A': 'K',
        'B': '2K',
        'C': '$\\frac{K}{2}$',
        'D': '$\\frac{1}{2K}$',
    },
    ('2022', 60): {  # 图示等截面直扞
        'A': '0',
        'B': '$\\frac{2FL}{EA}$',
        'C': '$\\frac{FL}{EA}$',
        'D': '$\\frac{FL}{2EA}$',
    },
}

for (year, qnum), options in fixes.items():
    q = next((x for x in public if x['year'] == year and x.get('yearQnum') == qnum), None)
    if q:
        print(f"修复 {year}-{qnum}:")
        for opt, val in options.items():
            old = q.get(opt, '')
            q[opt] = val
            print(f"  {opt}: '{old}' -> '{val}'")
    else:
        print(f"未找到 {year}-{qnum}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n题库已更新")

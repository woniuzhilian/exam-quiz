import json, re
from collections import defaultdict

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 数学相关小科目
math_subjects = ['微分学', '积分学', '概率论与数理统计', '气体动理论与热力学基础', 
                 '向量代数与空间解析几何', '无穷级数', '线性代数', '常微分方程']

# 找出数学题中选项包含配图的
math_img_questions = defaultdict(list)
for q in questions:
    if q.get('smallSubject') in math_subjects:
        has_img = False
        img_file = None
        for field in ['A', 'B', 'C', 'D']:
            match = re.search(r'【见本题选项配图[:：]([^】]+)】', q.get(field, ''))
            if match:
                has_img = True
                img_file = match.group(1)
                break
        if has_img:
            math_img_questions[img_file].append({
                'year': q['year'],
                'qnum': q.get('yearQnum', q['id']),
                'id': q['id'],
                'smallSubject': q['smallSubject'],
                'question': q['question'][:120],
                'answer': q['answer'],
                'A': q['A'][:60],
                'B': q['B'][:60],
                'C': q['C'][:60],
                'D': q['D'][:60],
            })

print(f"数学题选项配图的图片文件数: {len(math_img_questions)}")
print(f"数学题选项配图的题目数: {sum(len(v) for v in math_img_questions.values())}")

print("\n=== 按图片文件分组 ===")
for img_file, qs in sorted(math_img_questions.items()):
    print(f"\n{img_file}:")
    for q in qs:
        print(f"  {q['year']}-{q['qnum']} ({q['smallSubject']}) 答案={q['answer']}")
        print(f"    题干: {q['question'][:80]}")

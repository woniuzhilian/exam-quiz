import json, re, os

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2022-4题
for q in questions:
    if str(q.get('year')) == '2022' and q.get('yearQnum') == 4:
        q['question'] = r'设$y=\ln(1+x^2)$，则二阶导数$y''$等于（   ）。'
        q['A'] = r'$\frac{2(1+x^2)}{(1+x^2)^2}$'
        q['B'] = r'$\frac{2(1-x^2)}{(1+x^2)^2}$'
        q['C'] = r'$\frac{-2(1+x^2)}{(1+x^2)^2}$'
        q['D'] = r'$\frac{-2(1-x^2)}{(1+x^2)^2}$'
        q['analysis'] = r'复合函数求导法，高阶导数。$y\'=\frac{2x}{1+x^2}$，$y\'\'=\frac{2(1+x^2)-2x\cdot 2x}{(1+x^2)^2}=\frac{2(1-x^2)}{(1+x^2)^2}$，选B。'
        print("已修复2022-4")
        break

# 统计剩余选项配图题目按小科目分布
from collections import Counter
remaining = []
for q in questions:
    has_img = False
    img_file = None
    for field in ['A', 'B', 'C', 'D']:
        match = re.search(r'【见本题选项配图[:：]([^】]+)】', q.get(field, ''))
        if match:
            has_img = True
            img_file = match.group(1)
            break
    if has_img:
        remaining.append({
            'year': q['year'],
            'qnum': q.get('yearQnum', q['id']),
            'smallSubject': q.get('smallSubject', ''),
            'img_file': img_file,
        })

print(f"\n剩余选项配图题目: {len(remaining)} 道")
print(f"\n按小科目分布:")
for subj, count in Counter(r['smallSubject'] for r in remaining).most_common():
    print(f"  {subj or '(空)'}: {count}题")

# 检查这些题目的图片是否被多个选项引用
print(f"\n=== 图片引用情况 ===")
img_refs = Counter(r['img_file'] for r in remaining)
for img, count in img_refs.most_common(20):
    print(f"  {img}: 被{count}道题引用")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

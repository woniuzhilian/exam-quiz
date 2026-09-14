import json, re
from collections import Counter

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 检查专业基础
prof_questions = [q for q in data if q['bigSubject'] == '专业基础']
print(f"专业基础总题数: {len(prof_questions)}")

# 按年份统计
year_counts = Counter(q['year'] for q in prof_questions)
print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 检查专业基础的选项图片
prof_option_img = []
for q in prof_questions:
    for opt in ['A', 'B', 'C', 'D']:
        val = q.get(opt, '')
        if '<img' in val:
            prof_option_img.append(q)
            break

print(f"\n专业基础选项含图片的题目: {len(prof_option_img)}道")

# 检查是否有多个选项使用同一张图片
same_img = 0
for q in prof_option_img:
    imgs = []
    for opt in ['A', 'B', 'C', 'D']:
        val = q.get(opt, '')
        m = re.search(r'<img[^>]+src="/images/([^"]+)"', val)
        if m:
            imgs.append(m.group(1))
    if len(imgs) > 1 and len(set(imgs)) == 1:
        same_img += 1

print(f"专业基础多个选项同一张图: {same_img}道")

# 检查专业基础每年的前3题
print(f"\n专业基础各年前3题:")
for year in sorted(year_counts.keys()):
    yq = [q for q in prof_questions if q['year'] == year]
    print(f"\n  {year}年（{len(yq)}题）:")
    for q in yq[:3]:
        print(f"    id={q['id']}, [{q['smallSubject']}], {q['question'][:50]}")

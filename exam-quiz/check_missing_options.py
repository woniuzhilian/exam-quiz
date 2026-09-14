import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查看2013年63和64题
year_2013 = [q for q in questions if q['year'] == '2013' and q['bigSubject'] == '公共基础']
year_2013_sorted = sorted(year_2013, key=lambda x: x.get('yearQnum', 0))

for qnum in [62, 63, 64, 65]:
    q = next((q for q in year_2013_sorted if q.get('yearQnum') == qnum), None)
    if q:
        print(f"\n2013-{qnum}:")
        print(f"  题干: {q.get('question', '')[:120]}")
        print(f"  选项A: {q.get('A', '')[:60]}")
        print(f"  答案: {q.get('answer', '')}")
    else:
        print(f"\n2013-{qnum}: 未找到")

# 统计选项内容缺失的题目
print("\n\n选项内容缺失的题目统计:")
missing_options = []
for q in questions:
    for field in ['A', 'B', 'C', 'D']:
        text = q.get(field, '')
        if text in ['选项A', '选项B', '选项C', '选项D', 'A', 'B', 'C', 'D', '']:
            # 排除选项配图合并的情况
            if q.get('A') and '<img' in q.get('A', ''):
                continue
            missing_options.append((q['year'], q.get('yearQnum', q['id']), q['bigSubject'], field))
            break

print(f"共 {len(missing_options)} 道题选项内容缺失")
# 按年份统计
from collections import Counter
year_counts = Counter([f"{y}-{s}" for y, q, s, f in missing_options])
for year_subject, count in sorted(year_counts.items()):
    print(f"  {year_subject}: {count} 道")

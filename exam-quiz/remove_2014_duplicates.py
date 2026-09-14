import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 分离公共基础和专业基础
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

print(f"原专业基础题数: {len(pro)}")

# 删除2014年的题
pro = [q for q in pro if q['year'] != '2014']
print(f"删除2014年后: {len(pro)}")

# 删除2024年的重复题（保留第一个）
seen_2024 = set()
new_pro = []
for q in pro:
    if q['year'] == '2024':
        qnum = q.get('yearQnum')
        if qnum in seen_2024:
            print(f"删除重复: 2024-{qnum}")
            continue
        seen_2024.add(qnum)
    new_pro.append(q)
pro = new_pro
print(f"删除2024重复后: {len(pro)}")

# 重新分配id
for i, q in enumerate(pro):
    q['id'] = 1434 + i

# 合并
final = public + pro
print(f"最终题库题数: {len(final)}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("已保存")

# 统计各年份
from collections import Counter
year_counts = Counter(q['year'] for q in pro)
print("\n各年份题数:")
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]}")

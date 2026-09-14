import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查看专业基础2016年前10道题
print("=== 专业基础2016年前10道题 ===")
count = 0
for q in questions:
    if q['bigSubject'] == '专业基础' and q['year'] == '2016':
        print(f"\n--- 2016-{q.get('yearQnum')} (id={q['id']}) ---")
        print(f"smallSubject: {q['smallSubject']}")
        print(f"question: {q['question'][:80]}...")
        print(f"answer: {q['answer']}")
        count += 1
        if count >= 10:
            break

# 统计专业基础各年份题目数
print("\n=== 专业基础各年份题目数 ===")
year_counts = {}
for q in questions:
    if q['bigSubject'] == '专业基础':
        year = q['year']
        year_counts[year] = year_counts.get(year, 0) + 1
for year in sorted(year_counts.keys()):
    print(f"{year}: {year_counts[year]}题")

import json

with open(r'D:\应用程序开发\刷题\exam-quiz\prof_blank_questions.json', 'r', encoding='utf-8') as f:
    blank_questions = json.load(f)

# 检查2022年的题目
q2022 = [q for q in blank_questions if q['year'] == '2022']
print(f"2022年共{len(q2022)}题")
print(f"题号范围: {min(q['qnum'] for q in q2022)} - {max(q['qnum'] for q in q2022)}")

# 检查是否有重复题号
qnums = [q['qnum'] for q in q2022]
from collections import Counter
qnum_counts = Counter(qnums)
duplicates = {k: v for k, v in qnum_counts.items() if v > 1}
print(f"重复题号: {duplicates}")

# 显示前5题和后5题
print(f"\n前5题:")
for q in sorted(q2022, key=lambda x: x['qnum'])[:5]:
    print(f"  {q['qnum']}: {q['question'][:50]}")

print(f"\n后5题:")
for q in sorted(q2022, key=lambda x: x['qnum'])[-5:]:
    print(f"  {q['qnum']}: {q['question'][:50]}")

# 检查第60题和第61题
print(f"\n第60题:")
for q in q2022:
    if q['qnum'] == 60:
        print(f"  {q['question'][:80]}")

print(f"\n第61题:")
for q in q2022:
    if q['qnum'] == 61:
        print(f"  {q['question'][:80]}")

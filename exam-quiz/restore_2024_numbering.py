import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

pro = [q for q in questions if q['bigSubject'] == '专业基础']
public = [q for q in questions if q['bigSubject'] == '公共基础']

# 恢复2024年题号：将13-56都加4，变回17-60
year_2024 = [q for q in pro if q['year'] == '2024']
for q in year_2024:
    old_qnum = q.get('yearQnum', 0)
    if old_qnum >= 13:
        new_qnum = old_qnum + 4
        q['yearQnum'] = new_qnum
        print(f"  {old_qnum} -> {new_qnum}")

# 重新排序和分配id
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 验证
year_2024_new = [q for q in pro if q['year'] == '2024']
year_2024_new_sorted = sorted(year_2024_new, key=lambda x: x.get('yearQnum', 0))
qnums = [q.get('yearQnum') for q in year_2024_new_sorted]
print(f"\n2024年题号范围: {min(qnums)} - {max(qnums)}")
print(f"2024年题数: {len(year_2024_new)}")
print(f"缺少的题号: {[n for n in range(1, 61) if n not in qnums]}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("\n题库已更新")

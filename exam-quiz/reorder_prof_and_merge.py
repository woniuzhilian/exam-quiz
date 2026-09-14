import json
from collections import defaultdict

# 读取匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\prof_id_to_qnum.json', 'r', encoding='utf-8') as f:
    id_to_qnum = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    all_questions = json.load(f)

prof_bank = [q for q in all_questions if q['bigSubject'] == '专业基础']

# 按年份分组
prof_by_year = defaultdict(list)
for q in prof_bank:
    prof_by_year[q['year']].append(q)

new_prof = []
new_id = 1

for year in sorted(prof_by_year.keys()):
    year_questions = prof_by_year[year]

    if year == '2024':
        # 2024年无法匹配，保持原顺序
        for q in year_questions:
            q['id'] = new_id
            new_prof.append(q)
            new_id += 1
        print(f"  {year}: 保持原顺序 {len(year_questions)}题")
        continue

    # 分离匹配成功和未匹配的
    matched = []
    unmatched = []
    for q in year_questions:
        qid_str = str(q['id'])
        if qid_str in id_to_qnum:
            actual_year, actual_qnum = id_to_qnum[qid_str]
            if actual_year == year:
                matched.append((actual_qnum, q))
            else:
                unmatched.append(q)
        else:
            unmatched.append(q)

    # 按实际题号排序
    matched.sort(key=lambda x: x[0])

    # 重新分配id
    for actual_qnum, q in matched:
        q['id'] = new_id
        new_prof.append(q)
        new_id += 1

    # 未匹配的放在末尾
    for q in unmatched:
        q['id'] = new_id
        new_prof.append(q)
        new_id += 1

    print(f"  {year}: 匹配{len(matched)}题, 未匹配{len(unmatched)}题")

print(f"\n专业基础重新排序完成: {len(new_prof)}题")

# 读取公共基础
with open(r'D:\应用程序开发\刷题\exam-quiz\pub_final.json', 'r', encoding='utf-8') as f:
    pub_questions = json.load(f)

# 公共基础id已经是1-1433
# 专业基础id从1434开始
for q in new_prof:
    q['id'] = q['id'] + len(pub_questions)

# 合并
final_all = pub_questions + new_prof

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final_all, f, ensure_ascii=False, indent=2)

print(f"\n最终题库: {len(final_all)}题")
print(f"公共基础: {len(pub_questions)}题 (id 1-{len(pub_questions)})")
print(f"专业基础: {len(new_prof)}题 (id {len(pub_questions)+1}-{len(final_all)})")

# 验证2014-9题（公共基础）
print(f"\n验证公共基础2014-9题:")
for q in pub_questions:
    if q['year'] == '2014' and q['id'] == 129:
        print(f"  id={q['id']}, smallSubject={q['smallSubject']}")
        print(f"  question={q['question'][:60]}")
        print(f"  answer={q['answer']}")
        break

import json
from collections import defaultdict

# 读取匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'r', encoding='utf-8') as f:
    id_to_qnum = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    all_questions = json.load(f)

# 分离公共基础和专业基础
pub_questions = [q for q in all_questions if q['bigSubject'] == '公共基础']
prof_questions = [q for q in all_questions if q['bigSubject'] == '专业基础']

print(f"公共基础: {len(pub_questions)}题")
print(f"专业基础: {len(prof_questions)}题")

# 重新排序公共基础
pub_by_year = defaultdict(list)
for q in pub_questions:
    pub_by_year[q['year']].append(q)

new_pub = []
new_id = 1

for year in sorted(pub_by_year.keys()):
    year_questions = pub_by_year[year]

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
        new_pub.append(q)
        new_id += 1

    # 未匹配的放在末尾，保持原顺序
    for q in unmatched:
        q['id'] = new_id
        new_pub.append(q)
        new_id += 1

    print(f"  {year}: 匹配{len(matched)}题, 未匹配{len(unmatched)}题")

# 合并
new_all = new_pub + prof_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(new_all, f, ensure_ascii=False, indent=2)

print(f"\n重新排序完成: {len(new_all)}题")
print(f"公共基础id范围: 1-{len(new_pub)}")
print(f"专业基础id范围: {len(new_pub)+1}-{len(new_all)}")

# 验证2014年的前10题
print(f"\n2014年前10题:")
count = 0
for q in new_pub:
    if q['year'] == '2014':
        count += 1
        if count <= 10:
            print(f"  id={q['id']}, [{q['smallSubject']}], {q['question'][:50]}")

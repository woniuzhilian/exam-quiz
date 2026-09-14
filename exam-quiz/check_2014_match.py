import json

# 读取匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'r', encoding='utf-8') as f:
    id_to_qnum = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    all_questions = json.load(f)

# 查找2014年"设有直线L"的题目
print("=== 查找2014年'设有直线L'的题目 ===")
for q in all_questions:
    if q['bigSubject'] == '公共基础' and q['year'] == '2014' and '直线' in q['question'] and '夹角' in q['question']:
        print(f"  id={q['id']}, question={q['question'][:80]}")
        qid_str = str(q['id'])
        if qid_str in id_to_qnum:
            print(f"  匹配到实际题号: {id_to_qnum[qid_str]}")
        else:
            print(f"  未匹配")

# 检查2014年匹配成功的题号分布
print("\n=== 2014年匹配成功的题号 ===")
matched_2014 = []
for qid_str, (year, qnum) in id_to_qnum.items():
    if year == '2014':
        matched_2014.append(qnum)

matched_2014.sort()
print(f"共{len(matched_2014)}题匹配成功")
print(f"题号: {matched_2014}")

# 检查哪些题号缺失
all_nums = set(range(1, 121))
matched_set = set(matched_2014)
missing = sorted(all_nums - matched_set)
print(f"\n缺失的题号({len(missing)}个): {missing}")

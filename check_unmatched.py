import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\应用程序开发\刷题\prof_questions_parsed.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)
with open(r'D:\应用程序开发\刷题\prof_answers_parsed.json', 'r', encoding='utf-8') as f:
    ans = json.load(f)

# 找未匹配的题目
for q in qs:
    key = f"{q['year']}-{q['_qnum']}"
    if key in ['2018-19', '2017-40', '2022补-41']:
        print(f"题目: id={q['id']}, key={key}, page={q['_page']}")
        print(f"  题干: {q['question'][:80]}")

print()
# 找答案中类似的题号
for k in ans.keys():
    if '2018' in k and '19' in k:
        print(f"答案中有: {k}")
    if '2017' in k and '40' in k:
        print(f"答案中有: {k}")
    if '2022' in k and '41' in k:
        print(f"答案中有: {k}")

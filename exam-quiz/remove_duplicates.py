import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查重复
seen = {}
duplicates = []
for i, q in enumerate(questions):
    key = (q['bigSubject'], q['year'], q.get('yearQnum', q['id']))
    if key in seen:
        duplicates.append((i, key, q['question'][:50]))
    else:
        seen[key] = i

print(f"重复题目: {len(duplicates)} 道")
for idx, key, q in duplicates:
    print(f"  索引{idx}: {key} - {q}")

# 删除重复（保留第一个）
to_remove = set([d[0] for d in duplicates])
questions = [q for i, q in enumerate(questions) if i not in to_remove]

# 重新编号
pub_questions = [q for q in questions if q['bigSubject'] == '公共基础']
prof_questions = [q for q in questions if q['bigSubject'] == '专业基础']

for i, q in enumerate(pub_questions):
    q['id'] = i + 1
for i, q in enumerate(prof_questions):
    q['id'] = len(pub_questions) + i + 1

questions = pub_questions + prof_questions

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"\n去重后题库: {len(questions)} 题")
print(f"公共基础: {len(pub_questions)} 题, 专业基础: {len(prof_questions)} 题")

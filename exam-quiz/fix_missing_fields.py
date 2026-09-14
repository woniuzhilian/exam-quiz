import json

# 读取新题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"总题目数量: {len(questions)}")

# 检查缺少bigSubject的题目
missing_bigSubject = []
for i, q in enumerate(questions):
    if 'bigSubject' not in q:
        missing_bigSubject.append((i, q))
        print(f"第{i}题缺少bigSubject: {list(q.keys())}")
        print(f"  内容: {str(q)[:100]}")

print(f"\n缺少bigSubject的题目数量: {len(missing_bigSubject)}")

# 修复缺少bigSubject的题目
for i, q in missing_bigSubject:
    if i < 1433:
        q['bigSubject'] = '公共基础'
    else:
        q['bigSubject'] = '专业基础'

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("已修复缺少bigSubject的题目")

# 重新统计
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

print(f"公共基础: {len(public)}道")
print(f"专业基础: {len(pro)}道")

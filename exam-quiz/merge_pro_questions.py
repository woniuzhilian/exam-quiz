import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

print(f"题目数量: {len(questions)}")
print(f"答案解析数量: {len(answers)}")

# 合并题目和答案解析
merged = []
missing_answers = []

for q in questions:
    # 构建题号key
    key = f"{q['year']}-{q['yearQnum']}"
    
    # 查找答案解析
    if key in answers:
        ans = answers[key]
        q['answer'] = ans['answer']
        q['analysis'] = ans['analysis']
    else:
        missing_answers.append(key)
        q['answer'] = ""
        q['analysis'] = ""
    
    merged.append(q)

print(f"合并后题目数量: {len(merged)}")
print(f"缺少答案解析的题目: {missing_answers}")

# 读取原题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    original = json.load(f)

print(f"原题库题目数量: {len(original)}")

# 分离公共基础和专业基础
public_questions = [q for q in original if q['bigSubject'] == '公共基础']
pro_questions = [q for q in original if q['bigSubject'] == '专业基础']

print(f"公共基础题目数量: {len(public_questions)}")
print(f"原专业基础题目数量: {len(pro_questions)}")

# 重新分配专业基础的id（从1434开始）
for i, q in enumerate(merged):
    q['id'] = 1434 + i

# 合并
final = public_questions + merged

print(f"最终题库题目数量: {len(final)}")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print("题库已更新")

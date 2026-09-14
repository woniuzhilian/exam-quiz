import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查匹配失败的题目（smallSubject为空）
unmatched = [q for q in questions if not q.get('smallSubject')]
print(f"匹配失败题目: {len(unmatched)} 道")

# 检查这些题目的题干和解析是否有意义
print("\n=== 匹配失败题目检查 ===")
bad_questions = []
for q in unmatched:
    year_qnum = f"{q['year']}-{q.get('yearQnum', q['id'])}"
    question = q['question']
    analysis = q['analysis']
    
    # 检查题干是否包含明显乱码
    issues = []
    
    # 检查$配对
    if question.count('$') % 2 != 0:
        issues.append('题干$不配对')
    if analysis.count('$') % 2 != 0:
        issues.append('解析$不配对')
    
    # 检查是否包含零散的数学符号（可能是公式乱码）
    if re.search(r'[;][a-z]', question) and '\\' not in question:
        issues.append('题干可能含乱码公式')
    
    # 检查题干长度
    if len(question) < 10:
        issues.append('题干过短')
    
    if issues:
        bad_questions.append({
            'year_qnum': year_qnum,
            'id': q['id'],
            'issues': issues,
            'question': question[:100],
            'analysis': analysis[:100],
        })

print(f"有问题的匹配失败题目: {len(bad_questions)} 道")
for bq in bad_questions[:20]:
    print(f"\n{bq['year_qnum']} (id={bq['id']}): {', '.join(bq['issues'])}")
    print(f"  题干: {bq['question']}")
    print(f"  解析: {bq['analysis']}")

# 检查所有题目的$配对问题
print("\n=== 所有题目$配对检查 ===")
dollar_issues = []
for q in questions:
    year_qnum = f"{q['year']}-{q.get('yearQnum', q['id'])}"
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if text.count('$') % 2 != 0:
            dollar_issues.append(f"{year_qnum} {field}: $数量={text.count('$')}")

print(f"$不配对的字段: {len(dollar_issues)} 个")
for di in dollar_issues[:20]:
    print(f"  {di}")

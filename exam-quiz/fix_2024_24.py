import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2024-24的选项D
for q in questions:
    if str(q.get('year')) == '2024' and q.get('yearQnum') == 24:
        print(f"修复前 D: {q['D']}")
        # 移除多余的$
        q['D'] = q['D'].replace('$', '')
        print(f"修复后 D: {q['D']}")
        break

# 列出68道匹配失败的题目
unmatched = [q for q in questions if not q.get('smallSubject')]
print(f"\n=== 匹配失败题目清单（共{len(unmatched)}道，可能需要手动修复公式）===")
for q in unmatched:
    year_qnum = f"{q['year']}-{q.get('yearQnum', q['id'])}"
    print(f"  {year_qnum}: {q['question'][:60]}...")

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n修复完成")

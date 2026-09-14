import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 找出smallSubject为空的题目（匹配失败的）
unmatched = [q for q in questions if not q.get('smallSubject')]
print(f"匹配失败题目数: {len(unmatched)}")

# 定义特殊公式字符
special_chars = set()
for q in unmatched:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        for ch in text:
            if ord(ch) > 127 and not ('\u4e00' <= ch <= '\u9fff'):
                special_chars.add(ch)

print(f"\n特殊字符列表:")
for ch in sorted(special_chars):
    print(f"  {ch} (U+{ord(ch):04X})")

# 输出前10道题的完整内容
print("\n=== 前10道匹配失败题目 ===")
for i, q in enumerate(unmatched[:10]):
    print(f"\n--- {q['year']}-{q.get('yearQnum', q['id'])} ---")
    print(f"question: {q['question'][:200]}")
    print(f"A: {q['A'][:100]}")
    print(f"B: {q['B'][:100]}")
    print(f"analysis: {q['analysis'][:150]}")

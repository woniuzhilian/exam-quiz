import json, re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 检查匹配失败的题目（smallSubject为空）
unmatched = [q for q in questions if not q['smallSubject']]
print(f"匹配失败题目: {len(unmatched)}")

# 检查这些题目的公式和图片情况
has_raw_formula = 0
has_img_tag = 0
has_pdf_ref = 0
has_img_marker = 0

for q in unmatched:
    text = q['question'] + q['A'] + q['B'] + q['C'] + q['D']
    # 检查是否有原始公式字符（如𝑥, 𝑦, 𝛼等特殊字符）
    if re.search(r'[𝑥𝑦𝑧𝛼𝛽𝛾𝜃𝜋∫∑√]', text):
        has_raw_formula += 1
    # 检查是否有img标签
    if '<img' in text:
        has_img_tag += 1
    # 检查是否有PDF引用
    if 'PDF' in text or 'pdf' in text or '见' in text and '页' in text:
        has_pdf_ref += 1
    # 检查是否有配图标记
    if '配图' in text or '图' in text and '[' in text:
        has_img_marker += 1

print(f"\n匹配失败题目统计:")
print(f"  含原始公式字符: {has_raw_formula}")
print(f"  含img标签: {has_img_tag}")
print(f"  含PDF引用: {has_pdf_ref}")
print(f"  含配图标记: {has_img_marker}")

# 显示一些例子
print(f"\n前5个匹配失败题目的题干:")
for q in unmatched[:5]:
    print(f"\n  {q['year']}-{q['yearQnum']}:")
    print(f"    question: {q['question'][:100]}")
    print(f"    A: {q['A'][:50]}")
    print(f"    B: {q['B'][:50]}")

# 检查所有题目中是否有"见PDF"或"配图"标记
print(f"\n\n所有题目中含'见PDF'或'配图'标记的:")
for q in questions:
    text = q['question']
    if '见PDF' in text or '配图' in text or '本题配图' in text:
        print(f"  {q['bigSubject']} {q['year']}-{q['yearQnum']}: {text[:80]}")

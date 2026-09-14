import json, re

# 读取PDF提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_questions_raw.json', 'r', encoding='utf-8') as f:
    pdf_questions = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    bank_questions = json.load(f)

# 只处理公共基础
pub_bank = [q for q in bank_questions if q['bigSubject'] == '公共基础']
print(f"题库公共基础: {len(pub_bank)}题")
print(f"PDF提取: {len(pdf_questions)}题")

# 建立PDF题目的索引：用题干的前20个字符作为key
def normalize(text):
    """标准化文本用于匹配"""
    text = re.sub(r'\s+', '', text)  # 去空格
    text = re.sub(r'[\$]', '', text)  # 去$符号
    text = re.sub(r'[（）()]', '', text)  # 去括号
    return text[:30]

pdf_index = {}
for q in pdf_questions:
    key = normalize(q['question'])
    if key and key not in pdf_index:
        pdf_index[key] = q

# 匹配题库题目
matched = 0
unmatched = []
match_results = []

for q in pub_bank:
    key = normalize(q['question'])
    if key in pdf_index:
        pdf_q = pdf_index[key]
        match_results.append({
            'bank_id': q['id'],
            'bank_year': q['year'],
            'actual_year': pdf_q['year'],
            'actual_qnum': pdf_q['qnum'],
            'question': q['question'][:50]
        })
        matched += 1
    else:
        unmatched.append(q)

print(f"\n匹配成功: {matched}/{len(pub_bank)}")
print(f"未匹配: {len(unmatched)}")

# 显示一些匹配结果
print(f"\n匹配结果示例（前10个）:")
for r in match_results[:10]:
    print(f"  题库id={r['bank_id']} ({r['bank_year']}) -> 实际题号 {r['actual_year']}-{r['actual_qnum']}: {r['question']}")

# 显示未匹配的题目
print(f"\n未匹配题目示例（前10个）:")
for q in unmatched[:10]:
    print(f"  id={q['id']} ({q['year']}) [{q['smallSubject']}]: {q['question'][:60]}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\match_results.json', 'w', encoding='utf-8') as f:
    json.dump(match_results, f, ensure_ascii=False, indent=2)

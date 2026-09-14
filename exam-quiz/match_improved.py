import json, re
from collections import defaultdict

# 读取PDF提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_questions_raw.json', 'r', encoding='utf-8') as f:
    pdf_questions = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    bank_questions = json.load(f)

pub_bank = [q for q in bank_questions if q['bigSubject'] == '公共基础']

def normalize(text):
    if not text:
        return ''
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[\$]', '', text)
    text = re.sub(r'[（）()]', '', text)
    return text

# 建立PDF题目的多种索引
pdf_by_year = defaultdict(list)
for q in pdf_questions:
    pdf_by_year[q['year']].append(q)

# 改进匹配：先按年份分组，然后用题干+选项匹配
matched = {}
unmatched = []

for bank_q in pub_bank:
    year = bank_q['year']
    if year not in pdf_by_year:
        unmatched.append(bank_q)
        continue

    candidates = pdf_by_year[year]
    best_match = None
    best_score = 0

    bank_q_norm = normalize(bank_q['question'])
    bank_opts_norm = {opt: normalize(bank_q.get(opt, '')) for opt in ['A', 'B', 'C', 'D']}

    for pdf_q in candidates:
        if (pdf_q['year'], pdf_q['qnum']) in matched.values():
            continue  # 已经被匹配过了

        score = 0
        pdf_q_norm = normalize(pdf_q['question'])

        # 题干匹配：检查是否有共同的子串
        if bank_q_norm and pdf_q_norm:
            # 取较短的前15个字符
            min_len = min(len(bank_q_norm), len(pdf_q_norm), 15)
            if min_len > 5:
                common = 0
                for i in range(min_len):
                    if bank_q_norm[i] == pdf_q_norm[i]:
                        common += 1
                score += common / min_len * 3

        # 选项匹配
        for opt in ['A', 'B', 'C', 'D']:
            bank_opt = bank_opts_norm[opt]
            pdf_opt = normalize(pdf_q['options'].get(opt, ''))
            if bank_opt and pdf_opt:
                min_len = min(len(bank_opt), len(pdf_opt), 10)
                if min_len > 3:
                    common = sum(1 for i in range(min_len) if bank_opt[i] == pdf_opt[i])
                    score += common / min_len

        if score > best_score:
            best_score = score
            best_match = pdf_q

    # 阈值：分数大于2认为匹配成功
    if best_match and best_score > 1.5:
        matched[bank_q['id']] = (best_match['year'], best_match['qnum'])
    else:
        unmatched.append(bank_q)

print(f"匹配成功: {len(matched)}/{len(pub_bank)}")
print(f"未匹配: {len(unmatched)}")

# 检查每年的匹配情况
for year in sorted(pdf_by_year.keys()):
    year_matched = sum(1 for v in matched.values() if v[0] == year)
    print(f"  {year}: 匹配{year_matched}/{len(pdf_by_year[year])}")

# 显示未匹配的题目
print(f"\n未匹配题目（前20个）:")
for q in unmatched[:20]:
    print(f"  id={q['id']} ({q['year']}) [{q['smallSubject']}]: {q['question'][:50]}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存到 id_to_qnum.json")

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

# 按年份分组
bank_by_year = defaultdict(list)
for q in pub_bank:
    bank_by_year[q['year']].append(q)

pdf_by_year = defaultdict(list)
for q in pdf_questions:
    pdf_by_year[q['year']].append(q)

# 最终匹配结果
final_matched = {}  # bank_id -> (year, qnum)

for year in sorted(bank_by_year.keys()):
    bank_year = bank_by_year[year]
    pdf_year = pdf_by_year.get(year, [])

    if not pdf_year:
        continue

    # 第一步：内容匹配，确定每道PDF题目的小科目
    unmatched_bank = list(bank_year)
    pdf_subject = {}  # pdf_qnum -> subject

    for pdf_q in pdf_year:
        pdf_q_norm = normalize(pdf_q['question'])
        best_match = None
        best_score = 0
        best_idx = -1

        for i, bank_q in enumerate(unmatched_bank):
            score = 0
            bank_q_norm = normalize(bank_q['question'])

            if bank_q_norm and pdf_q_norm:
                min_len = min(len(bank_q_norm), len(pdf_q_norm), 25)
                if min_len > 5:
                    common = sum(1 for j in range(min_len) if bank_q_norm[j] == pdf_q_norm[j])
                    score += common / min_len * 4

            for opt in ['A', 'B', 'C', 'D']:
                bank_opt = normalize(bank_q.get(opt, ''))
                pdf_opt = normalize(pdf_q['options'].get(opt, ''))
                if bank_opt and pdf_opt:
                    min_len = min(len(bank_opt), len(pdf_opt), 15)
                    if min_len > 3:
                        common = sum(1 for j in range(min_len) if bank_opt[j] == pdf_opt[j])
                        score += common / min_len * 2

            if score > best_score:
                best_score = score
                best_match = bank_q
                best_idx = i

        if best_match and best_score > 2.0:
            final_matched[best_match['id']] = (year, pdf_q['qnum'])
            pdf_subject[pdf_q['qnum']] = best_match['smallSubject']
            unmatched_bank.pop(best_idx)

    # 第二步：按小科目分组未匹配的题库题目
    unmatched_by_subject = defaultdict(list)
    for q in unmatched_bank:
        unmatched_by_subject[q['smallSubject']].append(q)

    # 第三步：对每个小科目，找到PDF中该小科目的题号范围
    # 然后将未匹配的题库题目按顺序填入空缺的题号
    for subject, bank_qs in unmatched_by_subject.items():
        # 找到该小科目已匹配的PDF题号
        subject_qnums = [qnum for qnum, subj in pdf_subject.items() if subj == subject]

        if not subject_qnums:
            # 没有匹配到该小科目，尝试通过相邻题目推断
            continue

        min_qnum = min(subject_qnums)
        max_qnum = max(subject_qnums)

        # 找到该范围内所有PDF题目
        range_qs = [q for q in pdf_year if min_qnum <= q['qnum'] <= max_qnum]
        matched_qnums = set(subject_qnums)
        missing_qs = sorted([q for q in range_qs if q['qnum'] not in matched_qnums],
                           key=lambda x: x['qnum'])

        # 按顺序匹配
        for i, bank_q in enumerate(bank_qs):
            if i < len(missing_qs):
                final_matched[bank_q['id']] = (year, missing_qs[i]['qnum'])

print(f"匹配成功: {len(final_matched)}/{len(pub_bank)}")
print(f"未匹配: {len(pub_bank) - len(final_matched)}")

# 按年份统计
for year in sorted(bank_by_year.keys()):
    year_matched = sum(1 for v in final_matched.values() if v[0] == year)
    year_total = len(bank_by_year[year])
    print(f"  {year}: 匹配{year_matched}/{year_total}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in final_matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存")

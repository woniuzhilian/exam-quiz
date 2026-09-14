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

# 方法：按年份+小科目分组，然后按顺序匹配
# 因为题目PDF和题库都是按小科目顺序排列的

# 首先需要确定PDF中每道题属于哪个小科目
# 可以通过题干内容与题库中小科目的题目匹配来确定

# 按年份分组
bank_by_year = defaultdict(list)
for q in pub_bank:
    bank_by_year[q['year']].append(q)

pdf_by_year = defaultdict(list)
for q in pdf_questions:
    pdf_by_year[q['year']].append(q)

# 对每一年，按小科目顺序匹配
# 题库中的题目按小科目分组，保持原顺序
# PDF中的题目也按出现顺序（即小科目顺序）

matched = {}  # bank_id -> (year, qnum)

for year in sorted(bank_by_year.keys()):
    bank_year = bank_by_year[year]
    pdf_year = pdf_by_year.get(year, [])

    if not pdf_year:
        continue

    # 题库按小科目分组
    bank_by_subject = defaultdict(list)
    for q in bank_year:
        bank_by_subject[q['smallSubject']].append(q)

    # PDF题目按出现顺序，尝试匹配到对应的小科目
    # 方法：对每道PDF题目，找到最匹配的题库题目（未匹配过的）
    # 然后根据该题库题目的小科目，确定PDF题目的小科目

    unmatched_bank = list(bank_year)
    pdf_with_subject = []

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
            matched[best_match['id']] = (pdf_q['year'], pdf_q['qnum'])
            pdf_with_subject.append((pdf_q, best_match['smallSubject']))
            unmatched_bank.pop(best_idx)
        else:
            pdf_with_subject.append((pdf_q, None))

    # 对于未匹配的题库题目，根据小科目和位置推断题号
    # 按小科目分组未匹配的题库题目
    unmatched_by_subject = defaultdict(list)
    for q in unmatched_bank:
        unmatched_by_subject[q['smallSubject']].append(q)

    # 对于每个小科目，找到PDF中该小科目的题号范围
    # 然后将未匹配的题库题目按顺序填入空缺的题号
    for subject, bank_qs in unmatched_by_subject.items():
        # 找到该小科目已匹配的PDF题号
        subject_qnums = [qnum for (pdf_q, subj) in pdf_with_subject
                        if subj == subject for qnum in [pdf_q['qnum']]]
        subject_qs = [pdf_q for (pdf_q, subj) in pdf_with_subject if subj == subject]

        if not subject_qs:
            continue

        # 找到该小科目在PDF中的题号范围
        min_qnum = min(q['qnum'] for q in subject_qs)
        max_qnum = max(q['qnum'] for q in subject_qs)

        # 找到空缺的题号
        all_qs = [q for q in pdf_year if min_qnum <= q['qnum'] <= max_qnum]
        matched_qs = set(q['qnum'] for q in subject_qs)
        missing_qs = [q for q in all_qs if q['qnum'] not in matched_qs]

        # 按顺序匹配
        for i, bank_q in enumerate(bank_qs):
            if i < len(missing_qs):
                matched[bank_q['id']] = (year, missing_qs[i]['qnum'])

print(f"匹配成功: {len(matched)}/{len(pub_bank)}")
print(f"未匹配: {len(pub_bank) - len(matched)}")

# 按年份统计
for year in sorted(bank_by_year.keys()):
    year_matched = sum(1 for v in matched.values() if v[0] == year)
    year_total = len(bank_by_year[year])
    print(f"  {year}: 匹配{year_matched}/{year_total}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存")

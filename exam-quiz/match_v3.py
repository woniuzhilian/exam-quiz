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

# 按年份+小科目分组题库
bank_by_year_subject = defaultdict(list)
for q in pub_bank:
    key = (q['year'], q['smallSubject'])
    bank_by_year_subject[key].append(q)

# 按年份分组PDF题目
pdf_by_year = defaultdict(list)
for q in pdf_questions:
    pdf_by_year[q['year']].append(q)

# 为每道PDF题目匹配小科目和题库题目
# 方法：按年份遍历PDF题目，根据题干内容匹配到对应小科目的题库题目

matched = {}  # bank_id -> (year, qnum)
unmatched_bank = set(q['id'] for q in pub_bank)

for year in sorted(pdf_by_year.keys()):
    pdf_year = pdf_by_year[year]
    # 获取该年份所有小科目的题库题目
    bank_year = [q for q in pub_bank if q['year'] == year]

    for pdf_q in pdf_year:
        pdf_q_norm = normalize(pdf_q['question'])

        best_match = None
        best_score = 0

        for bank_q in bank_year:
            if bank_q['id'] not in unmatched_bank:
                continue

            score = 0
            bank_q_norm = normalize(bank_q['question'])

            # 题干匹配
            if bank_q_norm and pdf_q_norm:
                min_len = min(len(bank_q_norm), len(pdf_q_norm), 25)
                if min_len > 5:
                    common = sum(1 for i in range(min_len) if bank_q_norm[i] == pdf_q_norm[i])
                    score += common / min_len * 4

            # 选项匹配
            for opt in ['A', 'B', 'C', 'D']:
                bank_opt = normalize(bank_q.get(opt, ''))
                pdf_opt = normalize(pdf_q['options'].get(opt, ''))
                if bank_opt and pdf_opt:
                    min_len = min(len(bank_opt), len(pdf_opt), 15)
                    if min_len > 3:
                        common = sum(1 for i in range(min_len) if bank_opt[i] == pdf_opt[i])
                        score += common / min_len * 2

            if score > best_score:
                best_score = score
                best_match = bank_q

        if best_match and best_score > 2.0:
            matched[best_match['id']] = (pdf_q['year'], pdf_q['qnum'])
            unmatched_bank.remove(best_match['id'])

print(f"匹配成功: {len(matched)}/{len(pub_bank)}")
print(f"未匹配: {len(unmatched_bank)}")

# 按年份统计
for year in sorted(pdf_by_year.keys()):
    year_matched = sum(1 for v in matched.values() if v[0] == year)
    year_total = len([q for q in pub_bank if q['year'] == year])
    print(f"  {year}: 匹配{year_matched}/{year_total}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存")

import json, re
from collections import defaultdict

# 读取空白卷提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\prof_blank_questions.json', 'r', encoding='utf-8') as f:
    blank_questions = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    bank_questions = json.load(f)

prof_bank = [q for q in bank_questions if q['bigSubject'] == '专业基础']

def normalize(text):
    if not text:
        return ''
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[\$]', '', text)
    text = re.sub(r'[（）()]', '', text)
    return text

# 按年份分组
blank_by_year = defaultdict(list)
for q in blank_questions:
    if q['year'] != '2014':  # 跳过2014年
        blank_by_year[q['year']].append(q)

bank_by_year = defaultdict(list)
for q in prof_bank:
    bank_by_year[q['year']].append(q)

# 匹配
matched = {}  # bank_id -> (year, qnum)
unmatched_bank = []

for year in sorted(bank_by_year.keys()):
    bank_year = bank_by_year[year]
    blank_year = blank_by_year.get(year, [])

    if not blank_year:
        unmatched_bank.extend(bank_year)
        continue

    # 对每道题库题目，找到最匹配的空白卷题目
    used_blank = set()

    for bank_q in bank_year:
        best_match = None
        best_score = 0
        best_idx = -1

        bank_q_norm = normalize(bank_q['question'])
        bank_opts_norm = {opt: normalize(bank_q.get(opt, '')) for opt in ['A', 'B', 'C', 'D']}

        for i, blank_q in enumerate(blank_year):
            if i in used_blank:
                continue

            score = 0
            blank_q_norm = normalize(blank_q['question'])

            # 题干匹配
            if bank_q_norm and blank_q_norm:
                min_len = min(len(bank_q_norm), len(blank_q_norm), 25)
                if min_len > 5:
                    common = sum(1 for j in range(min_len) if bank_q_norm[j] == blank_q_norm[j])
                    score += common / min_len * 4

            # 选项匹配
            for opt in ['A', 'B', 'C', 'D']:
                bank_opt = bank_opts_norm[opt]
                blank_opt = normalize(blank_q['options'].get(opt, ''))
                if bank_opt and blank_opt:
                    min_len = min(len(bank_opt), len(blank_opt), 15)
                    if min_len > 3:
                        common = sum(1 for j in range(min_len) if bank_opt[j] == blank_opt[j])
                        score += common / min_len * 2

            if score > best_score:
                best_score = score
                best_match = blank_q
                best_idx = i

        if best_match and best_score > 2.0:
            matched[bank_q['id']] = (year, best_match['qnum'])
            used_blank.add(best_idx)
        else:
            unmatched_bank.append(bank_q)

print(f"匹配成功: {len(matched)}/{len(prof_bank)}")
print(f"未匹配: {len(unmatched_bank)}")

# 按年份统计
for year in sorted(bank_by_year.keys()):
    year_matched = sum(1 for v in matched.values() if v[0] == year)
    year_total = len(bank_by_year[year])
    print(f"  {year}: 匹配{year_matched}/{year_total}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\prof_id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存到 prof_id_to_qnum.json")

import json, re
from collections import defaultdict

# 读取专业基础空白卷提取的题目
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

# 分离2022和2022补考
# 空白卷中2022年有124题，包含两套题目
blank_2022 = [q for q in blank_questions if q['year'] == '2022']
print(f"空白卷2022年: {len(blank_2022)}题")

# 按题号分组，每个题号应该有2道题（2022和2022补考）
by_qnum = defaultdict(list)
for q in blank_2022:
    by_qnum[q['qnum']].append(q)

# 第一套是2022，第二套是2022补考
blank_2022_normal = []
blank_2022_supplement = []
for qnum in sorted(by_qnum.keys()):
    qs = by_qnum[qnum]
    if len(qs) >= 1:
        blank_2022_normal.append(qs[0])
    if len(qs) >= 2:
        blank_2022_supplement.append(qs[1])

print(f"2022正常: {len(blank_2022_normal)}题")
print(f"2022补考: {len(blank_2022_supplement)}题")

# 重新整理空白卷题目
blank_by_year = defaultdict(list)
for q in blank_questions:
    if q['year'] == '2014':
        continue  # 跳过2014年
    elif q['year'] == '2022':
        # 已经分离，跳过
        continue
    else:
        blank_by_year[q['year']].append(q)

blank_by_year['2022'] = blank_2022_normal
blank_by_year['2022补'] = blank_2022_supplement

# 匹配
matched = {}
unmatched_bank = []

for year in sorted(blank_by_year.keys()):
    blank_year = blank_by_year[year]
    bank_year = [q for q in prof_bank if q['year'] == year]

    if not bank_year:
        continue

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

            if bank_q_norm and blank_q_norm:
                min_len = min(len(bank_q_norm), len(blank_q_norm), 25)
                if min_len > 5:
                    common = sum(1 for j in range(min_len) if bank_q_norm[j] == blank_q_norm[j])
                    score += common / min_len * 4

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

print(f"\n匹配成功: {len(matched)}/{len(prof_bank)}")
print(f"未匹配: {len(unmatched_bank)}")

for year in sorted(blank_by_year.keys()):
    year_matched = sum(1 for v in matched.values() if v[0] == year)
    year_total = len([q for q in prof_bank if q['year'] == year])
    print(f"  {year}: 匹配{year_matched}/{year_total}")

# 保存匹配结果
with open(r'D:\应用程序开发\刷题\exam-quiz\prof_id_to_qnum.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in matched.items()}, f, ensure_ascii=False, indent=2)

print(f"\n匹配结果已保存")

import json, re
from collections import defaultdict

# 读取PDF提取的题目（按题号顺序）
with open(r'D:\应用程序开发\刷题\exam-quiz\pdf_questions_raw.json', 'r', encoding='utf-8') as f:
    pdf_questions = json.load(f)

# 读取当前题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    bank_questions = json.load(f)

pub_bank = [q for q in bank_questions if q['bigSubject'] == '公共基础']
prof_bank = [q for q in bank_questions if q['bigSubject'] == '专业基础']

def normalize(text):
    if not text:
        return ''
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[\$]', '', text)
    text = re.sub(r'[（）()]', '', text)
    return text

# 建立题库的索引：用题干前15字符+选项内容
bank_index = defaultdict(list)
for q in pub_bank:
    key = normalize(q['question'])[:15]
    bank_index[key].append(q)

# 为每道PDF题目匹配题库中的答案和解析
new_pub = []
matched_count = 0
unmatched_count = 0
matched_ids = set()

# 按年份+题号排序
pdf_questions.sort(key=lambda x: (x['year'], x['qnum']))

current_id = 1
for pdf_q in pdf_questions:
    # 尝试匹配
    best_match = None
    best_score = 0

    pdf_q_norm = normalize(pdf_q['question'])
    key = pdf_q_norm[:15]

    candidates = bank_index.get(key, [])
    # 如果key没找到，尝试所有同年份的题目
    if not candidates:
        candidates = [q for q in pub_bank if q['year'] == pdf_q['year']]

    for bank_q in candidates:
        # 检查是否已经被匹配过
        if bank_q['id'] in matched_ids:
            continue

        score = 0
        bank_q_norm = normalize(bank_q['question'])

        # 题干匹配
        if bank_q_norm and pdf_q_norm:
            min_len = min(len(bank_q_norm), len(pdf_q_norm), 20)
            if min_len > 5:
                common = sum(1 for i in range(min_len) if bank_q_norm[i] == pdf_q_norm[i])
                score += common / min_len * 3

        # 选项匹配
        for opt in ['A', 'B', 'C', 'D']:
            bank_opt = normalize(bank_q.get(opt, ''))
            pdf_opt = normalize(pdf_q['options'].get(opt, ''))
            if bank_opt and pdf_opt:
                min_len = min(len(bank_opt), len(pdf_opt), 10)
                if min_len > 3:
                    common = sum(1 for i in range(min_len) if bank_opt[i] == pdf_opt[i])
                    score += common / min_len

        if score > best_score:
            best_score = score
            best_match = bank_q

    if best_match and best_score > 1.5:
        # 匹配成功，使用题库中的答案和解析
        matched_ids.add(best_match['id'])
        matched_count += 1
        new_q = {
            'id': current_id,
            'bigSubject': '公共基础',
            'smallSubject': best_match['smallSubject'],
            'year': pdf_q['year'],
            'question': best_match['question'],  # 使用题库中的题干（已处理公式）
            'A': best_match['A'],
            'B': best_match['B'],
            'C': best_match['C'],
            'D': best_match['D'],
            'answer': best_match['answer'],
            'analysis': best_match['analysis']
        }
    else:
        # 匹配失败，使用PDF提取的题干，答案和解析留空
        unmatched_count += 1
        new_q = {
            'id': current_id,
            'bigSubject': '公共基础',
            'smallSubject': '',
            'year': pdf_q['year'],
            'question': pdf_q['question'],
            'A': pdf_q['options'].get('A', ''),
            'B': pdf_q['options'].get('B', ''),
            'C': pdf_q['options'].get('C', ''),
            'D': pdf_q['options'].get('D', ''),
            'answer': '',
            'analysis': ''
        }

    new_pub.append(new_q)
    current_id += 1

print(f"匹配成功: {matched_count}")
print(f"匹配失败: {unmatched_count}")
print(f"总题数: {len(new_pub)}")

# 检查每年的题数
year_counts = defaultdict(int)
for q in new_pub:
    year_counts[q['year']] += 1
print(f"\n按年份分布:")
for y, c in sorted(year_counts.items()):
    print(f"  {y}: {c}题")

# 合并专业基础
# 专业基础的id需要重新分配
for i, q in enumerate(prof_bank):
    q['id'] = current_id + i

new_all = new_pub + prof_bank

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(new_all, f, ensure_ascii=False, indent=2)

print(f"\n新题库已保存: {len(new_all)}题")
print(f"公共基础id: 1-{len(new_pub)}")
print(f"专业基础id: {len(new_pub)+1}-{len(new_all)}")

# 验证2014年第9题
print(f"\n2014年第9题（id=129）:")
for q in new_pub:
    if q['year'] == '2014' and q['id'] == 121 + 8:  # 2014年从id=121开始
        print(f"  question: {q['question'][:80]}")
        print(f"  answer: {q['answer']}")
        break

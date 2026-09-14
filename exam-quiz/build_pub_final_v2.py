import json, re
from collections import defaultdict

# 读取新合并的题目（带正确题号）
with open(r'D:\应用程序开发\刷题\exam-quiz\pub_merged_raw.json', 'r', encoding='utf-8') as f:
    new_questions = json.load(f)

# 读取原始题库（有小科目、公式处理、图片）
with open(r'D:\应用程序开发\刷题\all_questions_merged.json', 'r', encoding='utf-8') as f:
    old_questions = json.load(f)

old_pub = [q for q in old_questions if q['bigSubject'] == '公共基础']

def normalize(text):
    if not text:
        return ''
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[\$]', '', text)
    text = re.sub(r'[（）()]', '', text)
    # 统一特殊字符
    text = re.sub(r'[𝐿𝑙𝐿]', 'L', text)
    text = re.sub(r'[𝜃θ]', 'θ', text)
    text = re.sub(r'[𝛼α]', 'α', text)
    text = re.sub(r'[𝛽β]', 'β', text)
    text = re.sub(r'[𝜋π]', 'π', text)
    return text

# 按年份分组原始题库
old_by_year = defaultdict(list)
for q in old_pub:
    old_by_year[q['year']].append(q)

# 匹配
matched_count = 0
unmatched_count = 0
final_questions = []
used_old_ids = set()

for new_q in new_questions:
    year = new_q['year']
    candidates = old_by_year.get(year, [])

    best_match = None
    best_score = 0

    new_q_norm = normalize(new_q['question'])
    new_opts_norm = {opt: normalize(new_q.get(opt, '')) for opt in ['A', 'B', 'C', 'D']}

    for old_q in candidates:
        if old_q['id'] in used_old_ids:
            continue

        score = 0
        old_q_norm = normalize(old_q['question'])

        # 题干匹配：使用子串匹配
        if old_q_norm and new_q_norm:
            # 取共同前缀
            min_len = min(len(old_q_norm), len(new_q_norm))
            if min_len > 3:
                common = sum(1 for i in range(min_len) if old_q_norm[i] == new_q_norm[i])
                score += common / min_len * 3

            # 检查是否有共同的关键词
            keywords = ['向量', '直线', '平面', '极限', '导数', '积分', '微分', '级数',
                       '矩阵', '概率', '电路', '信号', '结构', '力学', '流体', '地质',
                       '法律', '合同', '许可', '质量', '安全']
            for kw in keywords:
                if kw in old_q_norm and kw in new_q_norm:
                    score += 0.5

        # 选项匹配
        for opt in ['A', 'B', 'C', 'D']:
            old_opt = normalize(old_q.get(opt, ''))
            new_opt = new_opts_norm[opt]
            if old_opt and new_opt:
                min_len = min(len(old_opt), len(new_opt))
                if min_len > 2:
                    common = sum(1 for i in range(min_len) if old_opt[i] == new_opt[i])
                    score += common / min_len * 1.5

        # 答案匹配
        if new_q['answer'] and old_q['answer'] == new_q['answer']:
            score += 0.5

        if score > best_score:
            best_score = score
            best_match = old_q

    # 降低匹配阈值
    if best_match and best_score > 1.5:
        used_old_ids.add(best_match['id'])
        matched_count += 1
        final_q = {
            'year': new_q['year'],
            'qnum': new_q['qnum'],
            'smallSubject': best_match['smallSubject'],
            'question': best_match['question'],
            'A': best_match['A'],
            'B': best_match['B'],
            'C': best_match['C'],
            'D': best_match['D'],
            'answer': new_q['answer'] if new_q['answer'] else best_match['answer'],
            'analysis': best_match['analysis']
        }
    else:
        unmatched_count += 1
        final_q = {
            'year': new_q['year'],
            'qnum': new_q['qnum'],
            'smallSubject': '',
            'question': new_q['question'],
            'A': new_q['A'],
            'B': new_q['B'],
            'C': new_q['C'],
            'D': new_q['D'],
            'answer': new_q['answer'],
            'analysis': new_q['analysis']
        }

    final_questions.append(final_q)

print(f"匹配成功: {matched_count}/{len(new_questions)}")
print(f"匹配失败: {unmatched_count}")

# 按年份+题号排序
final_questions.sort(key=lambda x: (x['year'], x['qnum']))

# 分配id
for i, q in enumerate(final_questions):
    q['id'] = i + 1
    q['bigSubject'] = '公共基础'
    del q['qnum']

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pub_final.json', 'w', encoding='utf-8') as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"\n最终公共基础题库: {len(final_questions)}题")

# 检查2014-9题
print(f"\n2014-9题（id=129）:")
for q in final_questions:
    if q['year'] == '2014' and q['id'] == 129:
        print(f"  smallSubject: {q['smallSubject']}")
        print(f"  question: {q['question'][:80]}")
        print(f"  answer: {q['answer']}")
        break

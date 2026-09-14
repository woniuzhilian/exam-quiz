import json, re
from collections import defaultdict

# 读取题目和答案
with open(r'D:\应用程序开发\刷题\exam-quiz\pub_questions_full.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open(r'D:\应用程序开发\刷题\exam-quiz\pub_answers_full.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 建立答案索引
answer_index = {}
for a in answers:
    key = (a['year'], a['qnum'])
    answer_index[key] = a

# 解析题目文本，提取题干和选项
def parse_question(text):
    """解析题目文本，返回题干和A/B/C/D选项"""
    lines = text.split('\n')
    question_parts = []
    options = {'A': '', 'B': '', 'C': '', 'D': ''}
    current_opt = None
    opt_parts = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 检查是否是选项开始
        opt_match = re.match(r'[（(]([A-D])[）)]\s*(.*)', line)
        if opt_match:
            # 保存上一个选项
            if current_opt and opt_parts:
                options[current_opt] = ' '.join(opt_parts)
            current_opt = opt_match.group(1)
            opt_parts = [opt_match.group(2)] if opt_match.group(2) else []
        elif current_opt:
            # 追加到当前选项
            opt_parts.append(line)
        else:
            # 追加到题干
            question_parts.append(line)

    # 保存最后一个选项
    if current_opt and opt_parts:
        options[current_opt] = ' '.join(opt_parts)

    question = ' '.join(question_parts)
    return question, options

# 合并题目和答案
merged = []
missing_questions = []
missing_answers = []

for q in questions:
    key = (q['year'], q['qnum'])
    question, options = parse_question(q['text'])

    if key in answer_index:
        ans = answer_index[key]
        answer = ans['answer']
        analysis = ans['analysis']
    else:
        answer = ''
        analysis = ''
        missing_answers.append(key)

    merged.append({
        'year': q['year'],
        'qnum': q['qnum'],
        'question': question,
        'A': options['A'],
        'B': options['B'],
        'C': options['C'],
        'D': options['D'],
        'answer': answer,
        'analysis': analysis
    })

# 检查是否有题目缺失
all_years = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2022补', '2023', '2024']
existing_keys = set((q['year'], q['qnum']) for q in merged)

for year in all_years:
    for qnum in range(1, 121):
        if (year, qnum) not in existing_keys:
            missing_questions.append((year, qnum))

print(f"合并题目总数: {len(merged)}")
print(f"缺失题目: {len(missing_questions)}")
if missing_questions:
    print(f"  缺失题号: {missing_questions[:20]}{'...' if len(missing_questions)>20 else ''}")

print(f"\n缺失答案: {len(missing_answers)}")
if missing_answers:
    print(f"  缺失答案题号: {missing_answers[:20]}{'...' if len(missing_answers)>20 else ''}")

# 保存合并结果
with open(r'D:\应用程序开发\刷题\exam-quiz\pub_merged_raw.json', 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"\n已保存到 pub_merged_raw.json")

# 显示2014-9题
print(f"\n2014-9题:")
for q in merged:
    if q['year'] == '2014' and q['qnum'] == 9:
        print(f"  question: {q['question'][:80]}")
        print(f"  A: {q['A'][:50]}")
        print(f"  B: {q['B'][:50]}")
        print(f"  answer: {q['answer']}")
        print(f"  analysis: {q['analysis'][:80]}")
        break

import json

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查看2013年的题目
year_2013 = [q for q in questions if q['year'] == '2013' and q['bigSubject'] == '公共基础']
year_2013_sorted = sorted(year_2013, key=lambda x: x.get('yearQnum', x['id']))

# 查看用户提到的题目
problem_questions = [3, 4, 10, 18, 19, 48, 56, 61, 62, 63, 90, 91, 95, 96]

for qnum in problem_questions:
    q = next((q for q in year_2013_sorted if q.get('yearQnum') == qnum), None)
    if q:
        print(f"\n{'='*60}")
        print(f"2013-{qnum}:")
        print(f"{'='*60}")
        print(f"题干: {q.get('question', '')[:200]}")
        print(f"\n选项A: {q.get('A', '')[:100]}")
        print(f"选项B: {q.get('B', '')[:100]}")
        print(f"选项C: {q.get('C', '')[:100]}")
        print(f"选项D: {q.get('D', '')[:100]}")
        print(f"\n答案: {q.get('answer', '')}")
        print(f"解析: {q.get('analysis', '')[:200]}")
    else:
        print(f"\n2013-{qnum}: 未找到")

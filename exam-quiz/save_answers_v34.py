import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第68页）
new_answers = {
    "2024-25": {"answer": "A", "analysis": "该结构已经可以通过三刚片原则证明为一个几何不变。当右侧支座为链杆时，无多余约束。右侧支座为铰时，有一个多余约束。该结构为与大地连接的几何多余约束。与上述结构相连后：可将该杆无限变短。即与大地多了一个铰，多了两个约束。即总共多了 3 个约束，超静定次数为 3。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

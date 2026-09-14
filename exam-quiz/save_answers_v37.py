import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第73页）
new_answers = {
    "2024-24": {"answer": "B", "analysis": "使用虚功原理，在 C 点加一个单位力 1（↓）。$F_{Bx} \\cdot f = \\frac{1}{2} \\cdot \\frac{L}{2}$，$F_{Bx} = \\frac{L}{4f}$（向左）。故，根据虚功方程：$1 \\cdot \\Delta_C + (-F_{Bx}) \\cdot \\Delta = 0 \\rightarrow \\Delta_C = \\frac{L}{4f} \\Delta$"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

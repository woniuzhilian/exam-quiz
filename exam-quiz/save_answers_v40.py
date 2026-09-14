import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第78页）
new_answers = {
    "2024-26": {"answer": "B", "analysis": "动力位移系数：$\\beta = \\frac{1}{1-(\\frac{\\theta}{\\omega})^2} = 2$，振幅$A = \\beta y_{st} = 2y_{st}$，$y_{st}$为 F 作用下时的静力位移。用位移法求解：求侧移，一个自由度（EI = ∞，不发生弯曲）故：求侧移时用剪力的形常数：$r_{11} = \\frac{12i}{l^2} + \\frac{3i}{l^2} = \\frac{12EI}{l^3} + \\frac{3EI}{l^3} = \\frac{15EI}{l^3}$。则：$r_{11}Z_1 + R_{1P} = 0$，$\\frac{15EI}{l^3} \\cdot Z_1 = F$，$Z_1 = \\frac{Fl^2}{15EI}$，$A = \\beta y_{st} = 2 \\cdot \\frac{Fl^2}{15EI} = \\frac{2Fl^2}{15EI}$"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

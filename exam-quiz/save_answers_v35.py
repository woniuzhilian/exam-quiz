import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第69-70页）
new_answers = {
    "2017-22": {"answer": "C", "analysis": "$M_{BA} = ql^2/36 - 5ql/12 \\times l + ql \\times l/2 = ql^2/9$（上拉）结构对称，$M_{DC} = M_{BA} = -ql^2/9$"},
    "2017-23": {"answer": "A", "analysis": "取半结构如图，$H_A = P$。"},
    "2019-22": {"answer": "B", "analysis": "采用截面法分析内力，将 BC 杆断开，设 BC 杆内力为$F_N$。对 A 点取矩，由$\\Sigma M_A=0$，$F_P \\times 4+F_N \\times cos45° \\times 2=0$，解得 $F_N$=−2 $\\sqrt{2}F_P$（压力）。"},
    "2019-23": {"answer": "A", "analysis": "根据结构的静力平衡条件求解。对 B 点取矩，假定 A 支座竖向支反力 $F_{Ay}$ 方向为↑，由$\\Sigma M_B=0$，$F_{Ay} \\times L-F_P \\times L/4=0$，解得 $F_{Ay}$=$F_P/4$（↑）；将结构从 C 点断开，取左半部分研究，对 C 点取矩,由$\\Sigma M_C=0$，$F_H \\times f-F_{Ay} \\times L/2$=$F_H \\times L/2$-$F_{Ay} \\times L/2$=0，求得水平推力为：$F_H$=$F_P/4$(→)。"},
    "2020-23": {"answer": "B", "analysis": "①整体对 B 取矩 $F_{AX} \\times 4 + F_{Ay} \\cdot 8 = 10 \\times 4 \\times 6$。②左部分隔离体对 C 取矩$F_{AX} \\cdot 8 + F_{Ay} \\times 4 = 70 \\times 4 + 10 \\times 4 \\times 2$。② × 2 − ① 720 − 240 = $12F_{AX}$ $\\Rightarrow$ $F_{AX} = 40kN$。③$M$=$40 \\times 8 - 70 \\times 40 = 40KN \\cdot m$"},
    "2021-22": {"answer": "A", "analysis": "(1)以整体为研究对象，对 B 力矩平衡，$A_y \\times 8 + 20 \\times 4 = 5 \\times 4 \\times 2$，解得$A_y = -5kN$。(2)以左部分为研究对象，对 C 力矩平衡，$A_x \\times 8 + 20 \\times 4 = -5 \\times 4$，解得$A_x = -12.5kN$。(3)$M = -12.5 \\times 8 + 20 \\times 4 = -20kN \\cdot m$。"},
    "2021-23": {"answer": "C", "analysis": "(1)求支点反力，根据对称，$F_B = 30kN$ ↑。(2)分析 B 结点可知，$F_{BC} = -30kN$（压）。(3)分析 C 结点，DE、DC 为 0 杆；水平方向力的平衡可知，$F_{EC} = F_{FC}$；竖直方向力的平衡可知，$F_{EC} = -25kN$。"},
    "2022-23": {"answer": "A", "analysis": "采用截面法求解。沿图示虚线截面截开，取左上角隔离体为研究对象，对 O 点取力矩平衡，除了 C 杆，其余几个杆件均通过 O 点，对 O 点力矩为零。因此有：$F_c \\times l = p \\times l$，解得$F_c = p$。"},
    "2022补-23": {"answer": "B", "analysis": "(1)以整体为研究对象，对 D 取力矩平衡，$F_{Ay} \\times 2a + P \\times 2a = 0 \\Rightarrow F_{Ay} = -p$(竖直向下)；(2)沿着铰 C 截开，取左半部分为研究对象，对铰 C 取力矩平衡，$F_{Ay} \\times 2a - F_{Ax} \\times 2a = 0 \\Rightarrow F_{Ay} = F_{Ax} = -p$(水平向左)；(3)以 AB 杆为研究对象，$M_{BA} = F_{Ax} \\times 2a = 2pa$；(4)B 节点无外力偶，两端弯矩应相等，故$M_{BA} = M_{BC} = 2pa$。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

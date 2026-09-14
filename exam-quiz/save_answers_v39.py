import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第76-77页）
new_answers = {
    "2019-24": {"answer": "D", "analysis": "利用位移法求解。B 点处产生角位移，设 B 处的转角为$\\theta_B$，则各杆端弯矩为：M$_{AB}$=4i$\\theta$+2i$\\theta_B$；M$_{BA}$=2i$\\theta$+4i$\\theta_B$；M$_{BC}$=i$\\theta_B$；M$_{CB}$=-i$\\theta_B$。考虑结点 B 的平衡，列位移法基本方程为：$\\Sigma M_B$=0，M$_{BA}$+M$_{BC}$=0，解得：$\\theta_B$=-2$\\theta$/5。"},
    "2020-24": {"answer": "A", "analysis": "用力矩分配法计算时，B 处附加刚臂后为固定端，则：1 力矩分配系数：$\\mu_{BA} = \\frac{3i_{BA}}{3i_{BA}+3i_{BC}} = \\frac{3EI/L}{3EI/L+3 \\times 2EI/L} = \\frac{1}{3}$。2 固端弯矩：$M_{BA} = M \\times \\mu_{BA} = -\\frac{M}{3}$"},
    "2022-25": {"answer": "B", "analysis": "根据主系数物理含义，自身单位位移需要的单位力，恒为正。"},
    "2016-23": {"answer": "C", "analysis": "$\\omega = \\sqrt{k/m} = \\sqrt{\\frac{1}{M\\delta}}$。k 与 EI 成正比。"},
    "2018-23": {"answer": "B", "analysis": "单自由度体系有阻尼强迫振动，位移及受力特点是：当$\\frac{\\theta}{\\omega}$很小时，体系振动很慢，惯性力、阻尼力都很小，这时动荷载主要由弹性恢复力平衡，位移与荷载基本同步；当$\\frac{\\theta}{\\omega}$很大时，体系振动很快，惯性很大，而弹性力和阻尼力较小，这时动荷载主要由惯性力平衡，位移与动荷载方向相反；当$\\frac{\\theta}{\\omega}$=1 时，位移与荷载的相位角相差接近于 90°，这时惯性力与弹性恢复力平衡而动荷载与阻尼力平衡。"},
    "2022-26": {"answer": "B", "analysis": "悬臂梁，端部受到集中力时，k$_{11}$ = $\\frac{3EI}{l^3}$，因此，结构自振频率为：$\\omega = \\sqrt{\\frac{k_{11}}{m}} = \\sqrt{\\frac{3EI}{ml^3}}$，则，动力系数$\\mu = \\frac{1}{1-\\theta^2/\\omega^2} = \\frac{1}{1-\\frac{0.75}{3}} = 1.33$。"},
    "2022补-26": {"answer": "B", "analysis": "根据自振频率公式$\\omega = \\sqrt{\\frac{k}{m}}$，与质量成负相关，与刚度成正相关。"},
    "2023-26": {"answer": "D", "analysis": "动力自由度分析，M$_1$ 的竖向振动和水平振动没有约束，均存在。因为杆件不考虑轴向变形，所以 M$_1$ 与 M$_2$ 水平振动同步，属于一个动力自由度；M$_2$ 竖向直接受其连接的底端固结竖杆约束，不会发生振动，即不计入动力自由度。故结构有两个动力自由度，为 M$_1$ 竖向振动和 M$_1$M$_2$ 同步水平振动。"},
    "2024-26": {"answer": "B", "analysis": ""},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

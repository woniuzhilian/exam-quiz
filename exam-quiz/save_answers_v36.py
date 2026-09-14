import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第71-72页）
new_answers = {
    "2023-24": {"answer": "D", "analysis": "把 K 节点断开，取左边为隔离体，对隔离体左边铰接点取距得：2Q$_k$-1=0，故Q$_k$=0.5KN。"},
    "2024-23": {"answer": "C", "analysis": "整体对 A 取距：$\\Sigma M_A = 0$，$R_D \\times 4 = 10 \\times 5 + 4 \\times 5 + \\frac{5}{2}$，$R_D = 25kN$（↑）。取右半部分为隔离体：$\\Sigma y = 0$，$F_E = 25kN$（↓），$V_E = -25 \\times \\frac{4}{5} = -20kN$（逆时针）"},
    "2024-27": {"answer": "B", "analysis": "取中间段分析，其支座反力如图：排除 C。在集中力偶处，弯矩图突变，右边力偶为顺时针，使杆下侧受拉，应向下突变。同理，左边力偶也应向下突变，排除 A；在左边集中力，弯矩图应拐弯，所以排除 D。"},
    "2016-22": {"answer": "D", "analysis": "静定结构各杆件相对刚度变化不影响各杆件的内力，根据单位荷载法，位移用弯矩图图乘计算。正对称结构在反对称荷载作用下只有反对称力和反对称位移，取半结构，C 处只有竖向的支撑链杆。根据单位荷载法，AC 杆 EI 增大一倍，左侧半结构的水平位移为原来的一半，即Δ/4；BC 杆 EI 不变，右侧半结构的水平位移不变仍为Δ/2。故总的水平位移为：$\\Delta_{CH}$=Δ/4+Δ/2=0.75Δ。"},
    "2017-24": {"answer": "B", "analysis": "$M_C = 0$，$V_B \\times l/2 = q \\times l/2 \\times l/4$，故$V_B = ql/4$，B 杆位移等于弹簧变形，故：$ql^4/8EI - V_B l^3/3EI = V_B/k$，解得：$k = 6EI/l^3$"},
    "2018-22": {"answer": "B", "analysis": "该结构为对称结构，受对称荷载作用，且中间通过铰连接弯矩为零，故中间铰处只有水平力作用，取左侧结构分析可得 $F_H$=-M/L。"},
    "2022-24": {"answer": "C", "analysis": "力与位移对应性，相对线位移对应一对相对力。"},
    "2022补-24": {"answer": "C", "analysis": "(1)对 A 点施加顺时针单位力偶，做出$\\overline{M_1}$和$M_p$图分别如下：(2)图乘法：$\\frac{1}{EI}(\\frac{1}{2} \\times pa \\times a \\times 1) + \\frac{1}{2EI}(\\frac{1}{2} \\times pa \\times a \\times 1 + pa \\times a \\times 1) = 5Pa^2/(4EI)$"},
    "2024-24": {"answer": "B", "analysis": ""},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

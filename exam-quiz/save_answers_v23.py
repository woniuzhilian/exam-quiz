import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第48-49页）
new_answers = {
    "2017-38": {"answer": "C", "analysis": "A 选项中一维固结理论当中的固结系数与强度指标c、$\\varphi$无关，B 选项中地基土的渗流当中的重要参数渗透系数与强度指标c、$\\varphi$无关，D 选项中粘性土的压密当中的主要压缩性指标（压缩系数、压缩模量和体积压缩系数）均与强度指标c、$\\varphi$无关；而 C 选项中地基承载力理论当中，强度指标c、$\\varphi$为地基承载力的控制性指标，临塑荷载、临界荷载和极限荷载都与该两个指标有直接关系，故选 C。"},
    "2022-38": {"answer": "B", "analysis": "在小注教育精讲班中，我们一直强调，有几个公式我们是一定要背会的，包括下面两个公式：$\\sigma_1 = \\sigma_3 tan^2(45° + \\frac{\\varphi}{2}) + 2c \\cdot tan(45° + \\frac{\\varphi}{2})$，$\\sigma_3 = \\sigma_1 tan^2(45° - \\frac{\\varphi}{2}) - 2c \\cdot tan(45° - \\frac{\\varphi}{2})$。题目中已经告诉了我们地基土的抗剪强度指标，也告诉了某一点的大主应力$\\sigma_1 = 300kpa$，要求小主应力$\\sigma_3$就要用到第二个公式：$\\sigma_3 = \\sigma_1 tan^2(45° - \\frac{\\varphi}{2}) - 2c \\cdot tan(45° - \\frac{\\varphi}{2})$ = $300 \\times tan^2(45° - \\frac{30°}{2}) - 2 \\times 5 \\times tan(45° - \\frac{30°}{2})$ = $\\frac{300}{3} - 2 \\times 5 \\times \\frac{\\sqrt{3}}{3}$ =94.2kPa，所以本题选 B。"},
    "2022-53": {"answer": "A", "analysis": "地基土的短期承担荷载中，土体具有厚度，与荷载接触部位的水，被较快地排挤出去，深度大的水还没有来得及感受到荷载充分作用，水体来不及充分排挤，土体颗粒不能受到充分压缩，即不能充分固结。所以应采用不固结不排水试验抗剪强度指标。不固结不排水强度用于荷载增加较快，引起的孔隙水压力来不及消散的情况。"},
    "2022补-40": {"answer": "C", "analysis": "地基破坏形式分为整体剪切破坏、局部剪切破坏、冲剪破坏，在低压缩性土较易发生整体剪切破坏，在高压缩性土较易发生冲剪破坏。所以，选 C。"},
    "2023-38": {"answer": "D", "analysis": "在土的抗剪极限平衡状态中，剪切面与大主应力作用面（或小主应力方向）的夹角：$\\theta_f = 45° + \\frac{\\varphi}{2}$。剪切面与小主应力作用面（或大主应力方向）的夹角：$\\theta_f' = 90° - (45° + \\frac{\\varphi}{2}) = 45° - \\frac{\\varphi}{2}$，所以本题选 D。"},
    "2024-38": {"answer": "A", "analysis": "静力平衡条件是所有物体在任何状态下都应满足的基本条件，并不特定于土的极限平衡状态。建立土的极限平衡条件的依据是莫尔应力圆与抗剪强度包线相切的几何关系。当莫尔应力圆与抗剪强度包线相切时，表示该点的剪应力达到了土体的抗剪强度，即土体处于极限平衡状态。"},
    "2024-40": {"answer": "C", "analysis": "太沙基的地基极限承载力理论是基于土体达到塑性平衡状态时的力学条件推导出来的。结合他的计算公式，考虑的是基底以下土体的抗剪强度，未考虑倒基底以上填土的抗剪强度。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

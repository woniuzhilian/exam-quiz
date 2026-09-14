import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第42-43页）
new_answers = {
    "2020-34": {"answer": "D", "analysis": "土的三相比例指标包括由试验直接测定的基本指标和换算的物理性质指标。其中，由试验直接测定的基本指标包括含水率、重力密度和土粒比重。土粒比重是指土粒重量与同体积 4℃时水的重量之比，可通过比重瓶法测定。D 项为换算指标，可通过以上三项基本指标换算得出。"},
    "2020-35": {"answer": "C", "analysis": "对细粒土要求在最优含水量下压实，根据土的击实曲线，如下图，可知，对细粒土要求在最优含水量下压实，主要是为了在最优含水量下，在相同的压实功能作用下，能够得到最大的干密度。所以选 C。"},
    "2021-34": {"answer": "A", "analysis": "为了确定三相草图各量中的三个量，就必须通过实验室的实验来测定，通常做三个最容易操作的基本物理性质实验，它们是土的密度实验、土的比重实验和土的含水量实验。"},
    "2021-35": {"answer": "B", "analysis": "综合以上几种密度和重度的概念和定义可知，同一土样各种密度和重度在数值上由如下关系：$\\gamma_{sat} > \\gamma > \\gamma_d > \\gamma'$，$\\rho_{sat} > \\rho > \\rho_d > \\rho'$"},
    "2022-40": {"answer": "D", "analysis": "在小注教育精讲班中，我们一直强调，有几个公式我们是一定要背会的，包括下面两个公式太沙基极限承载力理论公式，整体剪切破坏时太沙基极限承载力理论公式：$P_u = \\frac{1}{2} \\gamma b N_r + \\gamma_m d N_q + c N_c = \\frac{1}{2} \\times 18 \\times 4 \\times 11 + 17 \\times 2 \\times 12.7 + 8 \\times 25.1 = 1028.6kPa$，所以本题选 D。"},
    "2023-35": {"answer": "A", "analysis": "为了确定土的三相草图各个量的大小，就必须通过实验室的试验测定，通常做三个最容易操作的基本物理实验性性质实验，分别是：土的密度实验，土粒比重实验和土的含水量实验，所以本题选 A。"},
    "2023-36": {"answer": "C", "analysis": "根据土的液性指标的计算公式，根据液性指数划分软硬程度：$I_L = \\frac{w - w_P}{w_L - w_P} = \\frac{28 - 20}{40 - 20} = 0.4$，属于可塑状态，所以本题选 C。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

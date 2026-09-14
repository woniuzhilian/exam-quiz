import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第52页）
new_answers = {
    "2023-51": {"answer": "C", "analysis": "（1）在边坡形成过程中，主应力迹线发生了明显偏转，表现为接近于临空面，其最大主应力方向趋于平行临空面，而最小主应力方向则与临空面垂直相交。（2）在临空面附近（尤其是在坡脚处）出现应力集中现象。平行于临空面的最大主应力显著升高，在边坡表面达到最大值，向岩体内部逐渐降低。垂直于临空面的最小主应力明显降低在边坡面附近降到最小，以至于变为零或转化为拉伸应力，向岩体内部逐渐升高。由此可见,临空面附近岩体中应力差最大，很容易发生剪切破坏。而主应力转为拉伸应力部分是出现拉裂破坏处。（3）由于主应力迹线发生偏转，最大剪应力迹线也随之变为凹向临空面的弧形分布。（4）在临空面附近，岩体近似处于单轴应力状态，向内部逐渐过渡为三轴应力状态。"},
    "2024-39": {"answer": "B", "analysis": "注意审题，题目问的是求解被动土压力时，破裂面与水平面的夹角。此时水平面为小主应力面，夹角为$45° - \\frac{1}{2}\\varphi$。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

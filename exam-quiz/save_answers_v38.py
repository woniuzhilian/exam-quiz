import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第74-75页）
new_answers = {
    "2016-24": {"answer": "D", "analysis": "注意图中结点，除了 A，三个都是刚节点。先解除支座，求出支座反力，左支座的竖向力(P，下)，根据两根横杆的抗侧移刚度分配剪力。AB 杆可视作一端固定一端铰支的杆件，抗侧移刚度为 3EI/l3 下面的横杆可视作两端固定，抗侧移刚度为 12EI/l3，则 AB 杆分配到3P/(3 + 12) = P/5，因此 B 端弯矩为Pl/5。题目的图不是特别清楚，可能会有些误解，如果将左下节点视作铰接点，就应当选 A。"},
    "2018-24": {"answer": "B", "analysis": "（a）图中，令 BD 杆长为 l，断开 BD 链杆，用未知力 X$_1$ 代替，如果力法方程中的自由项$\\Delta_{1t}$=0，则结构在温度作用下无内力产生，（a）图中的自由项，$\\Delta_{1t}$=-$\\frac{\\sqrt{2}}{2}$$\\alpha$t×$\\sqrt{2}$l×2+1×$\\alpha$t×l=-$\\alpha$tl≠0，故（a）图中有内力产生；同理，（b）图中，令 BD 杆长为 l，断开 BD 链杆，用未知力 X$_1$ 代替，自由项$\\Delta_{1t}$=-$\\frac{\\sqrt{2}}{2}$$\\alpha$t×$\\frac{\\sqrt{2}}{2}$l×2+1×$\\alpha$t×l=0，（b）图中无内力产生。"},
    "2021-24": {"answer": "B", "analysis": "(1)去掉弹簧，以未知力X$_1$替代，得到如下图所示基本体系：力法方程为：$\\delta_{11}X_1 + \\Delta_{1p} = -\\frac{x_1}{k}$。(2)施加竖直向上单位力，M$_p$和$\\overline{M}$图如下。(3)求解系数，解力法方程：$\\delta_{11} = \\frac{1}{2} \\times l \\times l \\times \\frac{2l}{3EI} = \\frac{l^3}{3EI}$，$\\Delta_{1p} = -\\frac{1}{2} \\times l \\times pl \\times \\frac{2l}{3EI} = \\frac{-pl^3}{3EI}$。带入力法方程，解得：X$_1$ = $\\frac{2p}{3}$。(4)图乘法求位移，B 点施加单位力矩，M$_p$和$\\overline{M}$图如下。则：$\\theta_B = -\\frac{1}{2} \\times l \\times \\frac{pl}{3} \\times \\frac{1}{EI} = \\frac{pl^2}{6EI}$"},
    "2022补-25": {"answer": "A", "analysis": "(1)令X$_1$ = 1，做出$\\overline{M_1}$图如下：(2)图形自乘：$\\delta_{11} = \\frac{1}{EI}(\\frac{1}{2} \\times l \\times 1 \\times \\frac{2}{3}) \\times 2 = 2l/(3EI)$"},
    "2023-25": {"answer": "D", "analysis": "力法的主系数恒为正。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

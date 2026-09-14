import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第22-23页）
new_answers = {
    "2016-10": {"answer": "B", "analysis": "根据线性函数的误差传播定律：若有 n 个独立观测值的线性函数：Z = $K_1X_1 + K_2X_2 + A + K_nX_n + K_0$，$m_z = \\pm\\sqrt{K_1^2m_1^2 + K_2^2m_2^2 + A + K_n^2m_n^2}$。则有：∵ ∠C = 180° − ∠A − ∠B，∴ $m_c = \\pm\\sqrt{(-1)^2m_A^2 + (-1)^2m_B^2} = \\pm6.4''$"},
    "2017-10": {"answer": "A", "analysis": "一般函数的误差传播定律，解题步骤为：（1）按实际测量问题的要求写出函数式：Z = f（$x_1$，$x_2$，…$x_n$）（2）对函数进行全微分：dZ = $(\\frac{\\partial f}{\\partial x_1}) dx_1 + (\\frac{\\partial f}{\\partial x_2}) dx_2 + \\cdots + (\\frac{\\partial f}{\\partial x_n}) dx_n$（3）变成中误差公式：$m_Z^2 = (\\frac{\\partial f}{\\partial x_1})^2m_1^2 + (\\frac{\\partial f}{\\partial x_2})^2m_2^2 + \\cdots + (\\frac{\\partial f}{\\partial x_n})^2m_n^2$。针对本题：（1）函数式为：A=a×b（2）全微分：dA = a × d(b) + b × d(a)（3）变成中误差：$m_A^2 = a^2 \\times m_b^2 + b^2 \\times m_a^2 = 30^2 \\times 0.003^2 + 25^2 \\times 0.004^2$，$m_A = \\pm0.134$"},
    "2017-11": {"answer": "A", "analysis": "三等水准测量，根据使用的仪器不同，红、黑面所测高差之差限值也不同，对于 DS1 水准仪，该限制为 1.5mm，DS3 水准仪，该限值为 3mm，根据本题的选项，应选 3mm。"},
    "2020-8": {"answer": "D", "analysis": "和函数的中误差计算传播规律为：Z=X1+X2+……+Xn，$m_z = \\pm\\sqrt{m_1^2 + m_2^2 + \\cdots + m_n^2}$。又因为 180°− ∠N=∠E+∠F，180°是常数，则 360°− ∠N 的中误差为 ∠N 的中误差，即：$m_z = \\pm\\sqrt{m_E^2 + m_F^2} \\approx \\pm4.2''$"},
    "2021-11": {"answer": "C", "analysis": "函数关系式S = a·b，求微分则ds = bda + adb，故$f_1 = \\frac{\\partial F}{\\partial a} = b$；$f_2 = \\frac{\\partial F}{\\partial b} = a$，得$m_s = \\pm\\sqrt{(f_1)^2m_a^2 + (f_{21})^2m_b^2} = \\pm\\sqrt{80^2 \\times (\\pm0.002)^2 + 60^2 \\times (\\pm0.003)^2} = \\pm0.024m^2$。"},
    "2024-10": {"answer": "D", "analysis": "相对精度K = $\\frac{m}{D}$，D= $\\frac{1}{2} \\times (D_往 + D_返)$ = $\\frac{1}{2} \\times (34.995 + 35.005)$ = 35m，m = $|D_往 - D_返|$ = |34.995 − 35.005| = 0.01，则K = $\\frac{0.01}{35}$ = $\\frac{1}{3500}$。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

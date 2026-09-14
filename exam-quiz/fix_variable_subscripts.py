import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def fix_variable_subscripts(text):
    """修复变量下标问题：变量+空格+数字 -> 变量_数字"""
    if not text:
        return text

    # 只处理不在$中的内容
    parts = re.split(r'(\$[^$]*\$)', text)
    result = []

    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            result.append(part)
            continue

        # 常见变量下标模式：
        # x 0, x 1, x 2 -> x_0, x_1, x_2
        # V 1, V 2 -> V_1, V_2
        # R 1, R 2 -> R_1, R_2
        # T 1, T 2 -> T_1, T_2
        # P 1, P 2 -> P_1, P_2
        # F 1, F 2 -> F_1, F_2
        # I 1, I 2 -> I_1, I_2
        # U 1, U 2 -> U_1, U_2
        # d 1, d 2 -> d_1, d_2
        # Q 1, Q 2 -> Q_1, Q_2
        # L 1, L 2 -> L_1, L_2
        # k 1, k 2 -> k_1, k_2
        # C 1, C 2 -> C_1, C_2
        # f 1, f 2 -> f_1, f_2
        # a 1, a 2 -> a_1, a_2
        # b 1, b 2 -> b_1, b_2
        # c 1, c 2 -> c_1, c_2
        # n 1, n 2 -> n_1, n_2
        # m 1, m 2 -> m_1, m_2
        # p 1, p 2 -> p_1, p_2
        # q 1, q 2 -> q_1, q_2
        # r 1, r 2 -> r_1, r_2
        # s 1, s 2 -> s_1, s_2
        # t 1, t 2 -> t_1, t_2
        # u 1, u 2 -> u_1, u_2
        # v 1, v 2 -> v_1, v_2
        # w 1, w 2 -> w_1, w_2
        # y 1, y 2 -> y_1, y_2
        # z 1, z 2 -> z_1, z_2

        # 只修复单个字母变量+空格+数字的情况
        # 并且数字后面不是其他字母（避免误修复）
        variables = ['x', 'y', 'z', 'V', 'R', 'T', 'P', 'F', 'I', 'U', 'd', 'Q', 'L', 'k', 'C', 'f', 'a', 'b', 'c', 'n', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'M', 'N', 'E', 'W', 'H', 'O', 'S', 'A', 'B', 'D', 'G', 'K', 'Y', 'Z']

        for var in variables:
            # 模式：变量+空格+数字（数字后面是空格、标点或结尾）
            pattern = re.escape(var) + r'\s+(\d+)(?=[\s，。、；：）)\]】]|$)'
            part = re.sub(pattern, var + r'_\1', part)

        result.append(part)

    return ''.join(result)

# 修复所有题目
fixed_count = 0
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D']:
        original = q.get(field, '')
        if not original:
            continue

        fixed = fix_variable_subscripts(original)

        if fixed != original:
            q[field] = fixed
            fixed_count += 1
            print(f'修复 {q["year"]}-{q.get("yearQnum")} {field}')

print(f'\n共修复 {fixed_count} 个字段')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

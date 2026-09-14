import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 查找2013年公共基础的题目
for q in questions:
    if q['year'] == '2013' and q['bigSubject'] == '公共基础':
        qnum = q.get('yearQnum')
        
        # 2013-3: 参数方程求导
        if qnum == 3:
            q['question'] = '若$\\begin{cases} x = \\cos t \\\\ y = \\sin t \\end{cases}$，则$\\frac{dy}{dx}$等于：（　　）。'
            q['A'] = '$-\\tan t$'
            q['B'] = '$\\tan t$'
            q['C'] = '$-\\sin t$'
            q['D'] = '$\\cot t$'
            q['analysis'] = '参数方程确定的函数的导数。$\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt} = \\frac{\\cos t}{-\\sin t} = -\\cot t$。'
            print('已修复 2013-3')
        
        # 2013-4: 不定积分性质
        elif qnum == 4:
            q['question'] = '设$f(x)$有连续的导数，则下列关系式中正确的是：（　　）。'
            q['A'] = '$\\int f(x)dx = f(x)$'
            q['B'] = '$(\\int f(x)dx)\' = f(x)$'
            q['C'] = '$\\int f\'(x)dx = f(x)$'
            q['D'] = '$(\\int f(x)dx)\' = f(x) + C$'
            q['analysis'] = '不定积分的性质，注意常数C。选项(A)$\\int f(x)dx = F(x) + C$，选项(C)$\\int f\'(x)dx = f(x) + C$，选项(D)$(\\int f(x)dx)\' = f(x)$。'
            print('已修复 2013-4')
        
        # 2013-10: 微分方程
        elif qnum == 10:
            q['question'] = '微分方程$xy\' - y\\ln y = 0$的满足$y(1) = e$的特解是：（　　）。'
            q['A'] = '$y = ex$'
            q['B'] = '$y = e^x$'
            q['C'] = '$y = e^{2x}$'
            q['D'] = '$y = \\ln x$'
            q['analysis'] = '可分离变量微分方程的求解。分离变量为：$\\frac{dy}{y\\ln y} = \\frac{dx}{x}$，积分得$\\ln\\ln y = \\ln x + \\ln C$，即$\\ln y = Cx$，$y = e^{Cx}$，代入初值得$y = e^x$。'
            print('已修复 2013-10')
        
        # 2013-18: 多元函数求导
        elif qnum == 18:
            q['question'] = '若$z = f(x, y)$和$y = \\varphi(x)$均可微，则$\\frac{dz}{dx}$等于：（　　）。'
            q['A'] = '$\\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}$'
            q['B'] = '$\\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y} \\cdot \\frac{d\\varphi}{dx}$'
            q['C'] = '$\\frac{\\partial f}{\\partial y} \\cdot \\frac{d\\varphi}{dx}$'
            q['D'] = '$\\frac{\\partial f}{\\partial x} - \\frac{\\partial f}{\\partial y} \\cdot \\frac{d\\varphi}{dx}$'
            q['analysis'] = '多元函数的求导法则。$\\frac{dz}{dx} = \\frac{\\partial f}{\\partial x} \\cdot 1 + \\frac{\\partial f}{\\partial y} \\cdot \\frac{d\\varphi}{dx}$。'
            print('已修复 2013-18')
        
        # 2013-19: 向量组极大无关组
        elif qnum == 19:
            q['question'] = '已知向量组$\\alpha_1 = (3, 2, -5)^T$，$\\alpha_2 = (3, -1, 3)^T$，$\\alpha_3 = (1, -1, 1)^T$，$\\alpha_4 = (6, -2, 6)^T$，则该向量组的一个极大线性无关组是：（　　）。'
            q['A'] = '$\\alpha_1, \\alpha_2$'
            q['B'] = '$\\alpha_1, \\alpha_3$'
            q['C'] = '$\\alpha_1, \\alpha_2, \\alpha_3$'
            q['D'] = '$\\alpha_1, \\alpha_2, \\alpha_4$'
            q['analysis'] = '向量组极大无关组的判定。2个向量线性无关则不成比例，依次排除后只有C满足。或用初等变换的方法。'
            print('已修复 2013-19')
        
        # 2013-62: 螺钉挤压应力（需要添加配图）
        elif qnum == 62:
            q['question'] = '螺钉承受轴向拉力F，螺钉头与钢板之间的挤压应力是：（　　）。<br><img src="/images/id721_2013_62_1.png" style="max-width:100%;" />'
            q['A'] = '$\\sigma_{bs} = \\frac{4F}{\\pi(D^2 - d^2)}$'
            q['B'] = '$\\sigma_{bs} = \\frac{F}{\\frac{\\pi}{4}d^2}$'
            q['C'] = '$\\sigma_{bs} = \\frac{4F}{\\pi d^2}$'
            q['D'] = '$\\sigma_{bs} = \\frac{4F}{\\pi D^2}$'
            q['analysis'] = '挤压强度计算。挤压面为螺钉头去除螺钉后的面积，则$\\sigma_{bs} = \\frac{F}{\\frac{\\pi}{4}(D^2 - d^2)} = \\frac{4F}{\\pi(D^2 - d^2)}$。'
            print('已修复 2013-62')
        
        # 2013-63: 题号应该是64
        elif qnum == 63:
            q['yearQnum'] = 64
            print('已修复 2013-63 -> 2013-64')
        
        # 2013-90: 逻辑表达式化简（上划线）
        elif qnum == 90:
            q['question'] = '对逻辑表达式$\\overline{AB} + \\overline{A}B + B$的化简结果是：（　　）。'
            q['A'] = '$AB$'
            q['B'] = '$A + B$'
            q['C'] = '$\\overline{A}BC$'
            q['D'] = '$\\overline{A}\\overline{B}C$'
            q['analysis'] = '数字信号的逻辑演算。可以利用$\\overline{AB} = \\overline{A} + \\overline{B}$，$\\overline{A+B} = \\overline{A}\\overline{B}$两个重要公式以及结合律，交换律等进行化简。'
            print('已修复 2013-90')
        
        # 2013-91: 数字信号波形（选项缺失）
        elif qnum == 91:
            q['question'] = '已知数字信号X和数字信号Y的波形如图所示：则数字信号$F = XY$的波形为：（　　）。<br><img src="/images/id1032_2013_91_1.png" style="max-width:100%;" />'
            q['A'] = '<img src="/images/id1032_2013_91_2.png" style="max-width:100%;" />'
            q['B'] = '<img src="/images/id1032_2013_91_3.png" style="max-width:100%;" />'
            q['C'] = '<img src="/images/id1032_2013_91_4.png" style="max-width:100%;" />'
            q['D'] = '<img src="/images/id1032_2013_91_5.png" style="max-width:100%;" />'
            q['analysis'] = '数字信号的逻辑运算。$F = XY$表示逻辑与运算，只有当X和Y都为高电平时，F才为高电平。'
            print('已修复 2013-91')

# 重新排序和分配id
public = [q for q in questions if q['bigSubject'] == '公共基础']
pro = [q for q in questions if q['bigSubject'] == '专业基础']

public.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))
pro.sort(key=lambda x: (x['year'], x.get('yearQnum', 0)))

for i, q in enumerate(public):
    q['id'] = i + 1

pro_start = len(public) + 1
for i, q in enumerate(pro):
    q['id'] = pro_start + i

final = public + pro

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print('\n题库已更新')

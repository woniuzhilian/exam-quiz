import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第113-114页）
new_answers = {
    "2016-34": {"answer": "A", "analysis": "由岩石在压应力作用下的变形和破坏规律和特征可知，当应力超出了岩石的弹性极限后，由于内部微裂纹的产生和扩展，岩石的体积开始增大，进入塑性变形阶段，这是岩石开始发生破坏的标志。"},
    "2017-34": {"answer": "C", "analysis": "主应力面为主应力的作用面，主应力面与主应力方向垂直。由莫尔-库仑强度理论知，α为破裂面与最大主应力面的夹角，有以下右图所示的几何关系可知2α = 90° + φ，则α = 45° + $\\frac{\\varphi}{2}$。"},
    "2018-34": {"answer": "B", "analysis": "蠕变模型一般由三种基本单元组成，分别是描述弹性体的弹性单元、描述理想刚塑性体的塑性单元、描述物体黏性行为的黏性单元，其中弹性单元和塑性单元在力作用下产生的变形都是瞬时变形，与时间无关，只有黏性体才会产生与时间相关的变形。开尔文（Kelvin）模型由弹性单元和黏性单元并联而成。当骤然施加应力时应变速率随着时间逐渐递减。"},
    "2019-39": {"answer": "B", "analysis": "岩石在一定的试验条件下吸收水分的能力，称为岩石的吸水性。常用吸水率、饱和吸水率、含水量与饱水系数等指标表示。岩石的吸水率 $\\omega_a$ 是指岩石试样在大气压力和室温条件下自由吸入水的质量 m$_{w1}$ 与岩样干质量 m$_t$ 之比，一般用百分数表示，即 $\\omega_a = \\frac{m_{w1}}{m_t} \\times 100\\%$"},
    "2020-39": {"answer": "D", "analysis": "饱水系数K$_s$ = $\\frac{\\omega_0}{\\omega_s}$，其中$\\omega_0$ = $\\frac{\\gamma_0-\\gamma_d}{\\gamma_d}$，$\\omega_s$ = $\\frac{\\gamma_s-\\gamma_d}{\\gamma_d}$。则K$_s$ = $\\frac{\\gamma_0-\\gamma_d}{\\gamma_s-\\gamma_d}$ = $\\frac{3}{5}$ = 0.6。"},
    "2021-39": {"answer": "A", "analysis": "岩体中的不连续面是岩体比岩块强度小的最主要原因。"},
    "2022-35": {"answer": "C", "analysis": "岩石三轴抗压强度会随着围压的提高而明显增大，而并不是越小。"},
    "2022补-34": {"answer": "A", "analysis": "岩体结构：断层和结构面附近，地应力分布状态将会受到明显扰动。断层端部、拐角及交汇处出现应力集中；断层带成为应力降低带等。"},
    "2024-34": {"answer": "D", "analysis": "结构面会削弱岩石的整体性和强度，A 选项正确；试件的形状和尺寸会影响抗压强度的测试结果，B 选项正确；加载速度不同，岩石的抗压强度表现也会有所不同，C 选项正确。承压板端部的摩擦力及其刚度不是影响岩石单轴抗压强度的主要因素，D 选项错误。故选 D。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

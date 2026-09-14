import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第20-21页）
new_answers = {
    "2021-12": {"answer": "A", "analysis": "R = $\\arctan|\\frac{\\Delta y}{\\Delta x}|$，由于Δx < 0，Δy > 0，所以 AB 直线的方位角$\\alpha_{AB}$ = 180° − R = 180° − $\\arctan\\frac{15.3}{30.6}$ = 153°26′06″。"},
    "2021-10": {"answer": "D", "analysis": "指标差公式 X = $\\frac{R+L-360°}{2}$。"},
    "2022补-9": {"answer": "A", "analysis": "水平角是测站点至两目标的方向线在水平面上投影的夹二面角。在测量中，把地面上的实际观测角度投影在测角仪器的水平度盘上，然后按度盘读数求出水平角值。水平角是在水平面上由 0-360 度的范围内，按顺时针方向量取 280° -120° =160°"},
    "2022补-10": {"answer": "A", "analysis": "经纬仪的对中误差是指仪器中心与测站点标志中心不在同一铅垂线上所引起的误差。这种误差会导致测量角度时产生偏差。当测站点到目标点的距离较远时，同样的对中误差所引起的角度偏差会较小；反之，当距离较近时，角度偏差会较大。因此，角度偏差与测站点到目标点的距离成反比关系。"},
    "2022补-11": {"answer": "B", "analysis": "视差是指眼睛在目镜端上下移动，所看见的目标有移动。原因是物像与十字丝分划板不共面。消除方法是仔细调节目镜调焦螺旋和物镜调焦螺旋。"},
    "2022补-12": {"answer": "C", "analysis": "经纬仪水平度盘不会随着照准部而转动，只是指针转动；竖直度盘随着望远镜的旋转而转动，指针始终竖直。"},
    "2023-10": {"answer": "C", "analysis": "盘左盘右观测取平均值的方法可以消除：1、可以消除照准部偏心差、照准误差；2、可以消除视准轴不垂直于横轴、横轴不垂直于竖轴和水平读盘偏心差的影响。"},
    "2017-9": {"answer": "A", "analysis": "钢尺精密量距的三项改正为尺长改正、温度改正和倾斜改正。"},
    "2019-12": {"answer": "D", "analysis": "视距测量距离公式为$kl\\cos^2\\alpha$ = 100 * 0.276 * $\\cos^2 5°38'$ = 27.3"},
    "2020-12": {"answer": "C", "analysis": "视线倾斜时的水平距离和高差公式为：D= klcos2α，h= Dtanα+i-v。式中，k 为视距乘常数；v 为中丝读数；i 为仪器高；l 为上下丝的读数称为视矩间隔或尺间隔。则可得：h=Dtanα+i-v=klcos2α×tanα+i-v=$\\frac{1}{2}$kl×2cosαsinα+i-v=$\\frac{1}{2}$klsin2α+i-v"},
    "2023-9": {"answer": "A", "analysis": "量距时，钢尺比标准尺长，会导致读数刻度小于标准刻度，使丈量值小于实际值。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

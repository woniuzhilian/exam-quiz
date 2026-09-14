import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第80-81页）
new_questions = [
    # 第二章 钢结构设计
    {"year": "2016", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "结构钢材牌号Q345C与Q345D主要区别在于（　　）。", "A": "抗拉强度不同", "B": "冲击韧性不同", "C": "含碳量不同", "D": "冷弯角不同"},
    {"year": "2016", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "钢结构轴心受拉构件的刚度指标是（　　）。", "A": "荷载标准值产生的轴向变形", "B": "荷载标准值产生的挠度", "C": "构件的长细比", "D": "构件的自振频率"},
    {"year": "2016", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "图中高强度螺栓摩擦型连接节点时，假设螺栓 A 所受的拉力（　　）【本题配图，PDF第80页】", "A": "$\\frac{Fey_1}{5y_1^2+y_2^2}$", "B": "$\\frac{Fey_1}{2y_1^2+2y_2^2}$", "C": "$\\frac{F}{10}$", "D": "$\\frac{F}{5}$"},
    {"year": "2017", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "结构钢材冶炼和轧制过程中可提高强度的方法是（　　）。", "A": "降低含碳量", "B": "镀锌或镀铝", "C": "热处理", "D": "减少脱氧剂"},
    {"year": "2017", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "设计起重量为Q = 100吨的钢结构焊接工形截面吊车梁且应力变化的循环次数 n ≥ $5 \\times 10^4$次时，截面塑性发展系数取（　　）。", "A": "1.05", "B": "1.2", "C": "1.15", "D": "1.0"},
    {"year": "2017", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "焊接 T 形截面构件中，腹板和翼缘相交处的纵向焊接残余应力为（　　）。", "A": "压应力", "B": "拉应力", "C": "剪应力", "D": "零"},
    {"year": "2018", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "设计我国东北地区露天运行的钢结构焊接吊车梁时宜选用的钢材牌号为（　　）。", "A": "Q235A", "B": "Q345B", "C": "Q235B", "D": "Q345C"},
    {"year": "2018", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "图中所示工形截面简支梁的跨度.截面尺寸和约束条件均相同，根据弯矩图($|M_1| > |M_2|$)可判断整体稳定性最好的是（　　）【本题配图，PDF第81页】", "A": "选项A", "B": "选项B", "C": "选项C", "D": "选项D"},
    {"year": "2018", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "计算拉力和剪力同时作用的普通螺栓连接时，螺栓（　　）。", "A": "抗剪承载力设计值取$N_v^b = 0.9n_f\\mu P$", "B": "承压承载力设计值取$N_c^b = d\\sum t f_c^b$", "C": "抗拉承载力设计值取$N_t^b = 0.8P$", "D": "预拉力设计值应进行折减"},
    {"year": "2019", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "属于碳素结构钢牌号的是（　　）。", "A": "Q345B", "B": "Q460GJ", "C": "Q235C", "D": "Q390A"},
    {"year": "2019", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "设计跨中受集中荷载作用的工作截面简支钢梁的强度时，应计算（　　）。", "A": "梁支座处抗剪强度", "B": "梁跨中抗弯强度", "C": "截面翼缘和腹板相交处的折算应力", "D": "以上三处都要计算"},
    {"year": "2019", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "采用高强度螺栓连接的构件拼接节点中，螺栓的中心间距p应（　　）。", "A": "不小于$1.5d_o$", "B": "不小于$3d_o$", "C": "不大于$3d_o$", "D": "不大于$1.5d_o$"},
    {"year": "2020", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "型号为L160×10 所表示的热轧型钢是（　　）。", "A": "钢板", "B": "不等边角钢", "C": "等边角钢", "D": "槽钢"},
    {"year": "2020", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "在验算普通螺栓连接的钢结构轴心受拉构件强度时，需考虑（　　）。", "A": "板件宽厚比", "B": "螺栓孔对截面的削弱", "C": "残余应力", "D": "构件长细比"},
    {"year": "2020", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "我国常用的高强度螺栓等级有（　　）。", "A": "5.6 级和 8.8 级", "B": "8.8 级和 10.9 级", "C": "4.6 级和 5.6 级", "D": "4.6 级和 8.8 级"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")

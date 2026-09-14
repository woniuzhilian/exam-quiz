import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第82-83页）
new_questions = [
    # 钢结构设计 续
    {"year": "2021", "yearQnum": 28, "smallSubject": "钢结构设计", "question": "设计寒冷地区的钢结构体育场时，不用采用的钢号是（　　）。", "A": "Q420C", "B": "Q345B", "C": "Q235A-F", "D": "Q390B"},
    {"year": "2021", "yearQnum": 29, "smallSubject": "钢结构设计", "question": "计算钢结构桁架下弦受拉杆时，需计算构件的（　　）。", "A": "净截面屈服强度", "B": "净截面稳定性", "C": "主截面屈服强度", "D": "净截面刚度"},
    {"year": "2021", "yearQnum": 30, "smallSubject": "钢结构设计", "question": "采用高强度螺栓的双盖板钢板连接节点如图所示，计算节点受轴心压力 N 作用时，假设螺栓 A 所承受的（　　）【本题配图，PDF第82页】", "A": "压力为 N/8", "B": "剪力为 N/8", "C": "压力为 N/12", "D": "剪力为 N/12"},
    {"year": "2022", "yearQnum": 32, "smallSubject": "钢结构设计", "question": "格构式轴心受压构件在验算其绕虚轴的整体稳定时，采用换算长细比，这是因为（　　）。", "A": "格构式构件的整体稳定承载力高于同截面的实腹式构件", "B": "考虑强度降低的影响", "C": "考虑剪切变形的影响", "D": "考虑单肢失稳对构件承载力的影响"},
    {"year": "2022", "yearQnum": 33, "smallSubject": "钢结构设计", "question": "两块厚度分别为 10mm 和 12mm 的钢板，板宽为 300mm，采用对接焊缝连接，材料为 Q235 钢，没有引弧板，承受静态轴心拉力 400KN，则焊缝应力为（　　）。", "A": "119N/mm²", "B": "121N/mm²", "C": "133N/mm²", "D": "143N/mm²"},
    {"year": "2022补", "yearQnum": 31, "smallSubject": "钢结构设计", "question": "下列钢结构计算阶段荷载设计值与标准值，哪一种符合现行钢结构规范：（　　）。①计算结构或构件的强度、稳定性及连接的强度时，应采用荷载标准值 ②计算结构或构件的强度、稳定性及连接的强度时，应采用荷载设计值 ③计算疲劳和正常使用极限状态时，应采用荷载标准值 ④计算疲劳和正常使用极限状态时，应采用荷载设计值", "A": "①③", "B": "②③", "C": "①④", "D": "②④"},
    {"year": "2022补", "yearQnum": 32, "smallSubject": "钢结构设计", "question": "如下图，摩擦型高强度螺栓连接，螺栓群受弯矩 M 作用，在计算螺栓拉力时，旋转中心应取：（　　）【本题配图，PDF第83页】", "A": "a", "B": "b", "C": "c", "D": "d"},
    {"year": "2023", "yearQnum": 32, "smallSubject": "钢结构设计", "question": "格构式轴心受压构件在验算其绕虚轴的整体稳定时采用换算长细比，这是因为：（　　）。", "A": "格构式构件的整体稳定承载力高于同截面的实腹式构件", "B": "考虑强度降低的影响", "C": "考虑剪切变形的影响", "D": "考虑单肢失稳对构件承载力的影响"},
    {"year": "2023", "yearQnum": 33, "smallSubject": "钢结构设计", "question": "一焊接工字形截面悬臂梁，承受向下的竖向荷载作用，欲保证此梁的整体稳定性，侧向支承应设置在：（　　）。", "A": "上翼缘", "B": "下翼缘", "C": "中和轴", "D": "任意位置"},
    {"year": "2024", "yearQnum": 32, "smallSubject": "钢结构设计", "question": "关于焊接残余应力对结构工作性能的影响，以下叙述错误的是（　　）。", "A": "将降低结构静力破坏荷载", "B": "将较大程度地影响压杆的稳定性", "C": "对低温冷脆的影响经常是决定性的", "D": "对结构的疲劳程度强度有明显不利影响"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")

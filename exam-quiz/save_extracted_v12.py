import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第67-69页）
new_questions = [
    # 地质作用及地质年代 续
    {"year": "2022补", "yearQnum": 43, "smallSubject": "地质作用及地质年代", "question": "河漫滩是在洪水期：（　　）。", "A": "能被淹没的浅滩", "B": "不能被淹没的浅滩", "C": "水的地方能被淹没的浅滩", "D": "水的地方不能被淹没的浅滩"},
    {"year": "2022补", "yearQnum": 44, "smallSubject": "地质作用及地质年代", "question": "按照岩体结构面的成因分类，层间错动面属于：（　　）。", "A": "原生结构", "B": "构造结构", "C": "次生结构", "D": "复合结构"},
    {"year": "2023", "yearQnum": 42, "smallSubject": "地质作用及地质年代", "question": "某岩层出露地面的层序为“新—老—新”，据此判断该处构造为：（　　）。", "A": "向斜构造", "B": "背斜构造", "C": "断层", "D": "破碎带"},
    {"year": "2023", "yearQnum": 43, "smallSubject": "地质作用及地质年代", "question": "靠近山区坡底的洪积土，具有的特点是：（　　）。", "A": "颗粒细小、地下水位较深", "B": "颗粒较粗、地下水位较浅", "C": "颗粒细小、地下水位较浅", "D": "颗粒较粗、地下水位较深"},
    {"year": "2023", "yearQnum": 45, "smallSubject": "地质作用及地质年代", "question": "震级是标准地震仪在距离震中下列哪个数值所记录的最大振幅的对数值：（　　）。", "A": "1km", "B": "10km", "C": "50km", "D": "100km"},
    {"year": "2023", "yearQnum": 46, "smallSubject": "地质作用及地质年代", "question": "河曲的形成是河流地质作用中哪种作用造成的？（　　）。", "A": "向源侵蚀作用", "B": "机械侵蚀作用", "C": "下蚀作用", "D": "侧蚀作用"},
    {"year": "2024", "yearQnum": 42, "smallSubject": "地质作用及地质年代", "question": "若断层面是倾斜的，则在断层面以上的断层盘称为（　　）。", "A": "下盘", "B": "上盘", "C": "下降盘", "D": "上升盘"},
    {"year": "2024", "yearQnum": 43, "smallSubject": "地质作用及地质年代", "question": "河流阶地根据地貌形态特征可分为（　　）。", "A": "堆积阶地、侵蚀阶地、基座阶地", "B": "基座阶地、堆积阶地", "C": "上叠阶地、内叠阶地", "D": "横阶地、纵阶地"},
    {"year": "2024", "yearQnum": 44, "smallSubject": "地质作用及地质年代", "question": "有关下图赤平极射投影中结构面的说法正确的是（　　）【本题配图，PDF第68页】", "A": "DFB 结构面的倾角小于 CKA 结构面的倾角", "B": "CKA 结构面的倾向为 NE", "C": "DFB 结构面与 CKA 结构面交线的倾伏向 SE", "D": "DFB 结构面的倾向为 SW"},
    
    # 第三章 地下水
    {"year": "2016", "yearQnum": 49, "smallSubject": "地下水", "question": "存在干湿交替作用时，侵蚀性地下水对混凝土的腐蚀强度比无干湿交替作用时（　　）。", "A": "相对较低", "B": "相对较高", "C": "不变", "D": "不一定"},
    {"year": "2017", "yearQnum": 48, "smallSubject": "地下水", "question": "每升地下水中以下成分的总量，称为地下水的总矿物度（　　）。", "A": "各种离子、分子与化合物", "B": "所有离子", "C": "所有阳离子", "D": "$Ca^{2+}$、$Mg^{2+}$离子"},
    {"year": "2017", "yearQnum": 49, "smallSubject": "地下水", "question": "利用指示剂或示踪剂来测定地下水流速时，要求钻孔附近的地下水流（　　）。", "A": "水里坡度较大", "B": "水里坡度较小", "C": "呈层流运动的稳定流", "D": "腐蚀性较弱"},
    {"year": "2018", "yearQnum": 48, "smallSubject": "地下水", "question": "粉质粘土层的渗透系数一般在（　　）。", "A": "1cm/s左右", "B": "$10^{-2}$cm/s左右", "C": "$10^{-4}$cm/s", "D": "$10^{-6}$cm/s左右"},
    {"year": "2018", "yearQnum": 49, "smallSubject": "地下水", "question": "通过压水试验，可以确定地下岩土的（　　）。", "A": "含水性", "B": "给水性", "C": "透水性", "D": "吸水性"},
    {"year": "2020", "yearQnum": 48, "smallSubject": "地下水", "question": "在地下水按照矿化度的分类中，淡水的矿化度指标是（　　）。", "A": "< 1 g/L", "B": "< 0.1 g/L", "C": "< 3 g/L", "D": "< 0.3 g/L"},
    {"year": "2022", "yearQnum": 48, "smallSubject": "地下水", "question": "总矿化度是指每升地下水中下列哪种物质（　　）。", "A": "所有离子", "B": "所有阳离子", "C": "$Ca^{2+}$、$Mg^{2+}$", "D": "各种离子、分子、化合物（不含气体）的总和"},
    {"year": "2022补", "yearQnum": 47, "smallSubject": "地下水", "question": "地下水按其埋藏条件可分为哪三类？（　　）。", "A": "包气带水、潜水和承压水", "B": "孔隙水、潜水、裂隙水", "C": "岩溶水、孔隙水、承压水", "D": "包气带水、裂隙水、岩溶水"},
    {"year": "2022补", "yearQnum": 48, "smallSubject": "地下水", "question": "某地基中水对混凝土的腐蚀性按环境类型进行评价时，对硫酸盐可评价为弱腐蚀；对镁盐可评价为弱腐蚀；对苛性碱评价为弱腐蚀；对铵盐评价为弱腐蚀；对总矿化度评价为中等腐蚀，最终评价为：（　　）。", "A": "弱腐蚀", "B": "中等腐蚀", "C": "强腐蚀", "D": "严重腐蚀"},
    {"year": "2023", "yearQnum": 47, "smallSubject": "地下水", "question": "下列几种工程病害，其中哪一项不是由于地下水活动引起的？（　　）。", "A": "地面沉降", "B": "砂土液化", "C": "基坑突涌", "D": "流砂、潜蚀"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")

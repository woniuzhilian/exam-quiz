import json

# 读取已提取的题目
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# 新增题目（第61-63页）
new_questions = [
    # 结构动力反应分析 续
    {"year": "2024", "yearQnum": 26, "smallSubject": "结构动力反应分析", "question": "图示结构中柱的质量不计，阻尼不计。刚性横梁上承受简谐荷载 $Fsin\\theta t$ 的作用，且$\\theta = \\frac{\\sqrt{2}}{2}\\omega$，ω为体系的自振频率，则横梁的振幅为（　　）【本题配图，PDF第61页】", "A": "$\\frac{FL^3}{12EI}$", "B": "$\\frac{FL^3}{15EI}$", "C": "$\\frac{2FL^3}{12EI}$", "D": "$\\frac{FL^3}{4EI}$"},
    
    # 第六部分 工程地质 - 第一章 岩石的成因及分类
    {"year": "2016", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "一种岩石具有以下特征：灰色，结构细腻，硬度比钥匙大且比玻璃小，滴盐酸不起泡，但其粉末滴盐酸微起泡，这是（　　）。", "A": "白云岩", "B": "石灰岩", "C": "石英岩", "D": "玄武岩"},
    {"year": "2016", "yearQnum": 42, "smallSubject": "岩石的成因及分类", "question": "具有交错层理的岩石（　　）。", "A": "砂岩", "B": "页岩", "C": "燧石条带石灰岩", "D": "流纹岩"},
    {"year": "2016", "yearQnum": 43, "smallSubject": "岩石的成因及分类", "question": "上盘相对上升，下盘相对下降的断层（　　）。", "A": "逆断层", "B": "正断层", "C": "平移断层", "D": "阶梯断层"},
    {"year": "2016", "yearQnum": 44, "smallSubject": "岩石的成因及分类", "question": "地质图上表现为中间新、两侧变老的对称分布地层，这种构造通常是（　　）。", "A": "向斜", "B": "背斜", "C": "正断层", "D": "逆断层"},
    {"year": "2017", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "下列岩石中，最容易遇水软化的事（　　）。", "A": "黏土岩", "B": "石英砂岩", "C": "石灰岩", "D": "白云岩"},
    {"year": "2018", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "下列岩石中，最容易遇水软化的是（　　）。", "A": "白云岩", "B": "泥质岩", "C": "石灰岩", "D": "硅质页岩"},
    {"year": "2018", "yearQnum": 42, "smallSubject": "岩石的成因及分类", "question": "下列构造中，不属于沉积岩的构造是（　　）。", "A": "片理", "B": "结核", "C": "斜层理", "D": "波痕"},
    {"year": "2019", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "地壳中含量最多的矿物是（　　）。", "A": "高岭石", "B": "方解石", "C": "长石", "D": "石英"},
    {"year": "2019", "yearQnum": 42, "smallSubject": "岩石的成因及分类", "question": "$SiO_2$含量超过60%，Fe、Mg含量较低的岩浆岩，其颜色通常有如下特征（　　）。", "A": "颜色较浅", "B": "颜色较深", "C": "颜色偏绿", "D": "颜色偏黑"},
    {"year": "2020", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "下列矿物中， 硬度最大的是（　　）。", "A": "正长石", "B": "石英", "C": "白云石", "D": "方解石"},
    {"year": "2021", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "典型情况下，关于方解石和斜长石的异同，不正确一条是（　　）。", "A": "盐酸反应不同", "B": "解理组数不同", "C": "颜色相似", "D": "硬度相近"},
    {"year": "2021", "yearQnum": 42, "smallSubject": "岩石的成因及分类", "question": "下列岩浆岩中，结晶最粗的是（　　）。", "A": "深成岩", "B": "浅成岩", "C": "喷出岩", "D": "岩墙"},
    {"year": "2022", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "沉积岩按其物质成分和结构、构造，可分为（　　）。", "A": "碎屑岩、粘土岩、化学及生物化学岩", "B": "粘土岩、化学岩、生物化学岩", "C": "粘土岩、化学及生物化学岩、生物化学岩", "D": "碎屑岩、生物化学岩、粘土岩"},
    {"year": "2022补", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "下列岩石中，不属于变质的岩石是：（　　）。", "A": "片麻岩", "B": "大理岩", "C": "千枚岩", "D": "白云岩"},
    {"year": "2023", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "按火成岩的化学成分（主要是 $SiO_2$ 的含量）和矿物组成，火成岩分为：（　　）。", "A": "酸性岩、中性岩、浅成岩、超基性岩", "B": "酸性岩、中性岩、基性岩、超基性岩", "C": "中性岩、深成岩、浅成岩、超基性岩", "D": "酸性岩、深成岩、浅成岩、超基性岩"},
    {"year": "2024", "yearQnum": 41, "smallSubject": "岩石的成因及分类", "question": "火成岩分为酸性岩、中性岩、基性岩和超基性岩四类的分类依据是（　　）。", "A": "基质含量", "B": "$SiO_2$ 含量", "C": "$SO_4^{2-}$含量", "D": "岩浆含量"},
]

# 合并
all_questions = extracted + new_questions

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_questions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(all_questions)} 道题")

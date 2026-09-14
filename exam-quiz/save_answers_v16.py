import json

# 读取已提取的答案解析
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 新增答案解析（第34-35页）
new_answers = {
    "2018-20": {"answer": "D", "analysis": "施工组织设计的编制程序：调查、研究、分析（建设地区条件、工程特点、施工条件）→ 主要工种工程量的计算 → 全部工程施工部署 → 各主要项目的施工方案 → 各主要项目的工期 → 各主要项目的直接费用 → 施工总进度计划 → 主要资源供应计划 → 施工总平面图 → 主要技术组织措施 → 主要技术经济指标"},
    "2020-20": {"answer": "B", "analysis": "单位工程施工平面图的设计步骤：1、确定垂直运输机械的布置 2、确定搅拌站、仓库、材料和构件堆场、加工厂的位置 3、布置运输道路 4、布置行政管理、生活福利用临时设施 5、布置水电管线 6、计算技术经济指标"},
    "2022-19": {"answer": "D", "analysis": "施工班组人数要适当，既要满足最小劳动组合人数的要求，同时还要考虑可能安排的施工人数和最小工作面情况，流水步距是两个施工工序之间的时间间隔，与施工人数确定无关。"},
    "2023-19": {"answer": "B", "analysis": "具体评价单位工程施工进度计划的指标主要有：（1）工期，包括总工期、主要施工阶段的工期、计划工期、定额工期或合同工期或期望工期。（2）施工资源的均衡性。施工资源是指劳动力、施工机具、周转材料、建筑材料及施工所需要的人、财、物。"},
}

# 合并
answers.update(new_answers)

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\pro_answers_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)

print(f"已提取 {len(answers)} 道题的答案解析")

import json
import re

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复剩余的平行符号问题
for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue

        original = text

        # 在$内部的// -> \parallel
        def fix_dollar_parallel(m):
            content = m.group(1)
            content = content.replace('//', r'\parallel')
            return '$' + content + '$'

        text = re.sub(r'\$([^$]*//[^$]*)\$', fix_dollar_parallel, text)

        # 不在$中的//（电路并联）-> $\parallel$
        parts = re.split(r'(\$[^$]*\$)', text)
        result = []
        for part in parts:
            if part.startswith('$') and part.endswith('$'):
                result.append(part)
            else:
                part = re.sub(r'([a-zA-Z0-9])\s*//\s*([a-zA-Z0-9])', lambda m: m.group(1) + '$\\parallel$' + m.group(2), part)
                result.append(part)
        text = ''.join(result)

        if text != original:
            q[field] = text
            print(f'修复 {q["year"]}-{q.get("yearQnum")} {field}')

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

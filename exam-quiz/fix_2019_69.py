import json

with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 修复2019-69题
for q in questions:
    if q['year'] == '2019' and q.get('yearQnum') == 69:
        print('当前选项:')
        print('A:', q['A'])
        print('B:', q['B'])
        print('C:', q['C'])
        print('D:', q['D'])
        q['A'] = r'$\frac{F_N}{A}+\frac{1}{W}\sqrt{(M)^2+(T)^2}\leq[\sigma]$'
        q['B'] = r'$\sqrt{\left(\frac{F_N}{A}\right)^2+\left(\frac{M}{W}\right)^2+\left(\frac{T}{2W}\right)^2}\leq[\sigma]$'
        q['C'] = r'$\sqrt{\left(\frac{F_N}{A}+\frac{M}{W}\right)^2+\left(\frac{T}{W}\right)^2}\leq[\sigma]$'
        q['D'] = r'$\sqrt{\left(\frac{F_N}{A}+\frac{M}{W}\right)^2+4\left(\frac{T}{W}\right)^2}\leq[\sigma]$'
        print('\n已修复2019-69所有选项')
        break

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("保存完成")

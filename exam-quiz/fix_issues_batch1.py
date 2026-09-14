import json
import re

# 读取题库
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# 特殊符号转换映射
unicode_to_latex = {
    '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5', '⁶': '^6', '⁷': '^7', '⁸': '^8', '⁹': '^9', '⁰': '^0',
    '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9', '₀': '_0',
    '√': '\\sqrt{}', '∛': '\\sqrt[3]{}', '∜': '\\sqrt[4]{}',
    '∞': '\\infty', '∑': '\\sum', '∏': '\\prod', '∫': '\\int', '∮': '\\oint',
    '∂': '\\partial', '∇': '\\nabla',
    'Δ': '\\Delta', 'δ': '\\delta', 'ε': '\\epsilon', 'ζ': '\\zeta', 'η': '\\eta',
    'θ': '\\theta', 'λ': '\\lambda', 'μ': '\\mu', 'ν': '\\nu', 'ξ': '\\xi',
    'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'τ': '\\tau', 'φ': '\\phi',
    'χ': '\\chi', 'ψ': '\\psi', 'ω': '\\omega',
    'Γ': '\\Gamma', 'Θ': '\\Theta', 'Λ': '\\Lambda', 'Ξ': '\\Xi', 'Π': '\\Pi',
    'Σ': '\\Sigma', 'Φ': '\\Phi', 'Ψ': '\\Psi', 'Ω': '\\Omega',
    '≤': '\\leq', '≥': '\\geq', '≠': '\\neq', '≈': '\\approx', '≡': '\\equiv',
    '±': '\\pm', '×': '\\times', '÷': '\\div',
    '∠': '\\angle', '⊥': '\\perp', '∥': '\\parallel',
    '∵': '\\because', '∴': '\\therefore',
}

def convert_special_chars(text):
    """将Unicode特殊符号转换为LaTeX格式"""
    if not text:
        return text
    
    # 如果已经包含$符号，可能已经是LaTeX，跳过
    # 但需要检查是否有未转换的符号
    
    # 简单替换：将特殊符号用$包裹
    result = text
    for char, latex in unicode_to_latex.items():
        if char in result:
            # 检查是否已经在$...$中
            # 简单处理：直接替换为LaTeX命令，并用$包裹
            result = result.replace(char, f'${latex}$')
    
    return result

def fix_superscript_subscript(text):
    """修复上标下标格式"""
    if not text:
        return text
    
    # 如果已经包含$符号，跳过
    if '$' in text:
        return text
    
    # m2, m3, cm2, cm3, mm2, mm3, kN/m2, kN/m3, N/mm2等
    patterns = [
        (r'(\d+)m(\d)(?!\d|m|c)', r'\1m$^{\2}$'),
        (r'(\d+)cm(\d)(?!\d|m)', r'\1cm$^{\2}$'),
        (r'(\d+)mm(\d)(?!\d)', r'\1mm$^{\2}$'),
        (r'kN/m(\d)(?!\d)', r'kN/m$^{\1}$'),
        (r'N/mm(\d)(?!\d)', r'N/mm$^{\1}$'),
        (r'm(\d)(?!\d|m|c|k|N)', r'm$^{\1}$'),
        (r'cm(\d)(?!\d|m)', r'cm$^{\1}$'),
        (r'mm(\d)(?!\d)', r'mm$^{\1}$'),
    ]
    
    result = text
    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result)
    
    return result

def fix_image_position(text):
    """修复配图位置：将img标签移到文本末尾"""
    if not text or '<img' not in text:
        return text
    
    # 提取所有img标签
    img_tags = re.findall(r'<img[^>]*>', text)
    if not img_tags:
        return text
    
    # 移除所有img标签
    text_without_img = re.sub(r'<img[^>]*>', '', text)
    
    # 清理多余的空白
    text_without_img = re.sub(r'\s+', ' ', text_without_img).strip()
    
    # 将img标签添加到末尾
    result = text_without_img + '<br>' + '<br>'.join(img_tags)
    
    return result

# 处理所有题目
count_special = 0
count_superscript = 0
count_image = 0

for q in questions:
    for field in ['question', 'A', 'B', 'C', 'D', 'analysis']:
        text = q.get(field, '')
        if not text:
            continue
        
        original = text
        
        # 1. 转换特殊符号
        text = convert_special_chars(text)
        
        # 2. 修复上标下标
        text = fix_superscript_subscript(text)
        
        # 3. 修复配图位置（仅题干）
        if field == 'question':
            text = fix_image_position(text)
        
        if text != original:
            q[field] = text
            if field == 'question':
                count_image += 1
            elif any(c in original for c in unicode_to_latex.keys()):
                count_special += 1
            else:
                count_superscript += 1

print(f"转换特殊符号: {count_special} 个字段")
print(f"修复上标下标: {count_superscript} 个字段")
print(f"修复配图位置: {count_image} 个字段")

# 保存
with open(r'D:\应用程序开发\刷题\exam-quiz\src\data\questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n题库已更新")

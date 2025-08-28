#!/usr/bin/env python3
import re

with open('assets/css/main.scss', 'r') as f:
    content = f.read()
    
# 去除注释和字符串
content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
content = re.sub(r'//.*', '', content)
content = re.sub(r'["\'].*?["\']', '', content)

# 统计括号
open_braces = content.count('{')
close_braces = content.count('}')

print(f'开括号: {open_braces}')
print(f'闭括号: {close_braces}')
print(f'匹配: {"是" if open_braces == close_braces else "否"}')

# 检查嵌套结构
stack = []
line_num = 1
for i, char in enumerate(content):
    if char == '\n':
        line_num += 1
    elif char == '{':
        stack.append(line_num)
    elif char == '}':
        if not stack:
            print(f'错误: 第{line_num}行有多余的闭括号')
        else:
            stack.pop()

if stack:
    print(f'错误: 有{len(stack)}个未闭合的开括号')
else:
    print('括号结构正确')

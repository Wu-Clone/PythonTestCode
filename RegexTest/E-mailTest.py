import re

# 示例字符串和正则表达式
string = "example@test.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# 使用 re.fullmatch() 判断字符串是否完全匹配正则表达式
match = re.fullmatch(pattern, string)

# 输出结果
if match:
    print("匹配成功！字符串是一个有效的电子邮箱格式。")
else:
    print("匹配失败！字符串不是一个有效的电子邮箱格式。")

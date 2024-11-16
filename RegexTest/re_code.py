import re
from re import match

from RegexTest.re_utility import draw_a_line, my_match

pattern0 = r"ello"
pattern1 = r"^Hello"
string = "Hello, world!"

# 使用match()
print("尝试从字符串的起始位置匹配一个模式。如果模式在起始位置匹配成功，返回一个匹配的对象，否则返回 None。")
draw_a_line()
m = my_match(pattern0, string)
if m:
    print("匹配成功：", m.group())
else:
    print("匹配失败")
draw_a_line()
m1 = my_match(pattern1, string)
if m1:
    print("匹配成功：", m1.group())
else:
    print("匹配失败")
draw_a_line()

print("re.search() 在整个字符串中搜索模式的首次匹配，找到就返回匹配对象，否则返回 None。")
pattern2 = r'world'
m2 = re.search(string, pattern2)
if m2:
    print("匹配成功", m2.group())
else:
    print("匹配失败")
print("re.search() 会在字符串的任何位置进行搜索，不局限于开头。")
draw_a_line()
print("re.findall() 查找字符串中所有匹配的子串，并以列表形式返回。")
pattern4 = r'\d+'
string4 = "There are 123 apples, 456 oranges, and 789 bananas."
# 使用 findall()
matches = re.findall(pattern4, string4)
print("匹配到的数字:", matches)
draw_a_line()
print("re.sub() 用于替换字符串中匹配正则表达式的部分")
# 示例：替换所有的数字为 "[数字]"
pattern5 = r'\d+'
string5 = "I have 10 apples and 20 oranges."
# 使用 sub() 替换
result = re.sub(pattern5, "[数字]", string5)
print("替换后的字符串:", result)
draw_a_line()
pattern5 = r'\W+'
string5 = "Hello, world! Welcome to Python."

# 使用 split() 分割
result = re.split(pattern5, string5)
print("分割后的列表:", result)
draw_a_line()
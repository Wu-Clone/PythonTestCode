import re

from RegexTest.re_utility import draw_a_line, draw_a_line2

# 在默认情况下， . 不会匹配换行符

pattern = r"hello.world"
string = "hello\nworld"

draw_a_line()
print("String:" + string)
draw_a_line()
print("Pattern:" + pattern)
draw_a_line()
draw_a_line2()
print("开启匹配：")
print(re.match(pattern, string, re.DOTALL))
print("关闭匹配：")
print(re.match(pattern, string))
draw_a_line2()

print("现在测试 如何匹配 .")
print(re.match(r'\.', '.'))
print(re.match(r'\.', 'a'))
print(re.match(r'.', 'a'))
print(re.match(r'.', '.'))
print(r"\. 经过转义，意义是单一的")
draw_a_line2()
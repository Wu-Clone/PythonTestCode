import re
from re import match

from RegexTest.re_utility import draw_a_line

def triple_number(match):
    return str(int(match.group())*3)

text = "The numbers are 10, 20, and 30."
draw_a_line()
print(text)
print(re.sub(r'(\d+)(.+?)(\d+)(.+?)(\d+)',r'\5\2\3\4\1',text))
draw_a_line()
print(text)
print(re.sub(r'(\d+)',triple_number,text))
draw_a_line()
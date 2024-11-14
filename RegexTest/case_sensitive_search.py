import re

string = "123ABc Abc abd"
pattern01 = r"Abc"
pattern02 = r"abc"

print("===================")
print(string + "中")
if re.search(pattern01, string):
    print(pattern01 + "能够找到")
else:
    print(pattern02 + "没找到")
if re.search(pattern02, string):
    print(pattern02 + "能够找到")
else:
    print("没找到")
if re.search(pattern02, string, re.IGNORECASE):
    print("此时忽略大小写")
    print(pattern02 + "找到了")
else:
    print("还是没找到？")
print("===================")
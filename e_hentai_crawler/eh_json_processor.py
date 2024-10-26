import json

# 打开并读取 JSON 文件
with open('ehtags-cn.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

eh_dict = {}
# 遍历并处理数据
for item in data:
    key = item["k"]
    value = item["v"]
    eh_dict[key] = value
print(eh_dict)

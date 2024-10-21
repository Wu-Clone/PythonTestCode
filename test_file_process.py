import re
from collections import defaultdict

def extract_links_from_md(file_path):
    # 定义一个 defaultdict 来存储结果
    result_map = defaultdict(list)
    # 正则表达式匹配 [文字描述](链接) 的格式
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
    # 定义匹配标记内容的正则表达式
    tag_pattern = re.compile(r'\b[a-zA-Z]+-[1-9]+\b')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 查找所有链接
        links = link_pattern.findall(content)
        print("links 的长度 ")
        print(len(links))
        for description, url in links:
            # 查找标记内容
            tags = tag_pattern.findall(description)

            if tags:
                # 清理描述文字，去除标记内容和"来自"子字符串
                cleaned_description = tag_pattern.sub('', description)
                cleaned_description = cleaned_description.replace('- Jable.TV | 免費高清AV在線看 | J片 AV看到飽', '').strip()

                # 将清理后的描述文字和链接组合成一个字符串数组
                entry = [cleaned_description, url]

                # 将标记内容作为 key，描述和链接数组作为 value 添加到 map 中
                for tag in tags:
                    result_map[tag].append(entry)

    return result_map

# 使用示例
file_path = 'C:\\Users\\14296\\Desktop\\FromJable.md'  # 替换为你的 .md 文件路径
result = extract_links_from_md(file_path)

print("字典的长度：" + str(len(result)))
# 打印结果
for tag, entries in result.items():
    print(f"Tag: {tag}")
    for entry in entries:
        print(f"  Description: {entry[0]}")
        print(f"  URL: {entry[1]}")

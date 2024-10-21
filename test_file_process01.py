import re
# TODO 为什么会有没有匹配到的
# TODO 最后将结果保存为什么格式比较合适
# TODO 去重了吗
# TODO 统计文件有多少行
def extract_links_from_md(file_path):
    # 定义一个列表来存储有序结果
    result_list = []

    # 正则表达式匹配 [文字描述](链接) 的格式
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')

    # 定义匹配标记内容的正则表达式
    tag_pattern = re.compile(r'\b[a-zA-Z]+-[1-9]+\b')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("文件行数：" + str(len(content.split("\n"))))
        # 查找所有链接
        links = link_pattern.findall(content)

        for description, url in links:
            # 查找标记内容
            tags = tag_pattern.findall(description)

            if tags:
                # 清理描述文字，去除标记内容和"来自"子字符串
                cleaned_description = tag_pattern.sub('', description)
                # cleaned_description = cleaned_description.replace('来自', '').strip()
                cleaned_description = cleaned_description.replace('- Jable.TV | 免費高清AV在線看 | J片 AV看到飽',
                                                                  '').strip()
                # 将清理后的描述文字和链接组合成一个字符串数组
                entry = [cleaned_description, url]

                # 将标记内容与 entry 按顺序存入列表中
                for tag in tags:
                    result_list.append((tag, entry))

    return result_list

# 使用示例
file_path = 'C:\\Users\\14296\\Desktop\\FromJable.md'  # 替换为你的 .md 文件路径
result = extract_links_from_md(file_path)

# 打印结果
for tag, entry in result:
    print(f"Tag: {tag}")
    print(f"\tDescription: {entry[0]}")
    print(f"\tURL: {entry[1]}")

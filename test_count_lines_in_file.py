import os

def count_lines_in_file(file_name):
    # 使用 'with' 语句打开文件，模式为 'r'，表示以只读模式打开文件。
    # 'encoding' 参数确保文件以 UTF-8 编码读取，避免乱码问题。
    if os.path.exists(file_name):
        # 由于不涉及写入操作，文件不会被锁定（即使其他程序也可以同时读取该文件），因此会更高效
        # 即使在读写文件的过程中发生了异常（例如读取时出错），with open 也会自动关闭文件，避免文件一直占用资源。
        with open(file_name, 'r', encoding='utf-8') as f:
        # 使用 sum() 函数计算文件的行数。
        # '1 for _ in file' 是一个生成器表达式，每读取一行，生成一个 '1'，然后 sum() 对所有 '1' 求和。
        # for _ in file 表示对文件中的每一行进行迭代。_ 是一个占位符变量，表示不关心每一行的具体内容
            line_count = sum(1 for line in f)
        return line_count
    else:
        return -1

# filename = input('Enter file name: ')
filename = 'C:\\Users\\14296\\Desktop\\FromJable.md'  # 替换为你的 .md 文件路径
line_count = count_lines_in_file(filename)
# 使用 f 字符串格式化输出行数
print(f'There are {line_count} lines in {filename}')
import os
# 获取不重复的url链接列表
def get_list(file_name):
    # 使用 'with' 语句打开文件，模式为 'r'，表示以只读模式打开文件。
    # 'encoding' 参数确保文件以 UTF-8 编码读取，避免乱码问题。
    ls = []
    if os.path.exists(file_name):
        # 由于不涉及写入操作，文件不会被锁定（即使其他程序也可以同时读取该文件），因此会更高效
        # 即使在读写文件的过程中发生了异常（例如读取时出错），with open 也会自动关闭文件，避免文件一直占用资源。
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                ls.append(line.strip("\n").strip("\""))
    if len(ls) > 0:
        seen = set()
        ls = [x for x in ls if not (x in seen or seen.add(x))]
    return ls

if __name__ == '__main__':
    ls = get_list(r"D:\code\python\pythonProgramForFun\local\url_list.txt")
    print(ls)
    print(len(ls))

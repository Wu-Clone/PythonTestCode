import requests
import time
import os

def fetch_response(url, headers, retries=3, backoff_factor=1):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers = headers, timeout=20)
            response.raise_for_status()  # 检查是否返回了错误的 HTTP 状态码
            return response
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(backoff_factor * (attempt + 1))  # 指数退避
    print("All attempts failed.")
    return None


def is_filename_exists(directory, filename):
    """
        检查指定目录中是否存在指定文件名。

        :param directory: 文件所在的目录路径
        :param filename: 要检查的文件名
        :return: 如果文件已存在则返回 True，否则返回 False
        """
    # 构建完整路径
    file_path = os.path.join(directory, filename)
    # 检查文件是否存在
    res = os.path.exists(file_path)
    if res:
        print("出现重复")
    return res

def name_a_name(dir, filename, method=0):
    if method == 1:
        time_stamp = time.strftime("%Y%m%d_%H%M%S")
        filename = time_stamp + "_" + filename
    return os.path.join(dir, filename)

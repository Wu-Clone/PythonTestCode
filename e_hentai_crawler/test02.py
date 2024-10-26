from random import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import os
import time

from e_hentai_crawler.get_list import get_list
from get_title import get_title

# 起始URL
start_urls = []

proxies = {
    'http': 'http://127.0.0.1:7897',  # 根据 Clash 的配置调整端口
    'https': 'http://127.0.0.1:7897'
}

def create_dir(start_url):
    # 设置请求头，包括User-Agent（模拟浏览器访问）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.121 Safari/537.36"
    }
    dir_name = get_title(url=start_url)
    # 创建一个存储图片的文件夹
    os.makedirs(dir_name, exist_ok=True)
    return dir_name

# 递归下载图片并访问下一页的函数
def download_images(url, dir_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.121 Safari/537.36"
    }
    # 发送请求并获取网页内容
    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    print(f"正在访问：{url}，状态码：{response.status_code}")

    # 如果状态码为200，继续解析内容
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找id为"img"的 <img> 标签
        img_tag = soup.find('img', id='img')

        # 如果找到了该标签并且其src属性存在
        if img_tag and img_tag.get('src'):
            # 获取图片的URL
            img_url = img_tag.get('src')
            img_name = img_url.split('/')[-1]

            # 下载图片并保存到指定文件夹
            img_response = requests.get(img_url, headers=headers)
            if img_response.status_code == 200:
                with open(dir_name + '//' + img_name, 'wb') as f:
                    f.write(img_response.content)
                    print(f"{img_name} 下载完成")
            else:
                print(f"图片下载失败，状态码：{img_response.status_code}")
        # 延时请求，延时2秒
        # time.sleep(2)
        time.sleep(random())
        # time.sleep(random() * 30)
        # 查找下一页的链接<a id="next" ...>
        next_link = soup.find('a', id='next')
        if next_link and 'href' in next_link.attrs:
            temp_url = next_link['href']
            if url == temp_url:
                print("到最后一页了")
                return
            next_url = temp_url
            print(f"进入下一页：{next_url}")

            # 递归调用函数，继续处理下一页
            download_images(next_url, dir_name)
        else:
            print("没有找到下一页链接，下载结束。")
    else:
        print(f"网页请求失败，状态码：{response.status_code}")


# 开始从起始URL下载
if __name__ == '__main__':
    unique_urls = get_list(r"D:\code\python\pythonProgramForFun\local\url_list.txt")
    for url in unique_urls:
        dir_name = create_dir(url)
        download_images(url, dir_name)
        print("休息一下")
        sleep(10)

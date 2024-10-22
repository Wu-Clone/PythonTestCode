import os
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from ForJableHK import JABLEconstant


def unit_persons_get(href):
    headers = {'User-Agent': JABLEconstant.COMMON_USER_AGENT}
    unit_response = requests.get(href, headers=headers)
    dict_name_link = {}
    if unit_response.status_code == 200:
        soup = BeautifulSoup(unit_response.content, 'html.parser')
        elements = soup.select("#gridThumbs > a")
        print(elements)
        for element in elements:
            text = element.attrs['href']
            dict_name_link[text.split('/')[-1]] = text
    print(f"键值对：{dict_name_link}")
    return dict_name_link


# 主角名称，保存父路径，下载链接
def download_images(name, original_dir, link):
    headers = {'User-Agent': JABLEconstant.COMMON_USER_AGENT}
    pic_links = []
    local_dir = original_dir + "\\" + name
    os.makedirs(local_dir, exist_ok=True)
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        images = soup.find_all("img")
        for img in images:
            img_src = img.get("src")
            # 使用urljoin来处理相对路径，确保图片链接是完整的
            img_url = urljoin(link, img_src)
            if img_url.endswith((".jpg", ".jpeg", ".png", ".gif", ".JPG", ".JPEG", ".PNG")):
                pic_links.append(img_url)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    print(f"获得{name} {len(pic_links)}张图片链接...")
    print("开始下载...")

    for img_url in pic_links:
        print(f"下载：{img_url}")
        img_name = img_url.split("/")[-1].replace("/", "_").replace("\\", "_")
        print(f"图片名称:{img_name}")
        file_path = os.path.join(local_dir, img_name)
        try:
            img_response = requests.get(img_url, headers=headers)
            if img_response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(img_response.content)
                    print(f"{img_name} 下载完成")
            else:
                print(f"无法下载{img_url}，状态码：{img_response.status_code}")
        except Exception as e:
            print(f"下载{img_url}时出错：{e}")
    print(f"{name} 写真下载完毕...")

if __name__ == '__main__':
    # print(unit_persons_get("https://jablehk.com/koreanjapangirls3"))
    download_images('pianono', JABLEconstant.DOWNLOAD_DIR + "\\test", "https://jablehk.com/koreanjapangirls3/pianono")

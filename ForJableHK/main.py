from bs4 import BeautifulSoup
import requests
import os
import JABLEconstant
from ForJableHK.JABLEconstant import KRJP_SELECTOR, BASE_URL
from ForJableHK.unit_persons_get import unit_persons_get, download_images

def start():
    headers = {'User-Agent': JABLEconstant.COMMON_USER_AGENT}
    response = requests.get(BASE_URL, headers=headers)

    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.content, "html.parser")
        # 获取所有需要的元素
        elements = soup.select(KRJP_SELECTOR)
        print(elements)
        hrefs = [BASE_URL + element.get('href') for element in elements if element.get('href')]
        print(f"找到以下链接：{hrefs}")

        for href in hrefs:
            # 进入单个单元
            dict_name_link = unit_persons_get(href)
            for name in dict_name_link:
                link = BASE_URL + dict_name_link[name]
                download_images(name, JABLEconstant.DOWNLOAD_DIR, link)

if __name__ == '__main__':
    start()
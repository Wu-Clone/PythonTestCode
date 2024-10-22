import os

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 输入目标网页的URL
# url = "https://telegra.ph/DJAWA-Photo---Kang-In-kyung-%EA%B0%95%EC%9D%B8%EA%B2%BD---Masked-Pirate-10-05"  # 这里替换成你想要抓取的网页URL
# img_url = "https://jablehk.com/koreanjapangirls2/moon-night-snap-yeon-woo-vol-1"
img_url = "https://jablehk.com/komachi"
save_dir = "D:\\写真\\" + img_url.split('/')[-1]
# 设置请求头，包括User-Agent（模拟浏览器访问）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.121 Safari/537.36"
}

final = []
# 发送请求并获取网页内容
response = requests.get(img_url)
# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找所有img标签
    images = soup.find_all("img")

    # 遍历所有图片，获取每个图片的src属性
    for img in images:
        img_src = img.get("src")
        # 使用urljoin来处理相对路径，确保图片链接是完整的
        img_url = urljoin(img_url, img_src)
        final.append(img_url)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


os.makedirs(save_dir, exist_ok=True)
for img_url in final:
    if img_url.endswith((".jpg", ".jpeg", ".png", ".gif", "JPG")):
        print(f"下载：{img_url}")
        img_name = img_url.split("/")[-1].replace("/","_").replace("\\", "_")
        file_path = os.path.join(save_dir, img_name)
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
    else:
        print(img_url)
        print("跳过")
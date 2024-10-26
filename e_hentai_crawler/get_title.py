import requests
from bs4 import BeautifulSoup
import re

def get_title(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title is not None else "No title found"
        print(title)
    else:
        print("无法获取，状态码：", response.status_code)

    clean_title = re.sub(r'[\/:*?"<>|]', ' ', title)
    # if len(clean_title) > 50:
    #     print(len(clean_title))
    #     clean_title = clean_title[:50]
    print(clean_title)
    return clean_title
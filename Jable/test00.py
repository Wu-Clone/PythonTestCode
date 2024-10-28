import requests
from bs4 import BeautifulSoup
# 测试失败

toplist_url = "https://jable.tv/models/6bb294e56620604f711927a5c269c9ad/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.97 Safari/537.36',
}
response = requests.get(url=toplist_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    pretty_html = soup.prettify()
    print(pretty_html)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
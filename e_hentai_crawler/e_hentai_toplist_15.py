import requests
from bs4 import BeautifulSoup
from soupsieve.pretty import pretty

import my_constant

toplist_url = my_constant.URL_TOPLIST_YESTERDAY
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.121 Safari/537.36"
    }
response = requests.get(url=toplist_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    pretty_html = soup.prettify()
    print(pretty_html)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
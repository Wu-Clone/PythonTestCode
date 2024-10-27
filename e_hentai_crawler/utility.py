import requests
from time import sleep

def fetch_response(url, headers, retries=3, backoff_factor=1):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers = headers, timeout=10)
            response.raise_for_status()  # 检查是否返回了错误的 HTTP 状态码
            return response
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            sleep(backoff_factor * (attempt + 1))  # 指数退避
    print("All attempts failed.")
    return None

import json
import requests
import my_constant

# 配置 API 基本信息
base_url = my_constant.CLASH_URL + ":" + str(my_constant.CLASH_CONTROL_PORT)
secret = my_constant.CLASH_CONTROL_KEY

# 设置请求头
headers = {
    "Authorization": f"Bearer {secret}"
}

# 1. 获取当前节点列表
def get_proxies():
    url = f"{base_url}/proxies"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("获取代理列表失败，状态码：", response.status_code)

# 2. 切换节点
def switch_proxy(group_name, proxy_name):
    url = f"{base_url}/proxies/{group_name}"
    data = {"name": proxy_name}
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 204:
        print(f"切换到节点 {proxy_name} 成功！")
    else:
        print("切换节点失败，状态码：", response.status_code)

# 3. 刷新节点列表
def refresh_proxies():
    url = f"{base_url}/providers/proxies"
    response = requests.put(url, headers=headers)
    if response.status_code == 204:
        print("节点列表已刷新！")
    else:
        print("刷新节点失败，状态码：", response.status_code)

# 示例调用
if __name__ == "__main__":
    proxies = get_proxies()  # 获取代理列表
    if proxies:
        proxies_data = json.dumps(proxies, indent=4, ensure_ascii=False)
        print(proxies_data)

    # 切换到指定节点
    # switch_proxy("Proxy-Group-Name", "Node-Name")  # 将"Proxy-Group-Name"和"Node-Name"替换为实际名称

    # 刷新节点列表
    # refresh_proxies()

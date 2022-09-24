import requests
import random
import json


# Server酱的通知
def notice(state, i):
    serverKey = config[i]["ServerKey"]
    url = 'https://sctapi.ftqq.com/' + serverKey + '.send'
    body = {
        "title": "疫情填报" + state,
        "desp": "尊敬的" + config[i]["name"] + ",你的疫情填报已" + "成功" + "，谢谢您的使用"
    }
    response = requests.request("POST", url, data=body)
    r = response.text


# 提交过程
with open('config.json', 'r+', encoding='utf-8') as f:
    config = json.load(f)
url = "https://ujnpl.educationgroup.cn/jksb/tb/save"

for i in range(5, 6):
    payload = config[i][
                  "id"] + '&ticket=&zx=%E6%98%AF&zx_select=%E6%98%AF&wxwz=%E5%B1%B1%E4%B8%9C%E7%9C%81%E7%83%9F%E5%8F' \
                          '%B0%E5%B8%82%E8%93%AC%E8%8E%B1%E5%8C%BA%E8%93%AC%E8%8E%B1%E9%98%81%E8%A1%97%E9%81%93%E8%93' \
                          '%AC%E8%8E%B1%E5%8D%9A%E6%96%87%E8%8B%91%E5%B0%8F%E5%8C%BA&tw=' + str(
        round(random.uniform(36.0, 36.9), 1)) + '&tw2=' + str(round(random.uniform(36.0, 36.9), 1)) + '&tw5=' + str(
        round(random.uniform(36.0, 36.9), 1)) + '&ks=%E5%90%A6&ks_select=%E5%90%A6&jkm=&xcm=&gtjz1=&gtjz5='
    headers = {
        'Cookie': config[i]["Cookie"],
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 判断是否提交成功
    response = requests.request("POST", url, headers=headers, data=payload)
    if "提交成功" in response.text:
        print(config[i]["name"] + " 提交成功")
        state = "提交成功"
    else:
        print("*****提交失败*****")
        state = "提交失败"

    notice(state, i)

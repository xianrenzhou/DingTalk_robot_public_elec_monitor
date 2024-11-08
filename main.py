import json

import os
import math
import json
import random
import requests
from datetime import datetime
import time
from datetime import timedelta




# 字体随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)

def get_elec(url,payload,headers):
    response = requests.request("POST", url, headers=headers, data=payload)
    elec = response.json()["d"]["data"]["surplus"]
    print(type(elec))
    elecfree = response.json()["d"]["data"]["freeEnd"]
    vtotal = response.json()["d"]["data"]["vTotal"]
    itotal = response.json()["d"]["data"]["iTotal"]
    # 获取当前时间
    current_time = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    # 添加 8 小时
    current_time += timedelta(hours=8)

    # 如果需要，将结果转换为字符串
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    flag = elec < 20
    return f"{current_time_str}  \n付费电量：{elec}\n免费电量：{elecfree}\n电压:{float(vtotal):.2f}\n电流:{float(itotal):.2f}\n功率：{round(float(vtotal) * float(itotal), 2)}",flag


def send_msg(token_dd, msg, at_all=False):
    """
    通过钉钉机器人发送内容
    @param date_str:
    @param msg:
    @param at_all:
    @return:
    """
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token_dd
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    content_str = "你好！\n\n{0}\n".format(msg)
    if at_all:
        content_str = "你好！该交电费了！\n\n{0}\n".format(msg)
    
    data = {
        "msgtype": "text",
        "text": {
            "content": content_str
        },
        "at": {
            "isAtAll": at_all
        },
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    print(res.text)

    return res.text


if __name__ == '__main__':
    token_dd = os.environ['MY_TOKENDD']
    payload = os.environ['MY_PAYLOAD']
    headers = os.environ['MY_HEADERS']
    headers = json.loads(headers)
    url = os.environ['MY_URL']
    wea, temperature = 0,1
    elec_info,flag= get_elec(url,payload,headers)
    print(elec_info,flag)
    send_msg(token_dd, elec_info, flag)

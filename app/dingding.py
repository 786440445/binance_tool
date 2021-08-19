import os, sys
home_dir = os.getcwd()

if home_dir not in sys.path:
    sys.path.append(home_dir)

import requests, json
from app.authorization import dingding_token

class Message:
    def __init__(self) -> None:
        pass

    @staticmethod
    def dingding_warn(text):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % dingding_token
        json_text = Message._msg(text)
        ret = requests.post(api_url, json.dumps(json_text), headers=headers).content

    @staticmethod
    def _msg(text):
        json_text = {
            "at": {
                "atMobiles":[
                    "180xxxxxx"
                ],
                "atUserIds":[
                    "user123"
                ],
                "isAtAll": False
            },
            "text": {
                "content":text
            },
            "msgtype":"text"
        }
        return json_text

if __name__ == "__main__":
    print(Message.dingding_warn("报警：EOSUSDT"))
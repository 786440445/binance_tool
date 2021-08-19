import os, sys
home_dir = os.getcwd()

if home_dir not in sys.path:
    sys.path.append(home_dir)

import requests,json
# windows
from app.authorization import dingding_token, api_secret,api_key
from app.BinanceAPI import BinanceAPI
# linux
# from app.authorization import dingding_token

class Message:
    def __init__(self) -> None:
        pass

    # def buy_limit_msg(self, market, quantity, rate):
    #     try:
    #         res = BinanceAPI(api_key,api_secret).buy_limit(market, quantity, rate)
    #         if res['orderId']:
    #             buy_info = "报警：币种为：{cointype}。买单价为：{price}。买单量为：{num}".format(cointype=market,price=rate,num=quantity)
    #             self.dingding_warn(buy_info)
    #             return res
    #     except BaseException as e:
    #         error_info = "报警：币种为：{cointype},买单失败.api返回内容为:{reject}".format(cointype=market,reject=res['msg'])
    #         self.dingding_warn(error_info)


    # def sell_limit_msg(self,market, quantity, rate):
    #     '''
    #     :param market:
    #     :param quantity: 数量
    #     :param rate: 价格
    #     :return:
    #     '''
    #     try:
    #         res = BinanceAPI(api_key,api_secret).sell_limit(market, quantity, rate)
    #         if res['orderId']:
    #             buy_info = "报警：币种为：{cointype}。卖单价为：{price}。卖单量为：{num}".format(cointype=market,price=rate,num=quantity)
    #             self.dingding_warn(buy_info)
    #             return res
    #     except BaseException as e:
    #         error_info = "报警：币种为：{cointype},卖单失败.api返回内容为:{reject}".format(cointype=market,reject=res['msg'])
    #         self.dingding_warn(error_info+str(res))
    #         return res

    def dingding_warn(self, text):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=09a5f6e8d30c09b600edbf76387b222f1dfb5503d34584c371f6403aeb2f11ff"
        # api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % dingding_token
        json_text = self._msg(text)
        ret = requests.post(api_url, json.dumps(json_text), headers=headers).content

    def _msg(self, text):
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
    msg = Message()
    print(msg.dingding_warn("报警：EOSUSDT"))
# 所有的订单配置文件
import requests
import  sys
sys.path.append(r"E:\PycharmProjects\a.xlsx")
from  diesheng.data.dingdan_duqu   import shuju

class Ding_Dan(object):
    def  Cha_mingxi(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList"
        payload = "{\r\n \"pageNum\": %s,\r\n \"pageSize\": 10,\r\n \"queryTerms\": {\r\n  \"orderType\": \"\",\r\n  \"orderStatus\": \"\",\r\n  \"orderDelayFlag\": \"\",\r\n  \"orderNo\": \"\",\r\n  \"startReportDate\": \"\",\r\n  \"endReportDate\": \"\"\r\n }\r\n}" % (num)
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderList",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "7142731819d68a28427de15602b18ce4",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "96a28135-70c6-4e30-ba71-951f5acf98aa,4c2ef22f-7f9f-4470-a3ad-18863da2c5aa",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=df634bc12d87fb0d152a9852a0fa3f45; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f; dapp.sgm.com:qa:=df634bc12d87fb0d152a9852a0fa3f45; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd",
            'accept-encoding': "gzip, deflate",
            'content-length': "194",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()
        # print(response.text)
if __name__ == '__main__':
    print(Ding_Dan().Cha_mingxi(1))
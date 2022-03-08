import seldom
from page.basic import Basic


class SignPage(seldom.TestCase):
    def __init__(self):
        self.appCode = Basic.APPCODE
        self.url = Basic.URL
        self.headers ={
            "Content-Type": "application/json"
        }

    # def get_data_key(self, size):
    #     """
    #     获取密钥的接口
    #     :param size: 本次生成的密钥数量
    #     :return:
    #     """
    #     # 获取密钥的地址
    #     url = self.url + "/risen-pcip-sm/api/public/api/getDataKey"
    #     body = {
    #         "appCode": self.appCode,
    #         "size": size
    #     }
    #     self.post(url=url, headers=self.headers, json=body)
    #     # 将返回的数据密钥赋值给dataKey
    #     dataKey = self.response['data']
    #     return dataKey

    def sign_data(self, data):
        """
        数据签名接口：三方应用系统调用此服务对数据进行签名操作。签名操作可用来验证数据是否被篡改。
        :param data: 明文数据
        :return: 签名值
        """
        url = self.url + "/risen-pcip-sm/api/public/api/signData"
        body = {
            "appCode": self.appCode,
            "data": data
        }
        self.post(url=url, headers=self.headers, json=body)
        # 赋值签名值
        r_data = self.response['data']
        return r_data

    def verify_data(self, data, signature):
        """
        数据验签接口：提供给三方应用系统，用来验证签名数据。验证数据在流转和存储过程中的真实性。
        :param data:签名数据
        :param signature:签名值
        :return:返回成功或者失败
        """
        url = self.url + "/risen-pcip-sm/api/public/api/verifyData"
        body = {
            "appCode": self.appCode,
            "data": data,
            "signature": signature
        }
        self.post(url=url, headers=self.headers, json=body)
        # 返回
        data = self.response['data']
        return data

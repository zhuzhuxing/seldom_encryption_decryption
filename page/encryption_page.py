import seldom
from page.basic import Basic
from seldom.logging import log

class EncryptionPage(seldom.TestCase):

    def __init__(self):
        # 应用编码
        self.appCode = Basic.APPCODE
        # 设置日志
        self.log = log
        # 数据密钥
        self.dataKey = []
        # 共同的headers
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_data_key(self, size):
        """
        获取密钥的接口
        :param size: 本次生成的密钥数量
        :return:
        """
        # 获取密钥的地址
        url = Basic.URL + "/risen-pcip-sm/api/public/api/getDataKey"

        body = {
            "appCode": self.appCode,
            "size": size
        }
        self.log.debug(f"发送post请求，请求地址{url}, 请求参数{body}")
        self.post(url=url,headers=self.headers,json=body)
        self.log.debug(f"服务器返回结果：{self.response}")
        # 将返回的数据密钥赋值给dataKey
        self.dataKey = self.response['data']
        return self.dataKey

    def encrypt_data(self, dataKey, plaintext_data):
        """
        数据加密接口
        :param dataKey: 数据密钥
        :param plaintext_data: 明文数据
        :return:
        响应参数：{
                 "message":"成功",//当失败时返回原因
                 "data":"b6c4b63f8d3b74813d30830ca7accb3fdbe57d625ddd1615a733d6d64544eaa3",//密文数据
                 "code":200//根据code类型判断本次操作是否成功
                }
        """

        # 数据加密地址
        url = Basic.URL + "/risen-pcip-sm/api/public/api/encryptData"

        body = {
            "appCode": self.appCode,
            "dataKey": dataKey,
            "data": plaintext_data
        }
        self.log.debug(f"发送post请求，请求地址{url}, 请求参数{body}")
        self.post(url=url, headers= self.headers, json=body)
        self.log.debug(f"服务器返回结果：{self.response}")
        return self.response['data']

    def decrypt_data(self, dataKey, ciphertext_data):
        """
        数据解密接口
        :param dataKey:数据密钥
        :param ciphertext_data:密文数据
        :return:
        """
        url = Basic.URL + "/risen-pcip-sm/api/public/api/decryptData"
        body = {
            "appCode": self.appCode,
            "dataKey": dataKey,
            "data": ciphertext_data
        }
        self.log.debug(f"发送post请求，请求地址{url}, 请求参数{body}")
        self.post(url=url, headers=self.headers, json=body)
        self.log.debug(f"服务器返回结果：{self.response}")








import seldom
from page.basic import Basic
from seldom.logging import log

class EncryptionPage(seldom.TestCase):

    def __init__(self):
        # 应用编码
        self.appCode = Basic.APPCODE
        # 设置日志
        self.log = log
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
        if self.response['code'] == 200:
            # 将返回的数据密钥赋值给dataKey
            dataKey = self.response['data']
            return dataKey

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

    def batch_encrypt(self, bath_data):
        """
        批量数据加密:提供给三方应用，进行批量对数据进行加密操作。
        :param bath_data: 明文数据
        :return:data(返回加密后的明文)
        """
        url = Basic.URL + "/risen-pcip-sm/api/public/api/batchEncrypt"
        body = {
            "appCode": self.appCode,
            "batchData": bath_data
        }
        self.post(url=url, headers=self.headers, json=body)
        # 将返回的密文数据赋值给data
        data = self.response['data']
        return data

    def batch_decrypt(self, bath_data):
        """
        批量数据解密接口：对大量密文数据进行批量解密，提高三方应用系统的解密效率
        :param bath_data:
        :return:data(返回解密后的密文)
        """
        url = Basic.URL + "/risen-pcip-sm/api/public/api/batchDecrypt"
        body = {
            "appCode": self.appCode,
            "batchData": bath_data
        }
        self.post(url=url, headers=self.headers, json=body)
        # 将解密后的明文数据赋值给data[]
        data = self.response['data']
        return data

    def hash_data(self, data):
        """
        不可逆加密:不可逆加密是指数据哈希。数据哈希使用的是sm3算法，具备有不可逆性，
        因此使用该算法进行加密的数据是那些不需要再进行解密的数据。该方法不需要使用数据密钥。
        常用此接口加密的数据例如用户的登录密码。
        :param data:明文数据
        :return:data 加密后的明文数据
        """
        url = Basic.URL + "/risen-pcip-sm/api/public/api/hashData"
        body = {
            "appCode": self.appCode,
            "data": data
        }
        self.post(url=url, headers=self.headers, json=body)
        # 将加密后的明文数据赋值给data
        data = self.response['data']
        return data











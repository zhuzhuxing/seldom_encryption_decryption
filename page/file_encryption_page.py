import seldom
from seldom.logging import log
from page.basic import Basic
from page.utils import Utils

class FileEncryptionPage(seldom.TestCase):

    def __init__(self):
        self.appCode = Basic.APPCODE
        self.headers = {
            "Content-Type": "application/json"
        }
        self.log = log
        self.utils = Utils()

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
        dataKey = self.response['data']
        return dataKey

    def encrypt_file(self, data_key, file_content):
        """
        文件加密接口:了保证存储安全，服务器内部存放的文件应该都是密文，
        因此在文件的收发文过程产生的文件，都应该进行加密，使文件以密文的形式在服务器上存储。
        将文件BASE64编码后调用接口服务进行加密操作,文件超过4MB建议使用本地API方法。
        :param data_key:数据密钥
        :param file_content:"BASE64编码文件内容"//明文BASE64编码
        :return:
        """
        url = Basic.URL + "/risen-pcip-sm/api/public/api/encryptFile"
        # 将传入的文件进行base64加密
        file_base64 = self.utils.file_base64(file_path=file_content)
        body = {
            "appCode": self.appCode,
            "dataKey": data_key,
            "fileContent": file_base64
        }
        self.post(url=url, headers=self.headers, json=body)
        # 返回BASE64编码文件内容
        return self.response['data']

    def decrypt_file(self, data_key, file_content):
        """
        文件解密接口:三方应用在服务器上存储的是加密后的文件，当三方
        应用需要查看文件内容时，必须调用文件的解密接口将文件解密。
        :param data_key:数据密钥
        :param file_content:BASE64文件编码内容"//密文BASE64编码
        :return:
        """
        url = Basic.URL + "/risen-pcip-sm/api/public//api/decryptFile"
        body = {
            "appCode": self.appCode,
            "dataKey": data_key,
            "fileContent": file_content
        }
        self.post(url=url, headers=self.headers, json=body)
        # 返回BASE64文件编码
        return self.response['data']
import seldom
from page.encryption_page import EncryptionPage
from seldom import file_data

class TestEncryption(seldom.TestCase):
    """加解密"""

    def start(self):
        # 获取应用编码
        self.en = EncryptionPage()
        
    # @seldom.data([[2],[3],[4]])
    # @file_data(file='get_key.json', key='size')
    def test_01_get_data_key(self, size=2):
        """
        测试获取密钥
        :param size: 获取密钥的个数
        :return:
        """
        self.en.get_data_key(int(size))
        self.assertStatusCode(200)
        self.en.log.debug(f"返回的密钥{self.en.dataKey}")

    # @seldom.depend
    # def test_02_encrypt_data(self, plaintext_data='123'):
    #     """
    #     测试明文数据加密
    #     :param dataKey:密钥
    #     :param plaintext_data:明文数据
    #     :return:
    #     """
    #     dataKey = self.en.dataKey
    #     self.en.encrypt_data(dataKey[0], plaintext_data)





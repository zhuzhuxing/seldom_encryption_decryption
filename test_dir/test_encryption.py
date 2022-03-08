import seldom
from page.encryption_page import EncryptionPage
from seldom import file_data


class TestEncryption(seldom.TestCase):
    """加解密"""

    def start(self):
        self.en = EncryptionPage()

    # @seldom.data([[2],[3],[4]])
    @file_data(file='get_key.json', key='normal_size')
    def test01_get_data_key(self, case, size):
        """
        测试获取密钥:正向用例
        :param size: 获取密钥的个数
        :return:
        """
        self.en.log.debug(case)
        self.en.get_data_key(size)
        self.assertStatusCode(200)
        # 获得密钥的个数
        total = len(self.response['data'])
        self.assertEqual(total, size)
        self.en.log.debug(f"返回的密钥{self.response['data']}")

    @file_data(file='get_key.json', key='abnormal_size')
    def test02_get_data_key(self,case, size):
        """
        测试获取密钥:异常用例
        :param size: 获取密钥的个数
        :return:
        """
        self.en.log.debug(case)
        self.en.get_data_key(size)
        self.assertStatusCode(200)
        # 获得密钥的个数
        print(self.response)


    @file_data(file='encrypt_data.json', key="plaintext_data")
    def test_encrypt_data(self, plaintext_data):
        """
        测试明文数据加密
        :param dataKey:密钥
        :param plaintext_data:明文数据
        :return:
        """
        dataKey = self.en.get_data_key(size=2)
        self.en.encrypt_data(dataKey[0]['dataKey'], plaintext_data)
        self.en.log.debug(f"加密后的明文数据{self.en.response['data']}")
        self.assertStatusCode(200)

    @file_data(file='encrypt_data.json', key='plaintext_data')
    def test_decrypt_data(self, plaintext_data):
        """解密"""
        # 获取密钥datakey
        datakeys = self.en.get_data_key(size=2)
        dataKey = datakeys[0]['dataKey']
        # 获取加密后的明文数据
        data = self.en.encrypt_data(dataKey, plaintext_data)
        # 解密
        self.en.decrypt_data(dataKey, data)
        # 解密后的明文数据
        data_ = self.en.response['data']
        self.assertEqual(data_, plaintext_data)
        self.en.log.debug(f"解密后的明文数据{self.en.response['data']}")



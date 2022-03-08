import seldom
from page.encryption_page import EncryptionPage
from seldom import file_data

class TestBatchEncryption(seldom.TestCase):
    """批量加解密"""

    def start(self):
        self.en = EncryptionPage()

    @file_data(file='batch_encrypt.json', key='bath_data')
    def test_batch_encrypt(self, case, data, excepted):
        """
        批量加密接口
        :param data:
        :return:
        """
        self.en.log.debug(case)
        # 获取密钥列表
        datakeys = self.en.get_data_key(len(data))
        print(datakeys)
        # 加密的body_data
        bath_data = []
        for i in range(len(data)):
            # 在bath_data中增加dataKey和IDCard
            bath_data.append({'dataKey': datakeys[i]['dataKey'], f"IDCard{i+1}": data[i]})

        self.en.batch_encrypt(bath_data)
        # 判断加密后的明文个数是否和密文个数相等
        self.assertEqual(len(self.response['data']), excepted)

    @file_data(file='bath_decrypt.json', key='data')
    def test_batch_decrypt(self, data):
        """
        批量解密接口
        :param data: 明文数据
        :return:
        """
        # 获取所有的密钥并且把密钥存到dataKeys里
        dataKeys = self.en.get_data_key(len(data))
        # 定义解密的body
        bath_body = []
        for i in range(len(data)):
            # 将dataKeys和IDcard遍历进解密的body里
            bath_body.append({'dataKey': dataKeys[i]['dataKey'], f"IDCard{i+1}": data[i]})
        # 执行解密接口
        self.en.batch_encrypt(bath_body)
        # 将解密后的数据保存encrypt_data中
        encrypt_data = self.response['data']
        # 定义解密的body
        encrypt_body = []
        for i in range(len(data)):
            # 将密钥和加密后的数据遍历到定义解密的body中
            encrypt_body.append({'dataKey':dataKeys[i]['dataKey'], f"IDCard{i+1}": encrypt_data[i][f"IDCard{i+1}"]})
        # 执行解密接口
        self.en.batch_decrypt(encrypt_body)
        # 将解密的数据存放到decrypt_data中
        decrypt_data = self.response['data']
        for i in range(len(data)):
            # 遍历断言加密前的明文数据是否和加密后的明文数据相等
            self.assertEqual(data[i], decrypt_data[i][f"IDCard{i+1}"])



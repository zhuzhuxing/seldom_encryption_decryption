import seldom
from seldom import file_data
from page.utils import Utils
from page.file_encryption_page import FileEncryptionPage

class TestFileEncryption(seldom.TestCase):
    """文件加解密"""

    def start(self):
        self.en = FileEncryptionPage()

    @file_data(file='entry_file.json', key="file")
    def test_encrypt_file(self, case, file):
        """文件加密接口测试"""
        self.en.log.debug(case)
        dataKeys = self.en.get_data_key(1)
        dataKey = dataKeys[0]['dataKey']
        # 文件编码后的内容
        self.en.encrypt_file(data_key=dataKey, file_content=file)
        data_base64 = self.en.encrypt_file(data_key=dataKey, file_content=file)
        self.assertStatusCode(200)
        self.en.log.debug(f'文件加密后的内容编码为{data_base64}')


    @file_data(file='decrypt.json', key='file')
    def test_decrypt_file(self, case, re_file):
        """文件解密接口测试"""
        self.en.log.debug(case)
        dataKeys = self.en.get_data_key(1)
        dataKey = dataKeys[0]['dataKey']
        # 文件编码后的内容
        data_base64 = self.en.encrypt_file(data_key=dataKey, file_content=re_file)
        self.en.log.debug(f'文件加密后的内容编码为{data_base64}')
        # 文件解密
        data = self.en.decrypt_file(data_key=dataKey, file_content=data_base64)
        # 由于文件解密为也为base64编码文件,所以将传入文件先加密
        re_file_base64 = self.en.utils.file_base64(file_path=re_file)
        self.assertEqual(data, re_file_base64)
        self.assertStatusCode(200)





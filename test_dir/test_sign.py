import seldom
from seldom import file_data
from page.sign_page import SignPage

class TestSign(seldom.TestCase):
    """数据签名"""

    def start(self):
        self.en = SignPage()

    @file_data(file='encrypt_data.json', key="plaintext_data")
    def test_sign_data(self, data):
        """
        数据签名接口
        :param data:签名数据
        :return:
        """
        self.en.sign_data(data)
        self.assertEqual(self.response['message'], '成功')
        self.assertStatusCode(200)

    @file_data(file='encrypt_data.json', key="plaintext_data")
    def test_verify_data(self, data):
        """
        数据验签接口
        :param data:签名数据
        :return
        """
        # 获取签名值
        signature= self.en.sign_data(data)
        # 验签接口返回为boolean类型
        data = self.en.verify_data(data, signature)
        self.assertEqual(data, True)
        self.assertTrue(data)




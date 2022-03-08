import base64

class Utils:

    def file_base64(self, file_path):
        """
        将文件转换成base64编码
        :param file_path:文件路径
        :return:编码后的文件
        """
        with open(file=file_path, mode='rb') as file:
            base64_str = base64.b64encode(file.read())
            src = base64_str.decode('utf-8')
            return src



if __name__ == '__main__':
    util = Utils()
    str_base64 = util.file_base64(file_path='../test_data/data.json')
    print(str_base64)



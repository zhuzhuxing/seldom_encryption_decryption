import seldom
from page.encryption_page import EncryptionPage

if __name__ == '__main__':
    # run test file
    # seldom.main("./test_dir/test_sample.py")
    # run test dir
    # seldom.main("./test_dir/test_encryption.py")
    # seldom.main("./test_dir/")
    en = EncryptionPage()
    data = en.get_data_key(1)
    print(data)


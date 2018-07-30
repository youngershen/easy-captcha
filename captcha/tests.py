# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
import unittest
from captcha import Captcha


class CaptchaTestCase(unittest.TestCase):
    def setUp(self):
        self.captcha = Captcha()

    def test_simple(self):
        self.captcha.get_file('hello', './test.png')


if __name__ == '__main__':
    unittest.main()
# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
from unittest import TestCase
from .captcha import Captcha


class CaptchaTestCase(TestCase):
    def setUp(self):
        pass

    def test_alphabet(self):
        captcha = Captcha(font=['a'], style=Captcha.STYLE_SIMPLE, format=Captcha.FORMAT_PNG)

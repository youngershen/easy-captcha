# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : Younger Shen
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
import os
from pathlib import Path
from unittest import TestCase
from .captcha import Captcha, SinaCaptcha, SimpleCaptcha, SimpleChineseCaptcha


class CaptchaTestCase(TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(__file__)
        self.captcha = Captcha()

    def test_load_font(self):
        path = Path(os.path.join(self.base_dir, 'fonts/RexBoldInline.otf'))
        font = self.captcha._load_font(path=path)
        self.assertTrue(font)

        font = self.captcha._load_font(name='RexBoldInline.otf')
        self.assertTrue(font)

        font = self.captcha._load_rand_font()
        self.assertTrue(font)

    def test_make_sina_captcha(self):
        captcha = SinaCaptcha()
        captcha = captcha.make_captcha(string='ABCD')
        captcha.save('test-sina.png')
        self.assertTrue(captcha)

    def test_make_simple_captcha(self):
        captcha = SimpleCaptcha()
        captcha = captcha.make_captcha(string='ABCD')
        captcha.save('test-simple.png')
        self.assertTrue(captcha)

    def test_make_simple_chinese_captcha(self):
        captcha = SimpleChineseCaptcha()
        captcha = captcha.make_captcha(string='我爱中国')
        captcha.save('test-simple-chinese.png')
        self.assertTrue(captcha)

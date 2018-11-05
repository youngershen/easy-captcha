# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
import os
from pathlib import Path
from unittest import TestCase
from .captcha import Captcha


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
        captcha = self.captcha.make_sina_captcha(string='ABCDEF')
        captcha.save('aa.png')

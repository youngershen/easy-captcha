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

        font = self.captcha._load_font()
        self.assertTrue(font)

    def test_make_char_image(self):
        font = self.captcha._load_font(name='RexBoldInline.otf')
        color = self.captcha._get_rand_color()
        image = self.captcha._make_char_image('A', font, color)
        image = self.captcha._rand_rotate_image(image)
        image = image.resize(size=(100, 50))
        self.assertTrue(image)
        image.save('a.png')

    def test_make_sina(self):
        font = self.captcha._load_font(name='RexBoldInline.otf')
        image = self.captcha._make_sina('ABCDEF2324DF', font, None, None, size=(200, 100))
        self.assertTrue(image)
        image.save('sina.png')

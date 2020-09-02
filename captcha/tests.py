# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen/

import os
import sys
from pathlib import Path
import unittest

path = os.path.abspath('.')
sys.path.append(path)


class GeneratorTestCase(unittest.TestCase):
    def setUp(self):
        from captcha.generator import BaseGenerator
        self.base_dir = os.path.dirname(__file__)
        self.base_generator = BaseGenerator()
        self.make_assets_dir()

    @staticmethod
    def make_assets_dir():
        p = os.path.join(path, 'assets')
        if not os.path.isdir(p):
            os.mkdir(p)

    def test_load_font(self):
        p = Path(os.path.join(self.base_dir, 'fonts/RexBoldInline.otf'))
        font = self.base_generator._load_font(path=p)
        self.assertTrue(font)

        font = self.base_generator._load_font(name='RexBoldInline.otf')
        self.assertTrue(font)

        font = self.base_generator._load_rand_font()
        self.assertTrue(font)

    def test_make_default_generator(self):
        from captcha import DefaultGenerator
        generator = DefaultGenerator()
        captcha = generator.make_captcha(string='ABCD')
        captcha.save('assets/test-default.png')
        self.assertTrue(captcha)

    def test_make_simple_captcha(self):
        from captcha import SimpleGenerator
        captcha = SimpleGenerator()
        captcha = captcha.make_captcha(string='ABCDEFG')
        captcha.save('assets/test-simple.png')
        self.assertTrue(captcha)

    def test_make_simple_chinese_captcha(self):
        from captcha import SimpleChineseGenerator
        captcha = SimpleChineseGenerator()
        captcha = captcha.make_captcha(string='我爱中国')
        captcha.save('assets/test-simple-chinese.png')
        self.assertTrue(captcha)

    # def test_make_controt_captcha(self):
    #     from captcha import ContortGenerator
    #     captcha = ContortGenerator()
    #     captcha = captcha.make_captcha(string='ABCD')
    #     captcha.save('assets/test-contront.png')
    #     self.assertTrue(captcha)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)

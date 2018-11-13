# PROJECT : hhcms
# TIME : 18-7-30 下午4:03
# AUTHOR : Younger Shen
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
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

    def test_load_font(self):
        path = Path(os.path.join(self.base_dir, 'fonts/RexBoldInline.otf'))
        font = self.base_generator._load_font(path=path)
        self.assertTrue(font)

        font = self.base_generator._load_font(name='RexBoldInline.otf')
        self.assertTrue(font)

        font = self.base_generator._load_rand_font()
        self.assertTrue(font)

    def test_make_sina_generator(self):
        from captcha.generator import SinaGenerator
        generator = SinaGenerator()
        captcha = generator.make_captcha(string='ABCD')
        captcha.save('test-sina.png')
        self.assertTrue(captcha)

    def test_make_simple_captcha(self):
        from captcha.generator import SimpleGenerator
        captcha = SimpleGenerator()
        captcha = captcha.make_captcha(string='ABCD')
        captcha.save('test-simple.png')
        self.assertTrue(captcha)

    def test_make_simple_chinese_captcha(self):
        from captcha.generator import SimpleChineseGenerator
        captcha = SimpleChineseGenerator()
        captcha = captcha.make_captcha(string='我爱中国')
        captcha.save('test-simple-chinese.png')
        self.assertTrue(captcha)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)

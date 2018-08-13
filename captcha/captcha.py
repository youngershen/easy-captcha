# PROJECT : easy-captcha
# TIME : 18-7-30 下午4:00
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
from PIL import Image, ImageDraw


class Captcha:
    font = None
    font_size = 30
    width = 60
    height = 30
    border = 1
    text = 'hello world'
    confuse_level = 0
    confuse_type = 'simple'

    def __init__(self):
        pass

    def get_image(self, text):
        self.text = text
        captcha = self._get_captcha()
        return captcha

    def get_file(self, text, path):
        self.text = text
        captcha = self._get_captcha()
        captcha.save(path)

    @property
    def image_size(self):
        return self.width, self.height

    def _confuse(self):
        pass

    def _confuse_simple(self):
        pass

    def _get_captcha(self):
        image = Image.new(mode="RGB", size=self.image_size, color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        # draw.text((self.border, self.border), self.text, font=self.font, fill="#000")
        draw.text((self.border, self.border), self.text, fill="#000")
        return image

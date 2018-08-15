# PROJECT : easy-captcha
# TIME : 18-7-30 下午4:00
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
from PIL import Image, ImageDraw, ImageFont


class Captcha:
    FONT_DEFAULT = ''

    FILE_FORMAT_JPG = 'jpg'
    FILE_FORMAT_PNG = 'png'
    FILE_FORMAT_GIF = 'gif'

    STYLE_ZERO = 0
    STYLE_ONE = 1
    STYLE_TWO = 2

    DISTORTION_LEVEL_ZERO = 0
    DISTORTION_LEVEL_ONE = 1
    DISTORTION_LEVEL_TWO = 2

    IMAGE_MODE = 'L'

    def get_file(self, text, path=None):
        image = self._get_image(text)
        image.save(path, self.file_format)
        return image

    def get_object(self, text):
        return self._get_image(text)

    def __init__(self, size, font=None, file_format='png', style=0, distortion_level=0):
        self.size = size
        self.font = font
        self.file_format = file_format
        self.style = style
        self.distortion_level = distortion_level

    def _get_image(self, text):
        image = Image.new(self.IMAGE_MODE, self.size)
        self._fill_image(image)
        self._text_image(text, image)
        return image

    def _text_image(self, text, image):
        font = ImageFont.truetype(self.font, self.font_size)
        d = ImageDraw.Draw(image)
        d.text((0, 0), text, font=font, fill=())

    def _fill_image(self, image):
        pass

    @property
    def _xy(self):
        return (1, 2)

    @property
    def _color(self):
        return (3, 4)

# PROJECT : easy-captcha
# TIME : 18-7-30 下午4:00
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEBSITE : www.punkcoder.cn
import os
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageColor


class BaseError(Exception):
    message = None

    def __str__(self):
        return self.message


class CreateCaptchaFailedError(BaseError):
    message = 'create captcha image failed.'


class FontNotFoundError(BaseError):
    message = 'the required font is not found.'


class StringIsNoneError(BaseError):
    message = 'the captcha string is none.'


class Captcha:
    FONT_SIZE = 100
    FONT_PADDING = 30

    FMT_PNG = 0
    FMT_JPEG = 1
    FMT_GIF = 2
    FMT_PIL_IMAGE = 3

    FONTS = [
        'RexBoldInline.otf',
        'TruenoBdOlIt.otf'
    ]

    # https://passport.baidu.com/cgi-bin/genimage?tcGaf07c1c76092c1b5024d15be4301997fc63f4307bb017ec7
    STYLE_BAIDU = 0
    # https://login.sina.com.cn/cgi/pin.php
    STYLE_SINA = 1

    NOISE_0 = 0
    NOISE_1 = 1
    NOISE_2 = 2

    def __init__(self):
        self.size = (200, 50)
        self.fmt = self.FMT_PNG
        self.style = self.STYLE_SINA
        self.noise = self.NOISE_0

    def get_image(self,
                  string: str=None,
                  font_path: Path=None,
                  font_name: str= None,
                  size: tuple=None,
                  fmt: int=None,
                  style: int=None,
                  noise: int=None):

        if string:
            image = self._get_image(string=string,
                                    font_path=font_path,
                                    font_name=font_name,
                                    size=size,
                                    fmt=fmt,
                                    style=style,
                                    noise=noise)
            return image
        else:
            raise StringIsNoneError()

    def _get_image(self, **kwargs):
        string = kwargs.get('string', '')
        font_path = kwargs.get('font_path', None)
        font_name = kwargs.get('font_name', None)
        size = kwargs.get('size', self.size)
        fmt = kwargs.get('fmt', self.fmt)
        style = kwargs.get('style', self.style)
        noise = kwargs.get('noise', self.noise)

        if font_path or font_name:
            font = self._load_font(path=font_path, name=font_name)
        else:
            font = None

        if style == self.STYLE_BAIDU:
            font = self._load_font(name='') if not font else font
            return self._make_baidu(string, font, fmt, noise)

        if style == self.STYLE_SINA:
            font = self._load_font(name='RexBoldInline.otf') if not font else font
            return self._make_sina(string, font, fmt, noise, size)

    def _make_baidu(self, string, font, fmt, noise):
        return ''

    def _make_sina(self, string, font, fmt, noise, size):
        bg_color = self._get_color('rgb(255,255,255)')
        bg_size = self._get_backgound_size(font, string)
        bg_image = self._make_background(size=bg_size, color=bg_color)
        image = self._make_sina_image(string, bg_image, font)
        image = image.resize(size=size)
        return image

    def _make_sina_image(self, string, bg_image, font):
        font_gap = 0
        for i, char in enumerate(string):
            font_color = self._get_rand_color()
            char_image = self._make_char_image(char, font, font_color)
            char_image = self._rand_rotate_image(char_image)
            font_gap = font_gap if 0 == i else font_gap + char_image.size[0]
            bg_image.paste(char_image, box=(font_gap, 0), mask=char_image)

        return bg_image

    def _load_font(self, path=None, name=None, index=0, encoding='', layout_engine=None):
        if path:
            p = Path(path)
            f = self._get_font_path(p)
        elif name:
            fp = self._get_font(name)
            f = self._get_font_path(font=fp)
        else:
            f = self._load_rand_font()

        font = ImageFont.truetype(font=f,
                                  size=self.FONT_SIZE,
                                  index=index,
                                  encoding=encoding,
                                  layout_engine=layout_engine)
        return font

    def _load_rand_font(self):
        import random
        i = random.randrange(0, len(self.FONTS))
        f = self._get_font(self.FONTS[i])
        font = self._get_font_path(font=f)
        return font

    def _get_font(self, name):
        path = os.path.join(self._base_dir(), 'fonts', name)
        return Path(path)

    def _rand_rotate_image(self, image):
        angel = random.randint(0, 360)
        image = self._rotate_image(image, angel)
        return image

    @staticmethod
    def _get_rand_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return 'rgb({R}, {G}, {B})'.format(R=r, G=g, B=b)

    @staticmethod
    def _get_color(color):
        return ImageColor.getrgb(color)

    @staticmethod
    def _make_background(size, color):
        image = Image.new('RGBA', size=size, color=color)
        return image

    def _add_random_line_to_background(self, image):
        pass

    def _add_dots_to_background(self, image):
        pass

    def _make_char_image(self, char, font, color):
        size = self._get_font_size(font, char)
        image = Image.new(mode='RGBA', size=size)
        draw = ImageDraw.Draw(image)
        draw.text((self.FONT_PADDING / 2, self.FONT_PADDING / 2), char, font=font, fill=color)
        return image

    def _get_font_size(self, font, char):
        size = font.getsize(char)
        width = size[0] + self.FONT_PADDING
        height = size[1] + self.FONT_PADDING
        return width, height

    def _get_backgound_size(self, font, string):
        width = 0
        height = 0
        for c in string:
            width = width + self._get_font_size(font, c)[0]
            height = self._get_font_size(font, c)[1]

        return width, height

    @staticmethod
    def _rotate_image(image, angel=0):
        return image.rotate(angel)

    @staticmethod
    def _resize_image(image, size=None):
        return image.resize(size)

    @staticmethod
    def _base_dir():
        path = os.path.dirname(__file__)
        return path

    @staticmethod
    def _get_font_path(font: Path=None):
        if font.exists():
            return str(font)
        else:
            raise FontNotFoundError()

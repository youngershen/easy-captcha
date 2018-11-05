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
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter


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
    FONTS = [
        'RexBoldInline.otf',
        'TruenoBdOlIt.otf'
    ]

    def __init__(self):
        self.size = (100, 40)

    # https://login.sina.com.cn/cgi/pin.php
    def make_sina_captcha(self, string: str=None, font_size: int=32, image_size: tuple=None):
        captcha = self._make_sina_captcha(string, font_size)
        size = image_size if image_size else self.size
        # captcha = self._resize_image(captcha, size)
        return captcha

    def _make_sina_captcha(self, string, font_size):
        font_name = 'TruenoBdOlIt.otf'
        font = self._load_font(name=font_name, size=font_size)
        char_images = self._make_sina_char_images(string, font)
        image = self._make_sina_image(char_images, bg_color=self._rand_color)
        return image

    @staticmethod
    def _make_sina_image(images, bg_color=None):
        width = 0
        height = 0
        for i in images:
            width = width + i.size[0]
            height = i.size[1] if height < i.size[1] else height

        image = Image.new('RGB', (width, height), color=bg_color)

        offset = 0
        for i in images:
            image.paste(i, (offset, 0), mask=i)
            offset = offset + i.size[0]

        return image

    def _make_sina_char_images(self, string, font):
        ret = []
        for c in string:
            w, h, wo, ho = self._get_char_font_size(font, c)
            image = Image.new(mode='RGBA', size=(w, h))
            draw = ImageDraw.Draw(image)
            draw.text((wo, ho), c, font=font, fill=self._rand_color)
            # image = self._rand_rotate_image(image)
            # image = self._rand_resize_image(image)
            ret.append(image)
        return ret

    def _load_font(self, path=None, name=None, size=100, index=0, encoding='', layout_engine=None):
        font_path = self._get_font_path(path=path, name=name)
        font = ImageFont.truetype(font=font_path,
                                  size=size,
                                  index=index,
                                  encoding=encoding,
                                  layout_engine=layout_engine)
        return font

    def _load_rand_font(self, index=0, encoding='', layout_engine=None):
        import random
        i = random.randrange(0, len(self.FONTS))
        name = self.FONTS[i]
        font = self._load_font(name=name,
                               index=index,
                               encoding=encoding,
                               layout_engine=layout_engine)
        return font

    def _rand_rotate_image(self, image):
        angel = random.randint(0, 360)
        image = self._rotate_image(image, angel)
        return image

    @property
    def _rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = 'rgb({R}, {G}, {B})'.format(R=r, G=g, B=b)
        return ImageColor.getrgb(color)

    @staticmethod
    def _get_color(r, g, b):
        color = 'rgb({R}, {G}, {B})'.format(R=r, G=g, B=b)
        return color

    @staticmethod
    def _get_char_font_size(font, char):
        size = font.getsize(char)
        width = size[0] * 2
        height = size[1] * 2
        width_offset = (width - size[0]) / 2
        height_offset = (height - size[1]) / 2
        return width, height, width_offset, height_offset

    @staticmethod
    def _rotate_image(image, angel=0):
        return image.rotate(angel)

    @staticmethod
    def _resize_image(image, size=None):
        return image.resize(size)

    @staticmethod
    def _rand_resize_image(image):
        import math
        ratio = random.random() + 0.5
        width = math.floor(image.size[0] * ratio)
        height = math.floor(image.size[1] * ratio)
        size = width, height
        return image.resize(size)

    @staticmethod
    def _base_dir():
        path = os.path.dirname(__file__)
        return path

    def _get_font_path(self, path: Path=None, name: str=None):
        path = path if path else Path(os.path.join(self._base_dir(), 'fonts', name))
        if path.exists():
            return str(path)
        else:
            raise FontNotFoundError()

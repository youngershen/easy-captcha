# Easy Captcha

![Travis](https://img.shields.io/travis/youngershen/easy-captcha.svg)
![codecov](https://codecov.io/gh/youngershen/django-easy-validator/branch/master/graph/badge.svg)
![PyPI - License](https://img.shields.io/pypi/l/easy-captcha.svg)
![PyPI](https://img.shields.io/pypi/v/easy-captcha.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/easy-captcha.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/easy-captcha.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/youngershen/easy-captcha.svg)

------

## What is it

this is a very easy to use python package that helps you to generate the image captchas, in the help of this package you
can easily make your own captcha design rather than the default design.

## Python supported

* CPYTHON 3.6
* CPYTHON 3.7

## Installation

* pip install easy-captcha
* python setup.py install

## Quick start

```python
    from captcha.generator import DefaultGenerator
    generator = DefaultGenerator()
    captcha = generator.make_captcha(string='ABCD')
    captcha.save('test-default.png')
```

the make_captcha method return a PIL Image object, you
can save it with your any type you wanted, easy to use.

## Samples

    from captcha import DefaultGenerator

![Default](assets/test-default.png)

    from captcha import SimpleGenerator

![Simple](assets/test-simple.png)

    from captcha import SimpleChineseGenerator

![Simple](assets/test-simple-chinese.png)

## Advance topic

### Custom font

```python
    from pathlib import Path
    from captcha.generator import DefaultGenerator

    class MyCaptchaGenerator(DefaultGenerator):
        def _get_font(self, size):
            p = Path('./fonts/test.otf')
            font = self._load_font(path=p, size=size)
            return font
```

if you just want to use your font instead of the default font,
just reimplement the _get_font method, make the method return
your font.

### Custom captcha generator

if you want to custom the captcha generator, you just need to subclass the **captcha.generator.BaseGenerator** class. when
you subclass the **BaseGenerator** then you could use the method
inside the **BaseGenerator** to make your own style captcha genrator.

if the default drawing methods are not well enough for you, you
could just use the **pillow** staff to make your own generator.
this whole package is based on **pillow**, so just feel free to
modify it.

for more details just check the code below. the important thing
is that when you subclass the **BaseGenerator**, you just need
to implement the **make_captcha** method and **_get_font** method.

```python
class DefaultGenerator(BaseGenerator):
    FONT = 'TruenoBdOlIt.otf'

    def make_captcha(self,
                     string: str = None,
                     font_size: int = 48,
                     image_size: tuple = None):
        captcha = self._make_captcha(string, font_size)
        size = image_size if image_size else self.size
        captcha = self._resize(captcha, size)
        return captcha

    def _make_captcha(self, string, font_size):
        font = self._get_font(font_size)
        char_images = self._make_char_images(string,
                                             font,
                                             rotate=None,
                                             color=self._rand_color)
        image = self._composite_char_images(char_images,
                                            color=self._get_color(255,
                                                                  255,
                                                                  255))

        self._rand_noise_lines(image, number=3)
        return image

    def _get_font(self, size: int):
        font = self._load_font(name=self.FONT, size=size)
        return font
```

## Future support feature

- [x] Basic png captcha support.
- [ ] GIF format support.
- [ ] Audio format support.
- [x] Django framework intergration, see [this](https://github.com/youngershen/django-easy-captcha).
- [ ] Flask framework intergration.
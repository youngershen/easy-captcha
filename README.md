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

    captcha.generator.DefaultGenerator

![Default](assets/test-default.png)

    from captcha.generator import SimpleGenerator

![Simple](assets/test-simple.png)

    from captcha.generator import SimpleChineseGenerator

![Simple](assets/test-simple-chinese.png)

## Advance topic

### Custom Font

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

## Future support feature

* GIF format support.
* Audio format support.
* Django framework intergration.
* Flask framework intergration.
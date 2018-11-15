# Easy Captcha

## What is it

this is a very easy to use python package that helps you to generate the image captchas, in the help of this package you
can easily make your own captcha design rather than the default design.

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

### Custom captcha generator

## Future support feature
from distutils.core import setup, Extension

module_spam = Extension('spam', sources=['spammodule.c'])

setup(
    name='project',
    version='1.0',

    py_modules=['project', 'graph', 'image', 'internet'],

    packages=['picture', 'telegram'],
    package_data={'picture':['*.png'], 'telegram':['*.py']},

    ext_modules=[module_spam]
)
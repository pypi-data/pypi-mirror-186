from setuptools import setup

setup(
    name='sothis',
    version='0.9.3',
    author='Oliver',
    author_email='oliverbcontact@gmail.com',
    packages=['sothis'],
    # scripts=['bin/script1','bin/script2'],
    # url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE',
    description='a growing library for all things I find use for that is not part of the standard library (to my knowledge)',
    long_description=open('README.md').read(),
    install_requires=[
        "Pillow"
    ],
)

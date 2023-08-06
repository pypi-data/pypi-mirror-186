from setuptools import setup, find_packages

VERSION = '0.0.1.25'
DESCRIPTION = 'Whisper package'
LONG_DESCRIPTION = 'A package that allows easily to use the Whisper library'

# Setting up
setup(
    name="whisp",
    version=VERSION,
    author="Peteris N.",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['setuptools-rust'],
    keywords=[],
    classifiers=[]
)
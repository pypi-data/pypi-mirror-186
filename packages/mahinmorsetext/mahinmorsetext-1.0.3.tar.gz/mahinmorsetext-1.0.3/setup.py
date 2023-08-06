from setuptools import setup, find_packages
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


VERSION = '1.0.3'
DESCRIPTION = 'Morse to Text and text to morse Decoder and Encoder'
setup(
    name="mahinmorsetext",
    version=VERSION,
    author="Mahin Bin Hasan (mahinbinhasan)",
    author_email="<allmahin149@gmail.com>",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahinbinhasan/morsetextencoder",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'morsecode','morsetotext','decoder','encoder','morsedecoder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
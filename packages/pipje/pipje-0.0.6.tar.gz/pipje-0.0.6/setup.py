from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.6'
DESCRIPTION = 'Shows a cat named pip.'

# Setting up
setup(
    name="pipje",
    version=VERSION,
    author="Hurbie48 (Matthijs Veldkamp) & Kjult (Kjeld Ritmeester)",
    author_email="<matjepatatje2@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['tk','pillow','urlopen'],
    keywords=['python', 'cat', 'image', 'tkinter'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
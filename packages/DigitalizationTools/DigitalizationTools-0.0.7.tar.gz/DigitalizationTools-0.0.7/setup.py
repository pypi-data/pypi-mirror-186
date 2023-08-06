
from setuptools import setup, find_packages

VERSION = '0.0.7'
DESCRIPTION = 'A package that manages database through sqlite3, and creates webapp through dash.'
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="DigitalizationTools",
    version=VERSION,
    author="Mengke Lu",
    author_email="<mklu0611@gmail.com>",
    description= DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'sqlite3', 'dash'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
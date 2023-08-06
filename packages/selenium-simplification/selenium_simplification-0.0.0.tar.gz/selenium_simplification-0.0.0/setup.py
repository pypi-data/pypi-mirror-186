from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.0"
DESCRIPTION = "Make Selenium simple. Using Selenium in a pythonic style without having to google how to do non-trivial stuff."

# Setting up
setup(
    name="selenium_simplification",
    version=VERSION,
    author="André Herber",
    author_email="andre.herber.programming@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    package_data={
        "": [
            "selenium_simplification/Chrome/chromedriver_win32/chromedriver.exe",
            "selenium_simplification/Chrome/config.json",
        ]
    },
    include_package_data=True,
    install_requires=["selenium"],
    keywords=["python", "selenium"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)

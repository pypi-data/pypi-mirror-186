from setuptools import *
import io

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(name="regfex",
    author="woidzero",
    version="1.0.3",
    license="MIT License",
    url="https://github.com/woidzero/regfex",
    description="Get regular expressions from .re files!", 
    packages=["regfex"], 
    author_email="woidzeroo@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False)
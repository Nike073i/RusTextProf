from setuptools import setup, find_packages

setup(
    name="text_utils", 
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.14.3"
    ],
    author="skuld",
    description="Утилиты для работы с текстом",
)
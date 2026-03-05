from setuptools import setup, find_packages

setup(
    name="text_metrics", 
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "intervaltree",
        "urlextract",
        "phonenumbers",
        "natasha",
        "pymorphy2==0.9.1",
        "pymorphy2-dicts-ru==2.4.417127.4579844",
        "setuptools==80.1.0",
        "nltk",
        "numpy"
    ],
    author="skuld",
    description="Извлечение метрик из текста",
)
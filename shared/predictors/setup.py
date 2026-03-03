from setuptools import setup, find_packages

setup(
    name="predictors", 
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "scikit-learn"
    ],
    author="skuld",
    description="Модули работы с ИИ-моделями",
)
from setuptools import setup, find_packages

setup(
    name="predictors", 
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "numpy",
        "pandas"
    ],
    author="skuld",
    description="Модули работы с ИИ-моделями",
)
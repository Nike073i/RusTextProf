from setuptools import setup, find_packages

setup(
    name="research_utils", 
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "statsmodels"
    ],
    author="skuld",
    description="Общие модули для проведения исследования, визуализации, обучения и экспериментов над моделями",
)
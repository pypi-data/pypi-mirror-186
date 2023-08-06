from setuptools import setup, find_packages

setup(
    name='scrap_stock',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
    ],
)
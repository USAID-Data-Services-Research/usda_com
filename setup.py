from setuptools import find_packages, setup

setup(
    name='usda_com',
    packages=find_packages(),
    version='0.1.0',
    description='This package wraps the USDA Commodity API for ease of use in python. ',
    author='Andrew Lightner',
    license='MIT',
    package_data={'usda_com': ['./usda_com/data/commodities.csv']},
    include_package_data=True
)

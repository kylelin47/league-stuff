from setuptools import find_packages, setup

setup(
    name='pyriot',
    version='0.1',
    install_requires=[
        'requests >=2.7.0',
    ],
    packages=find_packages(),
    include_package_data = True,
    scripts=[
    ],
)
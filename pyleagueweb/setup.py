from setuptools import find_packages, setup

setup(
    name='pyleagueweb',
    version='0.1',
    install_requires=[
        'pyleague >=0.1',
        'flask >=0.10.1'
    ],
    packages=find_packages(),
    include_package_data = True,
    scripts=[
    ],
)

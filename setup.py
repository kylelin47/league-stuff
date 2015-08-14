from setuptools import find_packages, setup

setup(
    name='pyleague',
    version='0.1',
    install_requires=[
        'requests >=2.7.0',
    ],
    packages=find_packages(exclude=['web']),
    include_package_data = True,
    scripts=[
    ],
)

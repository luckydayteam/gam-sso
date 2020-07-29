#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as req:
    reqs = [line.strip() for line in req]

setup(
    name='gammit',
    version='0.1',
    description='GAM User Mapping Tool',
    author='LuckyDay Engineering',
    author_email='dan@luckydayapp.com',
    url='https://github.com/luckydayteam/gammit-sso',
    packages=find_packages(),
    install_requires=reqs,
    setup_requires=[],
    tests_require=[],
    entry_points={
        'console_scripts': [
            'gammit = gammit.cli:main',
        ]
    },
    package_data={
        'gammit.mapping': ['*']
    },
    license='MIT',
)

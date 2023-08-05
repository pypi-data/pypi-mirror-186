
from setuptools import setup, find_packages
import os

setup(
    name='emmy',
    version='0.1.2',
    license='MIT',
    author="Joyoforigami",
    author_email='raise-an-issue-on-github@email-is-private.com',
    packages=find_packages('/Users/chenglei/emmy'),
    package_dir={'':'/Users/chenglei/emmy'},
    url='https://github.com/joyoforigami/emmy',
    keywords='esolang hash',
    install_requires=[
          'xxhash',
          'numpy'
      ]

)
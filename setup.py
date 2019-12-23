from setuptools import find_packages
from setuptools import setup

setup(
    name='rss_reader_kapitonov',
    version='4.0.0',
    packages=find_packages(),
    install_requires=[
                        'argparse',
                        'ebooklib',
                        'feedparser'
    ],
    author='Andrey Kapitonov',
    author_email='akapitonov1999@gmail.com',
    url='https://github.com/akapitonov1999',
    python_requires='>=3.7',
    scripts=['bin/rss_reader_kapitonov'],
    entry_points={'console_scripts': ['rss_reader_kapitonov'
                  '=rss_reader_kapitonov.command_line:main'], })

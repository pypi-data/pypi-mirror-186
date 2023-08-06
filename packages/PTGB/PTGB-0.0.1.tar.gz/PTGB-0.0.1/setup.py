from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PTGB',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/kalanakt/PTGB',
    author='kalanakt',
    author_email='e19198@eng.pdn.ac.lk',
    description='A package for sending Telegram messages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='telegram api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

# python setup.py sdist
# twine upload dist/*

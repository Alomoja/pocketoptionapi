from setuptools import setup, find_packages

setup(
    name='pocketoptionapi',
    version='0.1.1',
    description='A simple API wrapper for PocketOption',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alomoja',
    author_email='alomojaf@gmail.com',
    url='https://github.com/Alomoja/pocketoptionapi',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

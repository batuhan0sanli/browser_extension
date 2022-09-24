from setuptools import setup, find_packages

from os import path

# The directory containing this file
PATH = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(PATH, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the requirements from the requirements.txt file
with open(path.join(PATH, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='browser_extension',
    version='1.0.0',
    description='Download browser extensions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/batuhan0sanli/browser_extension',
    author='batuhan0sanli',
    author_email='batuhansanli@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='browser extension download selenium chrome chromium webdriver',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements,
    python_requires='>=3.8',
)

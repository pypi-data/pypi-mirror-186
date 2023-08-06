from distutils.core import setup
from setuptools import setup, find_packages
VERSION = '0.0.12'
setup(
    name = 'eCB1',
    packages=find_packages(),
    version = VERSION,
    description = 'A library to communicate with the eCB1 Hardy Barth Smart Meter for Hardy Barth Wallboxes',
    author='nilsmau',
    author_email='nilsmau@hotmail.com',
    license='GPL',
    url='https://github.com/nilsmau/eCB1',
    download_url='https://pypi.org/project/eCB1/'+VERSION+'/',
    install_requires=[
        'requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)

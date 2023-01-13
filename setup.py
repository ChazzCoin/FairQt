from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairQt',
    version='2.0.0',
    description='pyQt6 plus Qt Designer Support Framework',
    url='https://github.com/chazzcoin/FairQt',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    package_dir={'res': 'FQt'},
    package_data={
        'FQt': ['FTemplates/*.ui']
    },
    install_requires=['faircore>=1.0.0', 'pyqt6'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
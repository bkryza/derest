import os
from setuptools import setup, find_packages

from derest import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = []

setup(
    name="derest",
    version=".".join(map(str, __version__)),
    description="",
    long_description=read('README.rst'),
    url='https://github.com/bkryza/derest',
    license='Apache2',
    author='Bartek Kryza',
    author_email='bkryza@gmail.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache 2',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['requests', 'six'],
    tests_require=['pytest']
)

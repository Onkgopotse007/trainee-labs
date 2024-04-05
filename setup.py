# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='trainee-labs',
    version='0.0.1',
    author=u'Tony Richard',
    author_email='trichard@bhp.org.bw',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/onkgopotse007/trainee-labs.git',
    license='GPL license, see LICENSE',
    description='Trainee Labs',
    long_description=README,
    zip_safe=False,
    keywords='django trainee labs',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
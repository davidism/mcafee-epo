#!/usr/bin/env python
import os
import re
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'mcafee_epo.py')) as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

setup(
    name='mcafee-epo',
    version=version,
    url='https://bitbucket.org/davidism/mcafee-epo',
    license='BSD',
    author='David Lord',
    author_email='david.lord@moesol.com',
    description='McAfee ePolicy Orchestrator API',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Systems Administration'
    ],
    py_modules=['mcafee_epo'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['requests']
)

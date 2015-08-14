#!/usr/bin/env python
from setuptools import setup

setup(
    name='mcafee-epo',
    version='1.0.4',
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

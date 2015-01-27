#!/usr/bin/env python
from setuptools import setup

setup(
    name='McAfee-ePO',
    version='1.0',
    url='https://community.mcafee.com/docs/DOC-3095',
    license='BSD',
    author='David Lord',
    author_email='david.lord@moesol.com',
    description='McAfee ePolicy Orchestrator API',
    py_modules=['mcafee_epo'],
    zip_safe=True,
    install_requires=['requests']
)

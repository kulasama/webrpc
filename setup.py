#!/usr/bin/env python

import sys
import os
from distutils.core import setup

if sys.version_info < (2,5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use webrpc.")

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

# Ugly, but we can't import bottle with 3.x to read __version__ (throws SyntaxError)
for line in open(os.path.join(os.path.dirname(sys.argv[0]),'webrpc.py')):
    if line.startswith('__version__'):
        version = eval(line.split('=')[-1])

setup(name='webrpc',
      version=version,
      description='wep rpc framework.',
      long_description='simple web rpc framework,base bottle',
      author='kula',
      author_email='kulasama@gmail.com',
      url='http://github.com/kulasama/webrpc',
      py_modules=['webrpc'],
      license='MIT',
      platforms = 'any',
      cmdclass = {'build_py': build_py}
     )




#!/usr/bin/env python

import os, sys
from distutils.core import setup

sys.path.insert(0, os.path.dirname(__file__))
try:
    import stream
finally:
    del sys.path[0]

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

setup(
	name = 'stream',
	version = stream.__version__,
	description = stream.__doc__.split('\n')[0],
	long_description = stream.__doc__.split('\n\n')[1],
	author = 'Hai-Anh Trinh',
	author_email = 'moc.liamg@hnirt.iah.hna:otliam'[::-1],
	url = 'http://trinhhaianh.com/stream.py/',
	license='BSD',
	platforms=['any'],
	classifiers=filter(None, classifiers.split("\n")),
	py_modules = ['stream']
)

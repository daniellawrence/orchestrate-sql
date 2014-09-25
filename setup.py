#!/usr/bin/env python

import re
from setuptools import setup

VERSIONFILE="orchetrate-sql/version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^VERSION = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSION = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='orchetrate-sql',
      version=VERSION,
      description='Copies a SQL database into Orchestrate',
      author='Diana Thayer',
      author_email='diana@orchestrate.io',
      url='https://github.com/orchestrate-io/orchetrate-sql',
      packages=['orchetrate-sql'],
      license='Apache-2.0',
      install_requires=[
          'porc==0.3.1',
          'psycopg2==2.5.4',
          'vcrpy==1.1.0'
      ],
      test_suite="tests",
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
      ],
      )

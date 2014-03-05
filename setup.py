
#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append('./src')

from distutils.core import setup
from clikeepassx import __version__

setup(name='clikeepassx',
      version=__version__,
      description='A command line keepassx',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['clikeepassx'],
      package_dir={'clikeepassx': 'src/clikeepassx'},
      package_data={'clikeepassx': ['stuff']},
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/clikeepassx')

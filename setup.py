try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys,os

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='Code2pdf',
      version='0.0.2',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['Code2pdf', ],
      entry_points={
          'console_scripts': ['code2pdf=Code2pdf:main'],
      },
      license='GNU General Public License v3 (GPLv3)',
      url='https://github.com/tushar-rishav/code2pdf/',
      description="Converts given source code into pdf file with syntax highlighting, line numbers and much more",
      long_description=open('README').read(),
      keywords=['pdf', 'markup',
                'formatting', 'convert code to pdf', 'python'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring'
      ],
      )

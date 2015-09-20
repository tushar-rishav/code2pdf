try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='Py2pdf',
      version='0.0.1',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['Py2pdf', ],
      data_files=[('Py2pdf/css', ['Py2pdf/css/py2html.css'])],
      entry_points={
          'console_scripts': ['py2pdf=Py2pdf:main'],
      },
      license='GNU General Public License v3 (GPLv3)',
      url='https://github.com/tushar-rishav/py2pdf/',
      description="Converts python script into pdf file with syntax highlighting",
      long_description=open('README').read(),
      keywords=['reminder', 'battery',
                'notification', 'voice alert', 'python'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring'
      ],
      )

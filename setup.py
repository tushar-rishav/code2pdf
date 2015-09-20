try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys,os

extra = {}
this_dir, this_filename = os.path.split(__file__)
css_file = os.path.join(this_dir, "Py2pdf", "css", "py2html.css")
ins_dir = os.path.join(this_dir, "Py2pdf", "css")

if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='Py2pdf',
      version='0.0.18',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['Py2pdf', ],
      data_files=[(ins_dir, [css_file])],
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

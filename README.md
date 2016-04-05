## Code2pdf :fax:
Convert given source code into .pdf with syntax highlighting and more features

| Build Status | Version | Downloads | Python   |
| ------------ |---------|-----------|----------|
| [![Build Status](https://travis-ci.org/tushar-rishav/code2pdf.svg?branch=master)](https://travis-ci.org/tushar-rishav/code2pdf)|[![PyPI version](https://badge.fury.io/py/Code2pdf.svg)](http://badge.fury.io/py/Code2pdf)| [![PyPi downloads](https://img.shields.io/pypi/dw/code2pdf.svg)](https://pypi.python.org/pypi/Code2pdf)|[![PyPI](https://img.shields.io/pypi/pyversions/Code2pdf.svg)](https://pypi.python.org/pypi/Py2pdf)

### [Demo](https://cloud.githubusercontent.com/assets/7397433/10060934/645a3cc6-6272-11e5-9ebb-a1ac24c86d67.gif)
![demo](https://cloud.githubusercontent.com/assets/7397433/10060934/645a3cc6-6272-11e5-9ebb-a1ac24c86d67.gif)

### Dependencies
- [x] [PyQt](http://www.riverbankcomputing.com/software/pyqt/download)

### Installation

##### Build from source

```sh
git clone https://github.com/tushar-rishav/code2pdf.git
cd code2pdf
python setup.py install

```
Or

##### Using pip

```sh
pip install code2pdf

```
### Usage

##### A. As console app

###### Help

```sh
code2pdf -h

```
###### Usage
 ` code2pdf [-h] [-l] [-s SIZE] [-S NAME] [-v] filename [outputfile] `

###### Options

```sh
positional arguments:
  filename              absolute path of the python file
  outputfile            absolute path of the output pdf file

optional arguments:
  -h, --help            show this help message and exit
  -l, --linenos         include line numbers.
  -s SIZE, --size SIZE  PDF size. A2,A3,A4,A5 etc
  -S NAME, --style NAME
                        the style name for highlighting. Eg. emacs, vim style etc.
  -v, --version         show program's version number and exit

```
###### Available style types are

- [x] autumn
- [x] borland
- [x] bw
- [x] colorful
- [x] default
- [x] emacs
- [x] friendly
- [x] fruity
- [x] igor
- [x] manni
- [x] monokai
- [x] murphy
- [x] native
- [x] paraiso-dark
- [x] paraiso-light
- [x] pastie
- [x] perldoc
- [x] rrt
- [x] tango
- [x] trac
- [x] vim
- [x] vs
- [x] xcode

###### Example
```sh
 code2pdf -l -s a3 -S emacs ~/Code2Pdf/Code2pdf/code2pdf.py ~/Code2Pdf/Demo/demo.pdf

```
To see the demo for above check `Demo/` in github repo

##### B. As module

```py
	
from Code2pdf.code2pdf import Code2pdf
ifile,ofile,size = "test.py", "test.pdf", "A4"
pdf = Code2pdf(ifile, ofile, size)	# create the Code2pdf object
pdf.init_print()	# call print method to print pdf

```

### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

### Contributor
[Christopher Welborn](https://github.com/cjwelborn)

### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)



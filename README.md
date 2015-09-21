### Py2pdf :fax:
Converts python file into pdf with syntax highlighting and custom size

| Build Status | Version | Downloads | Python   |
| ------------ |---------|-----------|----------|
| [![Build Status](https://travis-ci.org/tushar-rishav/py2pdf.svg?branch=master)](https://travis-ci.org/tushar-rishav/py2pdf)|[![PyPI version](https://badge.fury.io/py/py2pdf.svg)](http://badge.fury.io/py/py2pdf)| [![PyPi downloads](https://img.shields.io/pypi/dw/py2pdf.svg)](https://pypi.python.org/pypi/Py2pdf)|[![PyPI](https://img.shields.io/pypi/pyversions/Py2pdf.svg)](https://pypi.python.org/pypi/Py2pdf)

### [Demo](https://cloud.githubusercontent.com/assets/7397433/9981909/383c2a50-5fe8-11e5-9ad5-90e12a5b838b.gif)
![demo](https://cloud.githubusercontent.com/assets/7397433/9981909/383c2a50-5fe8-11e5-9ad5-90e12a5b838b.gif)



#### Installation

###### Build from source

```sh
git clone https://github.com/tushar-rishav/py2pdf.git
cd py2pdf
python setup.py install

```
Or

###### Using pip

```sh
pip install py2pdf

```
#### Usage

##### A. As console app

###### Help

```sh
py2pdf -h

```

###### Options

```sh
-i or --ifile path for input python file
-o or --ofile path for ouput pdf file
-s or --size for pdf file size. Available sizes are A2,A3 and A4. Default one is A3
```

###### Example
```sh
py2pdf -i ~/Py2PDF/Py2pdf/py2pdf.py -o ~/Py2PDF/Demo/demo.pdf -s a3

```
To see the demo for above check `Demo/` in github repo

##### B. As module

```py
	
from Py2pdf.py2pdf import Py2pdf
ifile,ofile,size = "test.py", "test.pdf", "A4"
pdf = Py2pdf(ifile, ofile, size)	# create the Py2pdf object
pdf.init_print()	# call print method to print pdf

```

#### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

#### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)



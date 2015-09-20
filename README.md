### Py2pdf :fax:
Converts python file into pdf with syntax highlighting and custom size

#### Installation
###### Manually
```sh
	python setup.py install
```
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

#### Todo
- [x] Fix syntax highlighting bug
- [ ] Add working demo

#### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

#### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)



Code2pdf :fax:
------------

Convert given source code into .pdf with syntax highlighting and more features

+------------------+------------------+--------------------+----------+
| Build Status     | Version          | Downloads          | Python   |
+==================+==================+====================+==========+
| |Build Status|   | |PyPI version|   | |PyPi downloads|   | |PyPI|   |
+------------------+------------------+--------------------+----------+

`Demo <https://cloud.githubusercontent.com/assets/7397433/10060934/645a3cc6-6272-11e5-9ebb-a1ac24c86d67.gif>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://cloud.githubusercontent.com/assets/7397433/10060934/645a3cc6-6272-11e5-9ebb-a1ac24c86d67.gif
   :alt: demo

Dependencies
~~~~~~~~~~~~

-  [x] [PyQt](http://www.riverbankcomputing.com/software/pyqt/download)

Installation
~~~~~~~~~~~~

Build from source
'''''''''''''''''

.. code:: sh

    git clone https://github.com/tushar-rishav/code2pdf.git
    cd code2pdf
    python setup.py install

Or

Using pip
'''''''''

.. code:: sh

    pip install code2pdf

Usage
~~~~~

A. As console app
'''''''''''''''''

Help
    

.. code:: sh

    code2pdf -h

Usage
     

``code2pdf [-h] [-l] [-s SIZE] [-S NAME] [-v] filename [outputfile]``

Options
       

.. code:: sh

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

Available style types are
                         

-  [x] autumn
-  [x] borland
-  [x] bw
-  [x] colorful
-  [x] default
-  [x] emacs
-  [x] friendly
-  [x] fruity
-  [x] igor
-  [x] manni
-  [x] monokai
-  [x] murphy
-  [x] native
-  [x] paraiso-dark
-  [x] paraiso-light
-  [x] pastie
-  [x] perldoc
-  [x] rrt
-  [x] tango
-  [x] trac
-  [x] vim
-  [x] vs
-  [x] xcode

Example
       

.. code:: sh

     code2pdf -l -s a3 -S emacs ~/Code2Pdf/Code2pdf/code2pdf.py ~/Code2Pdf/Demo/demo.pdf

To see the demo for above check ``Demo/`` in github repo

B. As module
''''''''''''

.. code:: py

        
    from Code2pdf.code2pdf import Code2pdf
    ifile,ofile,size = "test.py", "test.pdf", "A4"
    pdf = Code2pdf(ifile, ofile, size)  # create the Code2pdf object
    pdf.init_print()    # call print method to print pdf

Contributions
~~~~~~~~~~~~~

Have an idea to make it better? Go ahead! I will be happy to see a pull
request from you! :blush:

Contributor
~~~~~~~~~~~

`Christopher Welborn <https://github.com/cjwelborn>`__

License
~~~~~~~

.. figure:: https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png
   :alt: gpl


.. |Build Status| image:: https://travis-ci.org/tushar-rishav/code2pdf.svg?branch=master
   :target: https://travis-ci.org/tushar-rishav/code2pdf
.. |PyPI version| image:: https://badge.fury.io/py/Code2pdf.svg
   :target: http://badge.fury.io/py/Code2pdf
.. |PyPi downloads| image:: https://img.shields.io/pypi/dw/code2pdf.svg
   :target: https://pypi.python.org/pypi/Py2pdf
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/Code2pdf.svg
   :target: https://pypi.python.org/pypi/Py2pdf

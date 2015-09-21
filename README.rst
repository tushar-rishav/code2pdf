Py2pdf :fax:
~~~~~~~~~~~~

Converts python file into pdf with syntax highlighting and custom size

+------------------+------------------+--------------------+----------+
| Build Status     | Version          | Downloads          | Python   |
+==================+==================+====================+==========+
| |Build Status|   | |PyPI version|   | |PyPi downloads|   | |PyPI|   |
+------------------+------------------+--------------------+----------+

`Demo <https://cloud.githubusercontent.com/assets/7397433/9981909/383c2a50-5fe8-11e5-9ad5-90e12a5b838b.gif>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://cloud.githubusercontent.com/assets/7397433/9981909/383c2a50-5fe8-11e5-9ad5-90e12a5b838b.gif
   :alt: demo


Installation
^^^^^^^^^^^^

Build from source
~~~~~~~~~~~~~~~~~
        

.. code:: sh

        wget "https://pypi.python.org/packages/source/P/Py2pdf/Py2pdf-0.0.5.tar.gz"
        tar xzvf Py2pdf-0.0.5.tar.gz
        cd Py2pdf-0.0.5
        python setup.py install

Or

Using pip
         

.. code:: sh

    pip install py2pdf

Usage
^^^^^

A. As console app
'''''''''''''''''

Help
    

.. code:: sh

    py2pdf -h

Options
       

.. code:: sh

    -i or --ifile path for input python file
    -o or --ofile path for ouput pdf file
    -s or --size for pdf file size. Available sizes are A2,A3 and A4. Default one is A3

Example
       

.. code:: sh

    py2pdf -i ~/Py2PDF/Py2pdf/py2pdf.py -o ~/Py2PDF/Demo/demo.pdf -s a3

To see the demo for above check ``Demo/`` in github repo

B. As module
''''''''''''

.. code:: py

        
    from Py2pdf.py2pdf import Py2pdf
    ifile,ofile,size = "test.py", "test.pdf", "A4"
    pdf = Py2pdf(ifile, ofile, size)    # create the Py2pdf object
    pdf.init_print()    # call print method to print pdf

Contributions
^^^^^^^^^^^^^

Have an idea to make it better? Go ahead! I will be happy to see a pull
request from you! :blush:

License
^^^^^^^

.. figure:: https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png
   :alt: gpl

.. |Build Status| image:: https://travis-ci.org/tushar-rishav/py2pdf.svg?branch=master
   :target: https://travis-ci.org/tushar-rishav/py2pdf
.. |PyPI version| image:: https://badge.fury.io/py/py2pdf.svg
   :target: http://badge.fury.io/py/py2pdf
.. |PyPi downloads| image:: https://img.shields.io/pypi/dw/py2pdf.svg
   :target: https://pypi.python.org/pypi/Py2pdf
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/Py2pdf.svg
   :target: https://pypi.python.org/pypi/Py2pdf

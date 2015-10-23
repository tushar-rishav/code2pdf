import os
import unittest2
import sys
from Code2pdf.code2pdf import *
try:
    import pygments
    from pygments import lexers, formatters, styles
except ImportError as ex:
    logging.warning('\nCould not import the required \
        "pygments" module:\n{}'.format(
        ex))
    sys.exit(1)


class Code2pdfTestCase(unittest2.TestCase):

    """
        Tests for `code2pdf.py`.
    """

    def setUp(self):
        self.filename = "test.py"
        self.pdf_file = os.path.abspath("test.pdf")
        self.size = "a4"
        self.style = "emacs"
        self.linenos = True
        self.output_file = None

    def test_init_print(self):
        pdf = Code2pdf(self.filename, self.pdf_file, self.size)
        pdf.init_print(self.linenos, self.style)
        self.assertTrue(os.path.exists(pdf.pdf_file))    # if pdf printed

    def test_highlight_file(self):
        hpdf = Code2pdf(self.filename, self.pdf_file, self.size)
        html = hpdf.highlight_file(True, 'emacs')
        self.assertIn("!DOCTYPE", html)                 # if html created

    def test_get_output_file(self):
        self.assertEqual(
            get_output_file(self.filename, self.output_file), self.pdf_file)

if __name__ == "__main__":
    unittest2.main()

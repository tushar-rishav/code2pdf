import subprocess
import unittest2


class Code2pdfTestCase(unittest2.TestCase):
    """Tests for `balert/main.py`."""

    def run_code2pdf(self):
        try:
            py2pdf_run = subprocess.Popen("code2pdf -h \
                ", shell=True, stdout=subprocess.PIPE).stdout.read()
            return True
        except:
            return False

    def test_code2pdf(self):
        self.assertTrue(self.run_code2pdf())

if __name__ == "__main__":
    unittest2.main()

import subprocess
import unittest2


class Py2pdfTestCase(unittest2.TestCase):
    """Tests for `balert/main.py`."""

    def run_py2pdf(self):
        try:
            balert_run = subprocess.Popen("py2pdf \
                ", shell=True, stdout=subprocess.PIPE).stdout.read()
            return True
        except:
            return False

    def test_py2pdf(self):
        self.assertTrue(self.run_balert())

if __name__ == "__main__":
    unittest2.main()

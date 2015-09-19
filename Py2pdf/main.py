#! /usr/bin/python
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication
import sys
import argparse
import subprocess

class Py2pdf:
	"""
		converts python file to pdf
	"""
	def __init__(self, ifile = None, ofile = None):
		
		self.temp_location = "/tmp/temp.py"
		self.style="css/py2html.css"
		if not ifile:
			raise Exception("input file is required")
		else:
			self.py_file = ifile
			if ofile:
				self.pdf_file = ofile
			else:
				self.pdf_file = ifile.split('.')[0]+".pdf"
			self.create_clone()
	
	def create_clone(self):
		"""
			creates a temporary file to copy python file
		"""
		ftemp = open(self.temp_location, 'wb') 
		fpy = open(self.py_file,'rb')
		ftemp.write(fpy.read())
		ftemp.close()
		fpy.close()

	def init_print(self):
		app = QApplication(sys.argv)
		doc = QTextDocument()
		r = "pyhtmlizer -s %s %s"%(self.style,self.temp_location)
		s = subprocess.Popen(r, shell=True)
		s.wait()	# let the child process get over else OSError
		self.temp_location+=".html"
		html = open(self.temp_location).read()	# location has to be the location of the file
		doc.setHtml(html)
		printer = QPrinter()
		printer.setOutputFileName(self.pdf_file)
		printer.setOutputFormat(QPrinter.PdfFormat)
		printer.setPageSize(QPrinter.A4);
		printer.setPageMargins (15,15,15,15,QPrinter.Millimeter);
		doc.print_(printer)
		print "done!"

def parse_arg():
	parser = argparse.ArgumentParser(description=" \
			 Convert Python code into pdf with syntax highlighting", epilog="\
			 Author:tushar.rishav@gmail.com")
	parser.add_argument("-i", "--ifile", help="Absolute path of the python file", type=str)
	parser.add_argument("-o", "--ofile", help="Absolute path of the output pdf file", type=str)
	args = parser.parse_args()
	if not args.ifile:
		raise Exception("input file is required")
	else:
		ifile = args.ifile # read python file which is to be converted
		if args.ofile:
			pdf_file = args.ofile
		else:
			pdf_file = args.ifile.split('.')[0]+".pdf"
	return (ifile,pdf_file)

def main():
	
	ifile,ofile = parse_arg()
	pdf = Py2pdf(ifile,ofile)	
	pdf.init_print()
	print pdf.style

if __name__ == "__main__":
	main()
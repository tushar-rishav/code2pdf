#! /usr/bin/env python
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication
import argparse
import logging
import os
import sys

try:
    import pygments
    from pygments import lexers, formatters, styles
except ImportError as ex:
    logging.warning('\nCould not import the required "pygments" \
        module:\n{}'.format(ex))
    sys.exit(1)

__version__ = '1.0.0'


def logger(func):
    def log_wrap(self, ifile=None, ofile=None, size="A4"):
        logging.getLogger().name = "code2pdf> "
        logging.getLogger().setLevel(logging.INFO)
        func(self, ifile, ofile, size)
    return log_wrap


class Code2pdf(QApplication):

    """
            Convert a source file into a pdf with syntax highlighting.
    """
    @logger
    def __init__(self, ifiles=None, ofile=None, size="A4"):
        super(Code2pdf, self).__init__(sys.argv)
        self.size = size
        if isinstance(ifiles, str):
            # To maintain backwards compatibility, probably kill this later.
            ifiles = [ifiles]
        if not ifiles:
            raise Exception("input file is required")
        self.input_files = ifiles
        self.pdf_file = ofile or "{}.pdf".format(ifiles[0].split('.')[0])

    def get_lexer(self, filename, content):
        """ Retrieve the correct lexer for this file, by name or content.
            If "-" is used as a file name, the lexer is guessed (for stdin).
        """
        lexer = None
        if filename != "-":
            try:
                lexer = lexers.get_lexer_for_filename(input_file)
            except pygments.util.ClassNotFound:
                # Try guessing the lexer (file type) later.
                pass
        if lexer is None:
            try:
                lexer = lexers.guess_lexer(content)
            except pygments.util.ClassNotFound:
                # No lexer could be guessed.
                lexer = lexers.get_lexer_by_name("text")
        return lexer

    def highlight_file(self, linenos=True, style='default'):
        """ Highlight the input file, and return HTML as a string. """

        try:
            formatter = formatters.HtmlFormatter(
                linenos=linenos,
                style=style,
                full=True)
        except pygments.util.ClassNotFound:
            logging.error("\nInvalid style name: {}\nExpecting one of:\n \
                {}".format(style, "\n    ".join(sorted(styles.STYLE_MAP))))
            sys.exit(1)

        allcontent = ""
        stdin_read = False
        for input_file in self.input_files:
            try:
                if (input_file == "-") and (not stdin_read):
                    content = sys.stdin.read()
                    stdin_read = True
                else:
                    with open(input_file, "r") as f:
                        content = f.read()
            except EnvironmentError as exread:
                fmt = "\nUnable to read file: {}\n{}"
                logging.error(fmt.format(input_file, exread))
                sys.exit(2)
            logging.debug("Highlighting file: {}".format(input_file))
            lexer = self.get_lexer(input_file, content)
            allcontent = "\n".join((
                allcontent,
                pygments.highlight(content, lexer, formatter)
            ))
        return allcontent

    def init_print(self, linenos=True, style="default"):
        # app = QApplication(sys.argv)  # noqa
        doc = QTextDocument()
        doc.setHtml(
            self.highlight_file(linenos=linenos, style=style)
        )
        printer = QPrinter()
        printer.setOutputFileName(self.pdf_file)
        printer.setOutputFormat(QPrinter.PdfFormat)
        page_size_dict = {"a2": QPrinter.A2, "a3": QPrinter.A3, "a4": QPrinter.A4}
        printer.setPageSize(page_size_dict.get(self.size.lower(), QPrinter.A4))
        printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)
        doc.print_(printer)
        logging.info("PDF created at %s" % (self.pdf_file))


def get_output_file(inputnames, outputname=None):
    """ If the output name is set, then return it.
        Otherwise, build an output name using the current directory,
        replacing the input name's extension.
    """
    if outputname:
        return outputname

    inputbase = os.path.split(inputnames[0])[-1]
    outputbase = "{}.pdf".format(os.path.splitext(inputbase)[0])
    return os.path.join(os.getcwd(), outputbase)


def parse_arg():
    parser = argparse.ArgumentParser(
        description=(
            "Convert given source code into .pdf with syntax highlighting"),
        epilog="Author:tushar.rishav@gmail.com"
    )
    parser.add_argument(
        "filename",
        help="absolute path of the python file",
        default=["-"],
        nargs="*",
        type=str)
    parser.add_argument(
        "-l",
        "--linenos",
        help="include line numbers.",
        action="store_true")
    parser.add_argument(
        "-o",
        "--outputfile",
        help="absolute path of the output pdf file",
        nargs="?",
        type=str)
    parser.add_argument(
        "-s",
        "--size",
        help="PDF size. A2,A3,A4,A5 etc",
        type=str,
        default="A3")
    parser.add_argument(
        "-S",
        "--style",
        help="the style name for highlighting.",
        type=str,
        default="default",
        metavar="NAME")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s v. {}".format(__version__))
    return parser.parse_args()


def main():
    args = parse_arg()
    pdf_file = get_output_file(args.filename, args.outputfile)
    pdf = Code2pdf(args.filename, pdf_file, args.size)
    pdf.init_print(linenos=args.linenos, style=args.style)
    pdf.exit(0)

if __name__ == "__main__":
    sys.exit(main())

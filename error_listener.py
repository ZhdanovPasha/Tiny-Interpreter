import sys
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        self.symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("lines " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)

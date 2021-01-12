import sys
from antlr4 import *
from LanguageLexer import LanguageLexer
from LanguageParser import LanguageParser
from visitor import MyVisitor
from error_listener import MyErrorListener


def main(argv):
	input_stream = FileStream(argv[1])
	lexer = LanguageLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = LanguageParser(stream)
	parser.removeErrorListeners()
	error_listener = MyErrorListener()
	parser.addErrorListener(error_listener)
	tree = parser.prog()
	visitor = MyVisitor()
	visitor.visit(tree)


if __name__ == '__main__':
	main(sys.argv)
from antlr4 import *
from LanguageLexer import LanguageLexer
from LanguageParser import LanguageParser
from interpreter import MyErrorListener, MyVisitor
import pytest


calculation_params_list = [
    pytest.param("""
    a = 10
    b = 20
    c = a + b
    k = b - a
    p = c * k
    """, 300, id='test_operations'),
    pytest.param("""
    a = -10
    b = (-10) - (-20)
    c = a + b + 1
    """, 1, id='test_negative_numbers'),
    pytest.param("""
    b = 1
    c = 10
    k = (b - (-(c + b) - 12) + 6 * 2) - (-10)
    """, 46, id='test_parens'),
    pytest.param("""
    c = 44390+ 403594 + (-432943 + 5434) - ((((43) + (4-43))-(42+43)) * (11-32) - 3)
    """, 18777, id='test_big_random_sample'),
    pytest.param("""
    a = NOT(NOT(1 AND 0)) OR TRUE
    """, 1, id='test_simple_boolean'),
    pytest.param("""
    a = 2 + (1 OR 0) - (1 AND 1)
    """, 2, id='test_boolean_and_int')
]


def create_parser(text, is_return_error_listener=False):
    lexer = LanguageLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)
    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)
    if is_return_error_listener:
        return parser, error_listener
    return parser


def get_final_result_from_parser(parser):
    tree = parser.prog()
    visitor = MyVisitor()
    result = visitor.visit(tree)
    return result


@pytest.mark.parametrize("input_code,expected", calculation_params_list)
def test_calculation(input_code, expected):
    parser = create_parser(input_code)
    result = get_final_result_from_parser(parser)
    assert result == expected


def test_incorrect_symbol(capsys):
    text = """
    b = _50
    """
    parser, error_listener = create_parser(text, True)
    result = get_final_result_from_parser(parser)
    out, err = capsys.readouterr()
    assert '_' in err


def test_zero_division(capsys):
    text = """
    a = 0
    b = 20 / a
    """
    parser, error_listener = create_parser(text, True)
    with pytest.raises(SystemExit):
        result = get_final_result_from_parser(parser)
    out, err = capsys.readouterr()
    assert 'zero division' in out


def test_unknown_variable(capsys):
    text = """
    a = 10 + b
    """
    parser, error_listener = create_parser(text, True)
    with pytest.raises(SystemExit):
        result = get_final_result_from_parser(parser)
    out, err = capsys.readouterr()
    assert 'unknown variable' in out

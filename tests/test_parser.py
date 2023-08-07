
from fat.lexer import Lexer
from fat.parser import Parser


def test_parser():
    a = [1]
    b = [2]
    f = lambda x: x*x
    g = lambda x: x*x*x
    assert Parser(Lexer((a))).parse_plot() == (None, [1], None)




from typing import Iterable

from .lexer import Lexer


def is_option(x):
    return isinstance(x, str)

def is_array(x):
    return isinstance(x, Iterable) and not isinstance(x, str)

def is_callable_or_array(x):
    return callable(x) or is_array(x)


class Parser:
    def __init__(self, args):
        self.lex = Lexer(args)

    def has_next(self):
        return self.lex.has_next()
    
    def peek(self, n = 0):
        return self.lex.peek(n)
    
    def read(self):
        return self.lex.read()
    
    def parse_plot(self):
        x = self.read()
        y = None
        o = None
        
        if is_callable_or_array(self.peek()):
            y = self.read()
        else:
            x, y = None, x

        if is_option(self.peek()):
            o = self.read()

        return x, y, o
        
    def parse(self):
        plots = []
        while self.has_next():
            if (is_callable_or_array(self.peek())):
                plots.append(self.parse_plot())
            else:
                print("Error: expected function or array, got", self.read())

        return plots
    


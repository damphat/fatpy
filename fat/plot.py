import matplotlib.pyplot as plt
import numpy as np

from .lexer import Lexer
from .parser import Parser

def plot3d(f, *args, a = None, b = None, n=None, cmap='viridis', **kwargs):
    plot.a = a if a is not None else plot.a
    plot.b = b if b is not None else plot.b
    plot.n = n if n is not None else plot.n
    x = np.linspace(plot.a, plot.b, plot.n)
    y = np.linspace(plot.a, plot.b, plot.n)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax = plt.subplot(111, projection='3d')
    return ax.plot_surface(X, Y, Z, *args, cmap=cmap, **kwargs ) # type: ignore

def show3d(f, *args, **kwargs):
    if f is not None:
        plot3d(f, *args, **kwargs)
    return plt.show()

def plot(*args, a = None, b = None, n=None, **kwargs):
    plot.a = a if a is not None else plot.a
    plot.b = b if b is not None else plot.b
    plot.n = n if n is not None else plot.n

    args = Parser(Lexer(args)).parse()
    new_args = []
    for x, y, o in args:
        if x is None:
            if callable(y):
                x = np.linspace(plot.a, plot.b, plot.n)
            else:
                x = np.arange(len(y))
        if callable(y):
            y = [y(t) for t in x]

        if (o is None):
            new_args.extend((x, y))
        else:
            new_args.extend((x, y, o))

    return plt.plot(*new_args, **kwargs)
        

def show(*args, **kwargs):
    if len(args) > 0:
        plot(*args, **kwargs)
    return plt.show()

plot.a = -1
plot.b = 1
plot.n = 100

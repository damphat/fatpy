from typing import Iterable
import matplotlib.pyplot as plt
import numpy as np

def _plot_func(f1, f2 = None, *args, **kwargs):
    T = np.linspace(plot.a, plot.b, plot.n)
    if f2 is None:
        _plotXY(T, [f1(t) for t in T],*args, **kwargs)
    else:
        _plotXY([f1(t) for t in T], [f2(t) for t in T],*args, **kwargs)


def _plotByIndex(y, *args, **kwargs):
    x = np.arange(len(y))
    _plotXY(x, y, *args, **kwargs)

def _plotXY(x, y, *args, **kwargs):
    plt.plot(x, y, *args, **kwargs)

def plot(*args, a = None, b = None, n=None, **kwargs):
    plot.a = a if a is not None else plot.a
    plot.b = b if b is not None else plot.b
    plot.n = n if n is not None else plot.n

    # non callable or array args
    args1 = [arg for arg in args if not callable(arg) and not plot.isArray(arg)]

    nargs = len(args)
    i = 0
    while i < nargs:
        f1 = args[i]
        f2 = args[i+1] if i+1 < nargs else None

        if callable(f1):
            if callable(f2):
                _plot_func(f1, f2, *args1, **kwargs)
                i+=1
            else:
                _plot_func(f1, None, *args1, **kwargs)
        elif plot.isArray(f1):
            if plot.isArray(f2):
                _plotXY(f1, f2, *args1, **kwargs)
                i+=1
            else:
                _plotByIndex(f1, *args1, **kwargs)
        i+=1


def show():
    plt.show()

plot.a = -1
plot.b = 1
plot.n = 100
plot.isArray = lambda x: isinstance(x, Iterable) and not isinstance(x, str)

print('fatpy/plot.py')


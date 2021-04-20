from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect


def hello(a, b):
    if a < b:
        c: int = a
        a: int = b
        b: int = c

    while b != 0:
        c: int = a
        a: int = b
        b: int = c % b
    return a


cfg = gen_cfg(inspect.getsource(hello))
graph = to_graph(cfg)
Source(graph)

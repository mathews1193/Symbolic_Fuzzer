from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect
from Examples import function1

cfg = gen_cfg(inspect.getsource(function1.gcd))
graph = to_graph(cfg)
Source(graph)

from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect
from Examples import function1, function2, function3, function4, function5


# testing function 1
cfg = gen_cfg(inspect.getsource(function1.gcd))
graph = to_graph(cfg)
Source(graph)

# testing function 2
cfg = gen_cfg(inspect.getsource(function2.check_triangle))
graph = to_graph(cfg)
Source(graph)

# testing function 3
cfg = gen_cfg(inspect.getsource(function3.Hello))
graph = to_graph(cfg)
Source(graph)


from fuzzingbook.ConcolicFuzzer import ArcCoverage
from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect

from Examples import function3, function4
from Examples.function1 import gcd
from Examples.function2 import check_triangle
from Examples.function5 import quad_solver

with ArcCoverage() as cov:
    gcd(64, 8)
    check_triangle(0, 0, 0)


# testing function 1
Source(to_graph(gen_cfg(inspect.getsource(gcd)), arcs=cov.arcs()).render("Results/GCD"))

# testing function 2
Source(to_graph(gen_cfg(inspect.getsource(check_triangle)), arcs=cov.arcs()).render("Results/Check_Triangle"))

# testing function 3 (function needs to be changed)
#graph = to_graph(gen_cfg(inspect.getsource(function3.Hello)))
#Source(graph.render("Hello"))

# testing function 4 (function needs to be changed)
#graph = to_graph(gen_cfg(inspect.getsource(function4.carsList)))
#Source(graph.render("Car List"))

# testing function 5
Source(to_graph(gen_cfg(inspect.getsource(quad_solver)), arcs=cov.arcs()).render("Results/Quad Solver"))


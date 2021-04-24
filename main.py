from fuzzingbook.ConcolicFuzzer import ArcCoverage
from fuzzingbook.ControlFlow import gen_cfg, to_graph
from contextlib import contextmanager
from graphviz import Source
import inspect

from Examples.examples import gcd, check_triangle, abs_value, quad_solver, calculate_sum

with ArcCoverage() as cov:
    gcd(64, 8)
    abs_value(-30)
    quad_solver(1, -5, -24)
    calculate_sum(1, 2, 94, 6, 2, 8, 9, 20, 43, 2)  # 187

# testing function 1
Source(to_graph(gen_cfg(inspect.getsource(gcd)), arcs=cov.arcs()).render("CFG/GCD/GCD1"))

# testing function 2

Source(to_graph(gen_cfg(inspect.getsource(check_triangle)), arcs=cov.arcs()).render("CFG/Check_Triangle/Check_Triangle1"))

# testing function 3

Source(to_graph(gen_cfg(inspect.getsource(abs_value)), arcs=cov.arcs()).render("CFG/Abs_value/Abs_value1"))

# testing function 4
Source(to_graph(gen_cfg(inspect.getsource(calculate_sum)), arcs=cov.arcs()).render("CFG/Calculate_sum/Calculate_sum1"))

# testing function 5
Source(to_graph(gen_cfg(inspect.getsource(quad_solver)), arcs=cov.arcs()).render("CFG/Quad Solver/Quad Solver1"))


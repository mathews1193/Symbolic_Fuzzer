from fuzzingbook.ConcolicFuzzer import ArcCoverage
from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect

from Examples.examples import gcd, check_triangle, abs_value, quad_solver, calculate_sum
from symbolic_fuzzer import SymbolicFuzzer

print("1- GCD")
print("2- Check Triangle")
print("3- Absolute Value")
print("4- Quad Solver")
print("5- Sum")
option = input("Enter Option")

if option ==  "1":
    symfz_ct = SymbolicFuzzer(gcd)
elif option == "2":
    symfz_ct = SymbolicFuzzer(check_triangle)
elif option == "3":
    symfz_ct = SymbolicFuzzer(abs_value)
elif option == "4":
    symfz_ct = SymbolicFuzzer(quad_solver)
elif option == "5":
    symfz_ct = SymbolicFuzzer(calculate_sum)
else:
    print("Invalid option! Try Again.")


paths = symfz_ct.get_all_paths(symfz_ct.fnenter)

print("Number of paths for function")
print(len(paths))

for i in range(len(paths)):
    txt = "Path: {}"
    print(txt.format(i))
    constraints = symfz_ct.extract_constraints(paths[i].get_path_to_root())
    print(constraints)


# testing function 1


# testing function 2

#Source(to_graph(gen_cfg(inspect.getsource(check_triangle)), arcs=cov.arcs()).render("CFG/Check_Triangle/Check_Triangle1"))

# testing function 3

#Source(to_graph(gen_cfg(inspect.getsource(abs_value)), arcs=cov.arcs()).render("CFG/Abs_value/Abs_value1"))

# testing function 4
#Source(to_graph(gen_cfg(inspect.getsource(calculate_sum)), arcs=cov.arcs()).render("CFG/Calculate_sum/Calculate_sum1"))

# testing function 5
#Source(to_graph(gen_cfg(inspect.getsource(quad_solver)), arcs=cov.arcs()).render("CFG/Quad Solver/Quad Solver1"))


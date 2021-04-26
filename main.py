from fuzzingbook.ConcolicFuzzer import ArcCoverage
from fuzzingbook.ControlFlow import gen_cfg, to_graph
from graphviz import Source
import inspect

from Examples.examples import gcd, check_triangle, abs_value, quad_solver, calculate_sum, fib
from symbolic_fuzzer import SymbolicFuzzer

print("1- GCD")
print("2- Check Triangle")
print("3- Absolute Value")
print("4- Sum")
print("5- Quad Solver")
print("6 - Fib")
option = input("Enter Option")

if option ==  "1":
    # testing function 1
    Source(to_graph(gen_cfg(inspect.getsource(gcd))).render("CFG/GCD/GCD1"))
    symfz_ct = SymbolicFuzzer(gcd)  # Works
elif option == "2":
    # testing function 2
    Source(to_graph(gen_cfg(inspect.getsource(check_triangle))).render("CFG/Check_Triangle/Check_Triangle1"))
    symfz_ct = SymbolicFuzzer(check_triangle)  # Works
elif option == "3":
    # testing function 3
    Source(to_graph(gen_cfg(inspect.getsource(abs_value))).render("CFG/Abs_value/Abs_value1"))
    symfz_ct = SymbolicFuzzer(abs_value)  # Works
elif option == "4":
    # testing function 4
    Source(to_graph(gen_cfg(inspect.getsource(calculate_sum))).render("CFG/Calculate_sum/Calculate_sum1"))
    symfz_ct = SymbolicFuzzer(calculate_sum)  # Does not work due to list being the argument
elif option == "5":
    # testing function 5
    Source(to_graph(gen_cfg(inspect.getsource(quad_solver))).render("CFG/Quad Solver/Quad Solver1"))
    symfz_ct = SymbolicFuzzer(quad_solver)  # Does not work due to division by zero paths in function

elif option == "6":
    # testing function 6
    Source(to_graph(gen_cfg(inspect.getsource(fib))).render("CFG/Fib/Fib1"))
    symfz_ct = SymbolicFuzzer(fib)  # Does not work due to the loop involved in the function
else:
    print("Invalid option! Try Again.")

paths = symfz_ct.get_all_paths(symfz_ct.fnenter)

print("Number of paths for function")
print(len(paths))

#generates the constraints in the path
for i in range(len(paths)):
    txt = "Path: {}"
    print(txt.format(i))
    constraints = symfz_ct.extract_constraints(paths[i].get_path_to_root())
    print(constraints)


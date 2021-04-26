import ast
import inspect

from fuzzingbook.ControlFlow import PyCFG
from fuzzingbook.SymbolicFuzzer import SimpleSymbolicFuzzer, to_src, PNode, to_single_assignment_predicates

from Examples.examples import check_triangle, abs_value, calculate_sum, gcd, quad_solver


class SymbolicFuzzer(SimpleSymbolicFuzzer):
    def get_all_paths(self, fenter):
        path_lst = [PNode(0, fenter)]
        completed = []
        for i in range(self.max_iter):
            new_paths = [PNode(0, fenter)]
            for path in path_lst:
                # explore each path once
                if path.cfgnode.children:
                    np = path.explore()
                    for p in np:
                        if path.idx > self.max_depth:
                            break
                        new_paths.append(p)
                else:
                    completed.append(path)
            path_lst = new_paths
        return completed + path_lst

    def extract_constraints(self, path):
        return [to_src(p) for p in to_single_assignment_predicates(path) if p]
from pymoo.problems import get_problem

def problem_dtlz6(n_obj: int):
    return get_problem('dtlz6', n_var=9+n_obj, n_obj=n_obj)
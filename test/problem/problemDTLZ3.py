from pymoo.problems import get_problem

def problem_dtlz3(n_obj: int):
    return get_problem('dtlz3', n_var=9+n_obj, n_obj=n_obj)
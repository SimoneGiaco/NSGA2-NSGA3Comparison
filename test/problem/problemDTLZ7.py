from pymoo.problems import get_problem

def problem_dtlz7(n_obj: int):
    return get_problem('dtlz7', n_var=19+n_obj, n_obj=n_obj)
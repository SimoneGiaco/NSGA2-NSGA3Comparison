from test.problem.problemDTLZ2 import problem_dtlz2
from test.problem.problemDTLZ3 import problem_dtlz3
from test.problem.problemDTLZ6 import problem_dtlz6
from test.problem.problemDTLZ7 import problem_dtlz7
import pandas as pd


# Auxiliary function which specifies the problem ID of n_obj from a user input
def set_problem() -> str:
    problem = input(
        "Enter the problem you want to solve ('DTLZ2', 'DTLZ3', 'DTLZ6' or 'DTLZ7'): "
    ).upper()
    if problem in ["DTLZ2", "DTLZ3", "DTLZ6", "DTLZ7"]:
        return problem
    print(
        "Invalid problem. Please enter 'DTLZ2', 'DTLZ3', 'DTLZ6' or 'DTLZ7'."
    )  # Exception if the user input does not correspond to the ID of one of the problems.
    return set_problem()


# Auxiliary function which sets the value of n_obj from a user input
def num_objective(problem: str) -> int:
    try:
        objective = int(
            input("Enter the number of objectives (2, 3 or 4): ")
        )  # Exception if the input from the user is not a number
        if objective == 2 and problem in ["DTLZ6", "DTLZ7"]:
            print(
                "For 'DTLZ6' and 'DTLZ7' only 3 and 4 objectives are supported"
            )  # n_obj=2 is not supported for these problems, so we treat this case separately.
        elif objective in [2, 3, 4]:
            return objective
        else:
            print("Not tested for more than 4 objectives, try another value.")
    except ValueError as e:
        print(e)
    return num_objective(problem)


#Function which returns the corresponding problem object given the ID (string) of the problem.
def get_prob(problem: str, n_obj: int):
    if problem == 'DTLZ2':
        return problem_dtlz2(n_obj)
    elif problem == 'DTLZ3':
        return problem_dtlz3(n_obj)
    elif problem == 'DTLZ6':
        return problem_dtlz6(n_obj) 
    else:
        return problem_dtlz7(n_obj)


#We collect our choices for the number of max generations in a pandas DataFrame. We pass this to the termination criterion.
def gen_dataframe():
    dict={'DTLZ2':[200,100,500] , 'DTLZ3':[3000,1000,2000] , 'DTLZ6':[100,800,1500] , 'DTLZ7':[100,400,400] }
    gen_table = pd.DataFrame(dict, columns=dict.keys(), index=[2,3,4])
    return gen_table
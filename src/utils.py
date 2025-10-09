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
def set_objective(problem: str) -> int:
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
    return set_objective(problem)
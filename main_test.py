from src.opt import NSGA2_opt, NSGA3_opt, optimization_outcome
from src.utils import set_problem, num_objective


def main():
    while True:
        print("\n1. Solve one of the problems with the NSGA2 algorithm")
        print("2. Solve one of the problems with the NSGA3 algorithm")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            problem = set_problem()
            n_obj = num_objective(problem)
            result = NSGA2_opt(problem, n_obj)
            optimization_outcome(problem, n_obj, result)

        elif choice == "2":
            problem = set_problem()
            n_obj = num_objective(problem)
            result = NSGA3_opt(problem, n_obj)
            optimization_outcome(problem, n_obj, result)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()

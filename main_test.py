from pymoo.visualization.scatter import Scatter
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV
from pymoo.util.ref_dirs import get_reference_directions
from src.opt import NSGA2_opt, NSGA3_opt, get_prob
import numpy as np


#Auxiliary function which specifies the problem ID of n_obj from a user input
def set_problem()-> str:
    problem = input("Enter the problem you want to solve ('DTLZ2', 'DTLZ3', 'DTLZ6' or 'DTLZ7'): ").upper()
    if problem in ['DTLZ2', 'DTLZ3', 'DTLZ6', 'DTLZ7']:
        return problem
    print("Invalid problem. Please enter 'DTLZ2', 'DTLZ3', 'DTLZ6' or 'DTLZ7'.")  #Exception if the user input does not correspond to the ID of one of the problems.
    return set_problem()


#Auxiliary function which sets the value of n_obj from a user input
def set_objective(problem)-> int:
    try:
        objective = int(input("Enter the number of objectives (2, 3 or 4): "))  #Exception if the input from the user is not a number
        if objective == 2 and problem in ['DTLZ6','DTLZ7']:
            print("For 'DTLZ6' and 'DTLZ7' only 3 and 4 objectives are supported") #n_obj=2 is not supported for these problems, so we treat this case separately.
        elif objective in [2,3,4]:
            return objective
        else:
            print("Not tested for more than 4 objectives, try another value.")
    except ValueError as e:
        print(e)
    return set_objective(problem)


#Function providing the metrics and plots for the optimized solution
def optimization_outcome(problem, n_obj, result):

    if n_obj == 4 and problem in ['DTLZ6','DTLZ7']:   #The Pareto front is not implemented in pymoo yet, so we can only compute the Hypervolume
        y=np.max(result.F, axis=0)                    #For the computation of HV we need a reference point. We simply take the max over the non-dominated front.
        index=HV(ref_point=y)
        print(f'Hypervolume: {round(index(result.F),5)}')

    elif n_obj == 4 and problem in ['DTLZ2','DTLZ3']:   #We compute both IGD score and Hypervolume, but with 4 objectives we cannot plot the graph of non-dominated points.
        ref_dirs = get_reference_directions("das-dennis", 4, n_partitions=6)  #The reference directions are needed to determine the pareto front with n_obj > 3.
        pf = get_prob(problem,n_obj).pareto_front(ref_dirs)     #Since problem is a string, we use the function get_prob() to extract the actual problem object.
        index= IGD(pf)
        print(f'IGD Score: {round(index(result.F),5)}')
        y=np.max(result.F, axis=0)
        index2=HV(ref_point=y)
        print(f'Hypervolume: {round(index2(result.F),5)}')
        print(f'Hypervolume Pareto front: {round(index2(pf),5)}') #Simple comparison to see how good the Hypervolume metric is (should be close to that of the Pareto front).

    else:
        pff = get_prob(problem,n_obj).pareto_front() #As before we compute IGD score and Hypervolume. Again we use get_prob() to extract the problem object from the string.
        index= IGD(pff)
        print(f'IGD Score: {round(index(result.F),5)}')
        y=np.max(result.F, axis=0)
        index2=HV(ref_point=y)
        print(f'Hypervolume: {round(index2(result.F),5)}')
        print(f'Hypervolume Pareto front: {round(index2(pff),5)}')
        plot = Scatter()                                              #We add the plot for the non-dominated front (in red) VS points of the Pareto front (in black).
        plot.add(pff, plot_type='scatter', color="black", alpha=0.5)
        plot.add(result.F, facecolor="red", edgecolor="red")
        plot.show()


def main():
    while True:
        print("\n1. Solve one of the problems with the NSGA2 algorithm")
        print("2. Solve one of the problems with the NSGA3 algorithm")
        print("3. Exit")
        choice= input("Enter your choice (1-3): ")

        if choice=="1":
            problem= set_problem()
            n_obj= set_objective(problem)
            result = NSGA2_opt(problem, n_obj)
            optimization_outcome(problem, n_obj, result)

        elif choice=="2":
            problem= set_problem()
            n_obj= set_objective(problem)
            result = NSGA3_opt(problem, n_obj)
            optimization_outcome(problem, n_obj, result)

        elif choice=="3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__=="__main__":
    main()
import numpy as np
import pandas as pd
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV
from pymoo.util.ref_dirs import get_reference_directions
from test.payload.configNSGA2 import get_config_NSGA2
from test.payload.configNSGA3 import get_config_NSGA3
from src.utils import get_prob, gen_dataframe


# Function defining the minimize object for the NSGA2 algorithm.
def NSGA2_opt(problem: str, n_obj: int):
    dict2 = get_config_NSGA2(n_obj)  #Configuration data for the algorithm.
    pop_size=dict2['pop_size']
    prob=get_prob(problem,n_obj)     #Problem object.
    n_var=prob.n_var
    df=gen_dataframe()               #Pandas Dataframe collecting max generations setting.
    X=np.random.rand(pop_size,n_var) #Initial generation.

    algorithm = NSGA2(pop_size=pop_size,
                    sampling=X,
                    crossover=SBX(prob=dict2['SBX_prob'], eta=dict2['SBX_eta']),
                    mutation=PM(prob=dict2['PM_prob'], eta=dict2['PM_eta']),
                    eliminate_duplicates=True)
    return minimize(prob,
                  algorithm,
                  ('n_gen', df.loc[n_obj,problem]),  #Termination criterion.
                  seed=1,
                  save_history=False,   #For faster convergence we do not keep the history.
                  verbose=False)


# Function defining the minimize object for the NSGA3 algorithm.
def NSGA3_opt(problem: str, n_obj: int):
    dict3 = get_config_NSGA3(n_obj)  
    pop_size=dict3['pop_size']
    prob=get_prob(problem,n_obj)    
    n_var=prob.n_var
    df=gen_dataframe()              
    X=np.random.rand(pop_size,n_var)

    algorithm = NSGA3(pop_size=pop_size,
                    ref_dirs=dict3['ref_dirs'],
                    sampling=X,
                    crossover=SBX(prob=dict3['SBX_prob'], eta=dict3['SBX_eta']),
                    mutation=PM(prob=dict3['PM_prob'], eta=dict3['PM_eta']),
                    eliminate_duplicates=True)
    return minimize(prob,
                  algorithm,
                  ('n_gen', df.loc[n_obj,problem]), 
                  seed=1,
                  save_history=False,   
                  verbose=False)


# Function providing the metrics and plots for the optimized solution
def optimization_outcome(problem, n_obj, result):
    y = np.max(result.F, axis=0)  # Reference point needed for the computation of HV. We take the max over the non-dominated front.
    index = HV(ref_point=y)
    ref_dirs = get_reference_directions("das-dennis", 4, n_partitions=6)  # Reference directions needed to determine the pareto front with n_obj > 3.

    if n_obj == 4 and problem in ["DTLZ6","DTLZ7"]:  # The Pareto front is not implemented in pymoo yet, so we can only compute the Hypervolume
        print(f"Hypervolume: {round(index(result.F),5)}")
    
    # We compute both IGD score and Hypervolume.
    elif n_obj == 4 and problem in ["DTLZ2","DTLZ3"]:  
        pf = get_prob(problem, n_obj).pareto_front(ref_dirs)  
        index2 = IGD(pf)
        print(f"IGD Score: {round(index2(result.F),5)}")
        print(f"Hypervolume: {round(index(result.F),5)}")
        print(f"Hypervolume Pareto front: {round(index(pf),5)}")  # Comparison to see how good the Hypervolume metric is (should be close to that of the Pareto front).

    else:
        pff = get_prob(problem, n_obj).pareto_front() 
        index2 = IGD(pff)
        print(f"IGD Score: {round(index2(result.F),5)}")
        print(f"Hypervolume: {round(index(result.F),5)}")
        print(f"Hypervolume Pareto front: {round(index(pff),5)}")
        # We add the plot for the non-dominated front (in red) VS points of the Pareto front (in black).
        plot = (Scatter())  
        plot.add(pff, plot_type="scatter", color="black", alpha=0.5)
        plot.add(result.F, facecolor="red", edgecolor="red")
        plot.save(f"{problem}_{n_obj}_objectives.png")  
        plot.show()
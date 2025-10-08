import numpy as np
import pandas as pd
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize
from test.problem.problemDTLZ2 import problem_dtlz2
from test.problem.problemDTLZ3 import problem_dtlz3
from test.problem.problemDTLZ6 import problem_dtlz6
from test.problem.problemDTLZ7 import problem_dtlz7
from test.payload.configNSGA2 import get_config_NSGA2
from test.payload.configNSGA3 import get_config_NSGA3

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
    dict3 = get_config_NSGA3(n_obj)  #Configuration data for the algorithm.
    pop_size=dict3['pop_size']
    prob=get_prob(problem,n_obj)     #Problem object.
    n_var=prob.n_var
    df=gen_dataframe()               #Pandas Dataframe collecting max generations setting.
    X=np.random.rand(pop_size,n_var) #Initial generation.

    algorithm = NSGA3(pop_size=pop_size,
                    ref_dirs=dict3['ref_dirs'],
                    sampling=X,
                    crossover=SBX(prob=dict3['SBX_prob'], eta=dict3['SBX_eta']),
                    mutation=PM(prob=dict3['PM_prob'], eta=dict3['PM_eta']),
                    eliminate_duplicates=True)
    return minimize(prob,
                  algorithm,
                  ('n_gen', df.loc[n_obj,problem]),  #Termination criterion.
                  seed=1,
                  save_history=False,     #For faster convergence we do not keep the history.
                  verbose=False)

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
from pymoo.util.ref_dirs import get_reference_directions

def get_directions(n_obj: int):
    return get_reference_directions("das-dennis", n_obj, n_partitions=partitions(n_obj))  #We choose Das-Dennis as a method to determine the reference directions for NSGA3. 

def get_config_NSGA3(n_obj: int)-> dict:
    return {
        'pop_size': population(n_obj),
        'ref_dirs': get_directions(n_obj),
        'SBX_prob': 1.0,     #For crossing we choose SBX.
        'SBX_eta': 20, 
        'PM_prob': 0.2,      #For mutation we choose PM.
        'PM_eta': 20
    }

#Function expressing the population size in terms of the number of objectives, according to our configuration choice.
def population(n_obj: int)-> int:
    return 30 if n_obj<=2 else 100

#Auxiliary function giving the parameter n_partitions required for Das-Dennis in terms of the number of objectives. Chosen so that # of reference directions < population. 
def partitions(n_obj: int)-> int:
    dict={2 : 20, 3 : 12, 4 : 6}
    if n_obj <= 4:
        return dict[n_obj]
    else:
        return n_obj
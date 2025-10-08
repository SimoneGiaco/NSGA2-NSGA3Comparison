def get_config_NSGA2(n_obj: int)-> dict:
    return {
        'pop_size': population(n_obj),
        'SBX_prob': 1.0,   #For crossing we choose SBX.
        'SBX_eta': 20, 
        'PM_prob': 0.2,    #For mutation we choose PM.
        'PM_eta': 20
    }

#Function expressing the population size in terms of the number of objectives, according to our configuration choice.
def population(n_obj: int)-> int:
    return 30 if n_obj<=2 else 100
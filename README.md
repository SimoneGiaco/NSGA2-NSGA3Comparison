[![Python application test with Github](https://github.com/SimoneGiaco/NSGA2-NSGA3Comparison/actions/workflows/main.yml/badge.svg)](https://github.com/SimoneGiaco/NSGA2-NSGA3Comparison/actions/workflows/main.yml)


# NSGA2-NSGA3Comparison
Comparison of the algorithms NSGAII and NSGAIII on a set of problems from the DTLZ suite.

## Organization of the project 

I chose a subset of problems from the DTLZ suite with different features: two have a convex Pareto front (DTLZ2 and DTLZ3). The former is easier and the latter more challenging. Then I picked DTLZ6 whose Pareto front has higher codimension to see how the algorithms behave in this case and finally DTLZ7 because it has a non connected Pareto front. For each problem I consider 2, 3 and 4 objectives to compare the behaviour of the two algorithms as we increase the number of objectives. For DTLZ6 and DTLZ7 the case with n_obj=2 is not implemented in pymoo so I have not considered them. 

I chose for both algorithms SBX for crossover and PM for mutation, with parameters close to those recommended in the literature but adjusted to speed up the execution. The number of variables for each problem is the one recommended in the original paper: 9+n_obj for DTLZ2,3,6 and 19+n_obj for DTLZ7. For the direction selection required by NSGAIII I used the Das-Dennis method. All these data are collected in the python files in the test directory. The information are then passed to the opt.py file in the src directory, which extracts the result of the optimization.

I chose generation as termination criterion. I have tuned the max number of generations with a preliminary run. Then I performed 10 runs for each problem with varying initial population to test the consistency of the results. These data are stored in a pandas dataframe defined in the opt.py file.

I compare the two algorithms using the metrics IGD (not available with 4 objectives for DTLZ6 and DTLZ7) and hypervolume. Their indications are always consistent. 

The code with all these runs is included in a notebook in the result directory, together with the detailed report. 

The main_test.py can be used to run a single time each problem with both algorithms. The output includes all the metrics and the plots for 2 and 3 objectives. Since the plots are not visible when executed in Codespaces, a copy of the plot is saved automatically each time for visualization in the main directory.

## Instructions

Execute the main file from a terminal (with e.g. python main_test.py). The terminal will then ask for further instructions to specify the desired algorithm and problem. The problem is specified by the code 'dtlz2', 'dtlz3', 'dtlz6' or 'dtlz7' and the number of objectives. 

## Results of the analysis 

The general outcome is that for 2 objectives both algorithms perform well, with a slight advantage for NSGAII. For 3 objectives they are comparable (which one is better depends on the problem) but NSGAIII shows in general a better distribution of solutions. In the case of 4 objectives NSGAIII clearly outperforms NSGAII.

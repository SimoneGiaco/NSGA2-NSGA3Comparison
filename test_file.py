from src.opt import NSGA2_opt, NSGA3_opt, get_prob


def test_problem1():
    assert 9 + 3 == get_prob("DTLZ2", 3).n_var


def test_problem2():
    assert 4 == get_prob("DTLZ3", 4).n_obj


def test_problem3():
    assert 3 == get_prob("DTLZ6", 3).pareto_front()[0].shape[0]


def test_problem4():
    assert 2 == get_prob("DTLZ2", 2).pareto_front()[0].shape[0]


def test_nsgaii():
    result = NSGA2_opt("DTLZ7", 3)
    assert result.F[0].shape[0] == 3


def test_nsgaiii():
    result = NSGA3_opt("DTLZ3", 2)
    assert result.F[0].shape[0] == 2

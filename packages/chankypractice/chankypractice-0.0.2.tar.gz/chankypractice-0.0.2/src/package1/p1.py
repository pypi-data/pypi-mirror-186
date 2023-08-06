from numpy.random import seed
from numpy.random import rand


def p1_sum(a, s=1):
    seed(s)
    b = rand(1)
    return a + b

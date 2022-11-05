import math

POPULATION_SIZE = 12
PANJANG_KROMOSOM = 18
PROBABILITAS_MUTASI = 0.1
PROBABILITAS_CROSSOVER = 0.9
A = 0.000000001


def heuristic(x, y):
    return (math.cos(math.radians(x)) + math.sin(math.radians(y)))**2 / (x**2 + y**2)

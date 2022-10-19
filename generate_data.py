import math
import numpy as np


DOMAIN = (-10, 10)
ELEMS = 100

def f(x) -> int:
    return 5 * math.pow(x, 3) - 2 * math.pow(x, 2) + 3 * x - 17

#---------------------------------------------------------------------------------#

step = (abs(DOMAIN[0]) + abs(DOMAIN[1])) / ELEMS

def generate_data():
    print(f"1 {ELEMS} {DOMAIN[0]} {DOMAIN[1]} {ELEMS}")
    for i in np.arange(DOMAIN[0], DOMAIN[1]+1, step):
        print(f"{i} {f(i)}")

generate_data()
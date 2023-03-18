# from vpython import *
from time import time
import sys
import os

module_path = os.path.abspath(os.path.join('.', "components"))
sys.path.append(module_path)

from components import solver
rubiks_cube = solver.RubiksCube

# scramble and solve multiple times

# obj=rubiks_cube(1, 0)
# t=time()
# for i in range(100):
#     obj.scramble(50)
#     obj.solve()
# print(time()-t)
# print("DONE")


# open commander


obj = rubiks_cube(1, 0)
obj.commander()

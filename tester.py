from vpython import *
from time import sleep, time
from random import randint

from rubik_3 import rubiks_cube


# scramble and solve multiple times

# obj=rubiks_cube(1, 0)
# t=time()
# for i in range(100):
#     obj.scramble(50)
#     obj.solve()
# print(time()-t)
# print("DONE")


# open commander


obj=rubiks_cube(10, 0.1)
obj.commander()
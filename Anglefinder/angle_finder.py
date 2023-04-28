from math import *

def find_arccos(adj, hyp):
    acos_x = (adj / hyp)
    result = acos(acos_x)
    result = result * (180 / pi)
    return result


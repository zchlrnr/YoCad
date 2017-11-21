import numpy as np
def ReadBearing(Sdata):
    n = int(Sdata[0])
    if n == 1:
        print("Yell at Zach to write the A sized bearing thing")
    elif n==2:
        print("Yell at Zach to write the B sized bearing thing")
    elif n==3:
        Bdata = np.loadtxt('BearingSeatCoords_C.txt')
    return Bdata

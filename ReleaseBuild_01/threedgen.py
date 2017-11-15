from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
from math import pi
def threedgen(bulkmat, angsteps):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x=[]
    y=[]
    z=[]
    bigx=[]
    bigy=[]
    bigz=[]
    for i in range(0, len(bulkmat)):
        x.append(bulkmat[i,0])
        y.append(bulkmat[i,1])
        z.append(0)
    for i in range(0,len(bulkmat)):
        for j in range(0,angsteps):
            # j is current angular step number
            # i is current point in original profile
            # the y value of the i'th entry is the radius
            bigx.append(x[i])
            bigy.append(math.cos(j*(2*pi)/angsteps)*y[i])
            bigz.append(math.sin(j*(2*pi)/angsteps)*y[i])

    ax.scatter(bigx, bigy, bigz)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

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
    '''
    #bigy.append(math.cos(j*(2*pi)/angsteps)*y[i])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    '''
    '''
    x = np.outer(np.linspace(-2,2,2), np.ones(2))
    y = x.copy().T
    z = np.cos(x**2 + y**2)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,z, linewidth=0)
    print(x)
    print(type(x))
    print(y)
    '''
    x = np.array([[1,2,3],[1,2,3],[1,2,3]])
    y = np.array([[1,1,1],[1,1,1],[1,1,1]])
    z = np.array([[0,0,0],[0,0,0],[0,0,0]])
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,z)

    plt.show()

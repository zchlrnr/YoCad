from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
def threedgen(bulkmat, angsteps):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    a = bulkmat.tolist()
    print(a)
    #for i in range(0, len(bulkmat)):


    #ax.scatter(xs, ys, zs)

    #ax.set_xlabel('X Label')
    #ax.set_ylabel('Y Label')
    #ax.set_zlabel('Z Label')

    #plt.show()

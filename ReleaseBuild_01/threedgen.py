import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
def threedgen(bulkmat, angsteps):
    # input xy coordinates
    xy = np.array(bulkmat)
    # radial component is x values of input
    r = xy[:,1]
    # angular component is one revolution of 60 steps
    phi = np.linspace(0, 2*np.pi, angsteps)
    # create grid
    R,Phi = np.meshgrid(r,phi)
    # transform to cartesian coordinates
    X = R*np.cos(Phi)
    Y = R*np.sin(Phi)
    # Z values are y values, repeated 60 times
    Z = np.tile(xy[:,0],len(Y)).reshape(Y.shape)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax2 = fig.add_axes([0.1,0.7,0.15,.2])
    ax2.plot(xy[:,0],xy[:,1], color="k")
    ax.plot_surface(Z, Y, X, alpha=0.5, color='gold', rstride=1, cstride=1)
    plt.axis('equal')
    plt.show()

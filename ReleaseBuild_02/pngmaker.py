import numpy as np
import matplotlib.pyplot as plt

def pngmaker(Bdata, Pdata, Rdata, Cdata, megamatx, megamaty):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []
    for i in range(0, len(Bdata)):
        x1 = np.append(x1, Bdata[i, 0])
        y1 = np.append(y1, Bdata[i, 1])
    # Generates coordinates of profile
    for i in range(0, len(Pdata)):
        x2 = np.append(x2, Pdata[i, 0])
        y2 = np.append(y2, Pdata[i, 1])
    # Generates coordinates of rim
    for i in range(0, len(Rdata)):
        x3 = np.append(x3, Rdata[i, 0])
        y3 = np.append(y3, Rdata[i, 1])
    # Generates coordinates of cup
    for i in range(0, len(Cdata)):
        x4 = np.append(x4, Cdata[i, 0])
        y4 = np.append(y4, Cdata[i, 1])
    font = {'family': 'sans',
            'color':  'black',
            'weight': 'normal',
            'size': 16,
            }
    plt.title('Scale Quarter Section (mm)', fontdict=font)
    plt.xlabel('x axis (mm)',fontdict=font)
    plt.ylabel('y axis (mm)',fontdict=font)
    plt.plot(x2, y2, "ro")
    plt.plot(x2, y2, "b--")
    plt.plot(x3,y3, "ro")
    plt.plot(x3,y3, "b--")
    plt.plot(x4,y4, "ro")
    plt.plot(x4,y4, "b--")
    plt.axis('equal')
    plt.savefig('figure.png')
    plt.plot(megamatx, megamaty, 'k')
    plt.plot(Bdata[:,0], Bdata[:,1], 'k')
    plt.axis('equal')
    plt.savefig('figure.png')
    plt.grid()
    plt.show()
    return

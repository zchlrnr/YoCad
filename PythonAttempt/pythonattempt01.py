# Perhaps a good way to do this is to use nump and scipy
# First, construct the coordinate pairs of the bearing seat
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.special import binom
from Bezier import Bezier

Bdata = np.loadtxt('BearingSeatCoords_C.txt')
Sdata = np.genfromtxt('specs.txt', usecols=0, delimiter=',', dtype=None)
Pdata = np.loadtxt('profile.txt', delimiter=',')
Rdata = np.loadtxt('rim.txt', delimiter=',')
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for i in range(0, len(Bdata)):
    x1 = np.append(x1, Bdata[i, 0])
    y1 = np.append(y1, Bdata[i, 1])

for i in range(0, len(Pdata)):
    x2 = np.append(x2, Pdata[i, 0])
    y2 = np.append(y2, Pdata[i, 1])

for i in range(0, len(Rdata)):
    x3 = np.append(x3, Rdata[i, 0])
    y3 = np.append(y3, Rdata[i, 1])

xp, yp = Bezier(list(zip(x2, y2))).T
xr, yr = Bezier(list(zip(x3, y3))).T

plt.plot(xp, yp)
plt.plot(xr, yr)
plt.plot(x1, y1)
plt.axis('equal')
plt.plot(x2, y2, "ro")
plt.plot(x2, y2, "b--")
plt.show()

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
Cdata = np.loadtxt('cup.txt',delimiter=',')
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
# Generates coordinates of bearing seat
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

xp, yp = Bezier(list(zip(x2, y2))).T
xr, yr = Bezier(list(zip(x3, y3))).T
xc, yc = Bezier(list(zip(x4, y4))).T

plt.plot(xp, yp)
plt.plot(xr, yr)
plt.plot(xc, yc)

plt.axis('equal')
plt.plot(x1, y1)
plt.plot(x2, y2, "ro")
plt.plot(x2, y2, "b--")
plt.plot(x3,y3, "ro")
plt.plot(x3,y3, "b--")
plt.plot(x4,y4, "ro")
plt.plot(x4,y4, "b--")
plt.show()

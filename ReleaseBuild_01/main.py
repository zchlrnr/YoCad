import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.special import binom
from Bezier import Bezier
from BearingSubtract import BearingSubtract
from ProfileSubtract import ProfileSubtract
from RimSubtract import RimSubtract
from CupSubtract import CupSubtract
from centroid import centroid
from minthick import minthick
Bdata = np.loadtxt('BearingSeatCoords_C.txt')
Sdata = np.genfromtxt('specs.txt', usecols = 0, delimiter=',', dtype=None)
Pdata = np.loadtxt('profile.txt', delimiter=',')
Rdata = np.loadtxt('rim.txt', delimiter=',')
Cdata = np.loadtxt('cup.txt', delimiter = ',')
Blank_Radius = Sdata[1]/2
Blank_Length = Sdata[2]/2
Blank_Volume = ((Blank_Radius**2)*math.pi)*Blank_Length
RunningVolume = Blank_Volume
RunningVolume = RunningVolume -  BearingSubtract(3)
Pxc = []
Pyc = []
Rxc = []
Ryc = []
Cxc = []
Cyc = []
for i in range(0,len(Pdata)):
    Pxc = np.append(Pxc, Pdata[i,0])
    Pyc = np.append(Pyc, Pdata[i,1])
Px, Py = Bezier(list(zip(Pxc, Pyc))).T
RunningVolume = RunningVolume - ProfileSubtract(Px, Py)
for i in range(0,len(Rdata)):
    Rxc = np.append(Rxc, Rdata[i,0])
    Ryc = np.append(Ryc, Rdata[i,1])
Rx, Ry = Bezier(list(zip(Rxc,Ryc))).T
RunningVolume = RunningVolume - RimSubtract(Rx, Ry)
for i in range(0,len(Cdata)):
    Cxc = np.append(Cxc, Cdata[i,0])
    Cyc = np.append(Cyc, Cdata[i,1])
Cx, Cy = Bezier(list(zip(Cxc, Cyc))).T
RunningVolume = RunningVolume - CupSubtract(Cx, Cy)
density = Sdata[7]/(10**(9))
halfmass = RunningVolume*density * (10**3)
prof = np.column_stack((Px, Py))
rim = np.column_stack((Rx, Ry))
cup = np.column_stack((Cx, Cy))
megamat = np.concatenate((prof,rim,cup),axis=0)
megamatx = np.concatenate((Px, Rx, Cx),axis=0)
megamaty = np.concatenate((Py, Ry, Cy),axis=0)
bulkmat = np.concatenate((Bdata,megamat), axis=0)
Cx, Cy, RimWeightRatio = centroid(bulkmat)
# CHECKING MINIMUM WALL THICKNESS
floatingminthick = minthick(Bdata, Sdata, prof, rim, cup)
print(floatingminthick)
# ALL BELOW PERTAINS TO PLOTTING
font = {'family': 'sans',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
plt.title('Scale Quarter Section (mm)', fontdict=font)
plt.xlabel('z axis (mm)',fontdict=font)
plt.ylabel('x axis (mm)',fontdict=font)
mass = str(halfmass)[:6]
plt.text(15, 5, 'mass =%s grams' % (mass))
Cxs = str(Cx)[:5]
Cys = str(Cy)[:5]
plt.text(12,3.5, 'Center of mass @ (%s, %s)' %(Cxs, Cys))
RimWeight_s = str(RimWeightRatio)[:6]
plt.text(13, 2, 'RimWeightRatio = %s' % RimWeight_s)
plt.plot(megamatx, megamaty, 'k')
# And now the bearing seat must be plotted.
plt.plot(Bdata[:,0], Bdata[:,1], 'k')
plt.axis('equal')
plt.savefig('figure.png')
plt.grid()
plt.show()
Bmatrix2 = [(float(x[0]), float(x[1]),) for x in Bmatrix]
prof2 = [(float(x[0]), float(x[1]),) for x in prof]
rim2 = [(float(x[0]), float(x[1]),) for x in rim]
cup2 = [(float(x[0]), float(x[1]),) for x in cup]
from dxfwrite import DXFEngine as dxf
drawing = dxf.drawing('drawing.dxf')
polyline= dxf.polyline(linetype='LINE')
polyline.add_vertices(Bmatrix2)
polyline.add_vertices(prof2)
polyline.add_vertices(rim2)
polyline.add_vertices(cup2)
drawing.add(polyline)
drawing.save()

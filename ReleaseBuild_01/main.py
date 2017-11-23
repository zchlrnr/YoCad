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
from threedgen import threedgen
from fracturearea import fracturearea
from ReadBearing import ReadBearing
Sdata = np.genfromtxt('specs.txt', usecols = 0, delimiter=',', dtype=None)
Bdata = ReadBearing(Sdata)
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
'''
This section creates the megamatrix of points connected by lines to
one another.  IT OMITS THE BEARING SEAT
'''
prof = np.column_stack((Px, Py))
rim = np.column_stack((Rx, Ry))
cup = np.column_stack((Cx, Cy))
megamat = np.concatenate((prof,rim,cup),axis=0)
megamatx = np.concatenate((Px, Rx, Cx),axis=0)
megamaty = np.concatenate((Py, Ry, Cy),axis=0)
bulkmat = np.concatenate((Bdata,megamat), axis=0)
#Creates coordinate pair that makes up physical location of centroid of
#... 2d quarter section, and computes RimWeightRatio
Cx, Cy, RimWeightRatio = centroid(bulkmat)
# CHECKING MINIMUM WALL THICKNESS AGAINST SPECIFIED ALLOWABLE MINIMUM
floatingminthick = minthick(Bdata, Sdata, prof, rim, cup)
thick_criteria = Sdata[8] #this is in millimeters
# ERROR CHECKING OCCURS IN THIS SECTION
# IF AN ERROR OCCURS, THEN THE BREAKFLAG, HEREFORTH SET EQUAL TO ZERO,
# ... WILL BE SET EQUAL TO A NON-ZERO VALUE
thickflag = 0
if floatingminthick <= thick_criteria:
    thickflag = 1
    print("ERRROR: YOUR DESIGN VIOLATES MINIMUM WALL THICKNESS")
    print("THIS CAN EITHER BE DUE TO SELF INTERSECTION, OR A GENUINELY")
    print("TOO THIN WALL.")
    #Yeah, this ain't workin, yet.
    farea = fracturearea(floatingminthick, thick_criteria, Sdata, prof, rim, cup)
# OUTPUT SECTION
# Configuration of the text in the 2d image
font = {'family': 'sans',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
plt.title('Scale Quarter Section (mm)', fontdict=font)
plt.xlabel('x axis (mm)',fontdict=font)
plt.ylabel('y axis (mm)',fontdict=font)
mass = str(halfmass)[:6]
plt.text(15, 5, 'mass =%s grams' % (mass))
Cxs = str(Cx)[:5]
Cys = str(Cy)[:5]
plt.text(12,3.5, 'Center of mass @ (%s, %s)' %(Cxs, Cys))
RimWeight_s = str(RimWeightRatio)[:6]
plt.text(13, 2, 'RimWeightRatio = %s' % RimWeight_s)
#THIS ONE LINE BELOW IS RESPONSIBLE FOR PLOTTING EVERYTHING THAT I
#... NOT THE BEARING SEAT
plt.plot(megamatx, megamaty, 'k')
#This plots the bearing seat, WITHOUT AXLE HOLE YET DRILLED .
plt.plot(Bdata[:,0], Bdata[:,1], 'k')
#This plots the section of filled area if and only if the minimum wall
#... thickness criteria is violated.
if thickflag == 1:
    plt.fill(farea[:,0],farea[:,1], 'k', alpha=0.3)
plt.plot()
plt.axis('equal')
plt.savefig('figure.png')
plt.grid()
plt.show()
#Generation of 3d plot in matplotlib
angsteps = 20
threedgen(bulkmat, angsteps)
# Generation of CAD file
Bmatrix2 = [(float(x[0]), float(x[1]),) for x in Bdata]
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

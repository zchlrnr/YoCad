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

'''
    This code will be structured for the purpose of having a running
calculation of mass.  In order to properly propogate this,
a function which determines volume subtracted will be neccesary.
'''

# First, a blank of appropriate size will be created from 'specs.txt'
Sdata = np.genfromtxt('specs.txt', usecols = 0, delimiter=',', dtype=None)
# Sdata[0] = bearing type.  If it is '3', then it uses a C bearing
# Sdata[1] = Diameter, blank "height" will be gotten by halving this
# Sdata[2] = Width, blank "length" will be gotten by halving this
# Sdata[4] = Axle length, hole depth will be pulled from this
# Sdata[5] = unit system of axle hole, if 1 then metric and mm
# Sdata[6] = pilot hole diameter of hole.  Radius will be half of this
# Sdata[7] = density of material in kg/m^3
#Generating volume varitable from specs document
Blank_Radius = Sdata[1]/2
Blank_Length = Sdata[2]/2
Blank_Volume = ((Blank_Radius**2)*math.pi)*Blank_Length
# ALL VOLUMES WILL BE MEASURED IN CUBIC MILIMETERS
RunningVolume = Blank_Volume

# THIS IS THE SUBTRACTION OF THE CUT FROM THE BEARING
RunningVolume = RunningVolume -  BearingSubtract(3)
# Now, The volume of the profile needs to be subtracted
# Pxc and Pyc are the coordinates of the control points in from
# ... 'profile.txt'
Pxc = []
Pyc = []
Pdata = np.loadtxt('profile.txt', delimiter=',')
for i in range(0,len(Pdata)):
    Pxc = np.append(Pxc, Pdata[i,0])
    Pyc = np.append(Pyc, Pdata[i,1])
# Px and Py are the many value long column vectors of the data points
# ... which compose the Bezier curve
Px, Py = Bezier(list(zip(Pxc, Pyc))).T
RunningVolume = RunningVolume - ProfileSubtract(Px, Py)

# Now, the volume of the rim needs to be subtracted
# Rxc and Ryx are the coordinates of the control points in from
# ...'rim.txt'
Rxc = []
Ryc = []
Rdata = np.loadtxt('rim.txt', delimiter=',')
for i in range(0,len(Rdata)):
    Rxc = np.append(Rxc, Rdata[i,0])
    Ryc = np.append(Ryc, Rdata[i,1])
Rx, Ry = Bezier(list(zip(Rxc,Ryc))).T
RunningVolume = RunningVolume - RimSubtract(Rx, Ry)

# Now, the volume of the cup needs to be subtracted
# Cxc and Cyc are the coordinates of the control points in from
# ... 'cup.txt'
Cxc = []
Cyc = []
Cdata = np.loadtxt('cup.txt', delimiter = ',')
for i in range(0,len(Cdata)):
    Cxc = np.append(Cxc, Cdata[i,0])
    Cyc = np.append(Cyc, Cdata[i,1])
Cx, Cy = Bezier(list(zip(Cxc, Cyc))).T
RunningVolume = RunningVolume - CupSubtract(Cx, Cy)

# The running volume is now complete in cubic milimeters.
# Now you will call the material density from 'specs.txt'
density = Sdata[7]/(10**(9)) #THIS IS IN KG/MM^3
halfmass = RunningVolume*density * (10**3) #THIS IS IN GRAMS
'''
The next step is the generation of a graphical read out to for the
use to be able to see what it is they are doing.
'''
# Now I will add all the non-bearing seat data points together to form
# ... single, monolothic array: Recall that they are Px, Py, Rx, Ry, and Cx, Cy
prof = np.column_stack((Px, Py))
rim = np.column_stack((Rx, Ry))
cup = np.column_stack((Cx, Cy))
megamat = np.concatenate((prof,rim,cup),axis=0)
megamatx = np.concatenate((Px, Rx, Cx),axis=0)
megamaty = np.concatenate((Py, Ry, Cy),axis=0)

# Now, I want to calculate rim weight coeficient
# First, I need area
Bdata = np.loadtxt('BearingSeatCoords_C.txt')
bulkmat = np.concatenate((Bdata,megamat), axis=0)
Cx, Cy, RimWeightRatio = centroid(bulkmat)

# EVERYTHING AFTER THIS POINT IS JUST PLOTTING. I SHOULD REALLY MAKE THIS
# ... A FUNCTION INSTEAD.
'''
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
plt.show()
'''
# EVERYTHING AFTER THIS POINT PERTAINS TO THE RUNNING DXF FILE THAT IS GOING TO BE CREATED WITH EVERY ITERATION.
# For the Profile ---
Bmatrix = np.loadtxt('BearingSeatCoords_C.txt')
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

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
from Bulkmat import Bulkmat
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
# This populates matrices for plotting
megamatx, megamaty, prof, rim, cup, bulkmat = Bulkmat(Px, Py, Rx, Ry, Cx, Cy, Bdata, Pdata, Rdata, Cdata)
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

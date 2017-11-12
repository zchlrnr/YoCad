import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.special import binom
from Bezier import Bezier
from BearingSubtract import BearingSubtract
from ProfileSubtract import ProfileSubtract
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
RunningVolume = RunningVolume - ProfileSubtract(Px, Py, RunningVolume)
print(RunningVolume)

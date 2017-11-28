import re
import sys
import numpy as np
import math
from ReadBearing import ReadBearing
from BearingSubtract import BearingSubtract
from trim import trim
from pngmaker import pngmaker
from dxfmaker import dxfmaker
from inputchecker import inputchecker

#These writes the passed in filename strings to variables
sfile = sys.argv[1]
pfile = sys.argv[2]
rfile = sys.argv[3]
cfile = sys.argv[4]

#These read the contents of the files in as numpy arrays
#This is the specifications document
Sdata = np.genfromtxt(sfile, usecols = 0, delimiter=',', dtype=float)

#This is the Bearing coordinate pairs document
Bdata = ReadBearing(Sdata)

#This is the Profile Spline Points document
Pdata = np.loadtxt(pfile, delimiter=',')

#This is the Rim Spline Points document
Rdata = np.loadtxt(rfile, delimiter=',')

#This is the Cup spline Points documen
Cdata = np.loadtxt(cfile, delimiter = ',')

#This calls a function to check for low level data input errors
#inputchecker(Sdata,Bdata,Pdata,Rdata,Cdata)
#These determine the size of the initial blank for the yoyo half
Blank_Radius = Sdata[1]/2
Blank_Length = Sdata[2]/2

#This computes the initial volume of the blank in question
Blank_Volume = ((Blank_Radius**2)*math.pi)*Blank_Length
RunningVolume = Blank_Volume

#This performs the subtractive operation to cut the desired bearing
RunningVolume = RunningVolume - BearingSubtract(Sdata)

#Calls'trim' function to 'cut away' rest of blank and leave mass accurate
#... yoyo curve shape
megamatx, megamaty, prof, rim, cup, bulkmat, halfmass = trim(RunningVolume,Sdata,Bdata,Pdata,Rdata,Cdata)

#Generates png of the final yoyo geometry and displays the control points
pngmaker(Bdata, Pdata, Rdata, Cdata, megamatx, megamaty)

#Generates DXF file of the final yoyo geometry
dxfmaker(Bdata,prof,rim,cup)

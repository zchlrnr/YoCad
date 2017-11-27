import re
import sys
import numpy as np
import math
from ReadBearing import ReadBearing
from BearingSubtract import BearingSubtract
from trim import trim
sfile = sys.argv[1]
pfile = sys.argv[2]
rfile = sys.argv[3]
cfile = sys.argv[4]
Sdata = np.genfromtxt(sfile, usecols = 0, delimiter=',', dtype=float)
Bdata = ReadBearing(Sdata)
Pdata = np.loadtxt(pfile, delimiter=',')
Rdata = np.loadtxt(rfile, delimiter=',')
Cdata = np.loadtxt(cfile, delimiter = ',')
Blank_Radius = Sdata[1]/2
Blank_Length = Sdata[2]/2
Blank_Volume = ((Blank_Radius**2)*math.pi)*Blank_Length
RunningVolume = Blank_Volume
RunningVolume = RunningVolume - BearingSubtract(3,Sdata)
#TRIM CALLS BULKMAT WHICH CREATES A PLOT!!
megamatx, megamaty, prof, rim, cup, bulkmat, halfmass = trim(RunningVolume,Sdata,Bdata,Pdata,Rdata,Cdata)

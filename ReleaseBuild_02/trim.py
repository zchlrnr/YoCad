import numpy as np
from Bezier import Bezier
from BearingSubtract import BearingSubtract
from ProfileSubtract import ProfileSubtract
from RimSubtract import RimSubtract
from CupSubtract import CupSubtract
from Bulkmat import Bulkmat
def trim(RunningVolume,Sdata,Bdata,Pdata,Rdata,Cdata):
    '''
    It is the job of the trim function to generate the unified polyline
    curves of the yoyo as well as calculate the volume of the final yoyo
    half by calling the individual, pupose built subtracting functions
    of each yoyo section
    '''
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
    megamatx, megamaty, prof, rim, cup, bulkmat = Bulkmat(Px, Py, Rx, Ry, Cx, Cy, Bdata, Pdata, Rdata, Cdata)
    return megamatx, megamaty, prof, rim, cup, bulkmat, halfmass

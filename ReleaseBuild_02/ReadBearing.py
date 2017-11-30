import numpy as np
def ReadBearing(Sdata):
    #This function will contain the file information for all the
    #... bearing types.  I will possibly hard code them in
    #... future versions of this code, in order to preven the need
    #... to be call a specific text file
    n = int(Sdata[0])
    if n == 1:
        print("Yell at Zach to write the A sized bearing thing")
    elif n==2:
        print("Yell at Zach to write the B sized bearing thing")
    elif n==3:
        Bdata = np.loadtxt('BearingSeatCoords_C.txt')
    return Bdata

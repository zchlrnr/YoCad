import numpy as np
import math
def inputchecker(Sdata,Bdata,Pdata,Rdata,Cdata):
    '''
    It is the job of this function to read the input data files and
    check to see that they aren't breaking any rules to properly
    condition the inputs for spline generation
    '''
    #First, will check to see if the linearity conditions are respected
    #This is true if the slope of the last two points of a file are the
    #... same as the slope of the first two points of another file
    #First it's Bdata to Pdata
    LB = len(Bdata)
    LP = len(Pdata)
    LR = len(Rdata)
    LC = len(Cdata)
    slope1 = (Bdata[1,LB]-Bdata[1,LB-1])/(Bdata[0,LB]-Bdata[0,LB-1])
    print(slope1)

import numpy as np
import math
def cloudify(ubermat, angsteps):
    # For 'N' points in a 2D profile with a zero component in a matrix
    #... with a zero Z-axis component
    ubermat = ubermat.tolist()
    firstpoint = ubermat[1]
    lastpoint = ubermat[len(ubermat)-1]
    cylmat = ubermat[2:len(ubermat)-1] # matrix of points in the 2d profile
    '''
    There will be three definitive phases of this code.
    1.) Generation of cylinder mesh
    2.) Generation of cone mesh 1 (bearing seat)
    3.) Generation of cone mesh 2 (cup)
    '''
    points = []
    icount = 0
    theta = 360/angsteps
    for i in cylmat:
        r = cylmat[icount][1]
        jcount = 0
        for j in range(angsteps):
            # angle will be in radians
            angle = theta*(jcount/angsteps)*(math.pi/180)
            x = cylmat[icount][0]
            y = r*np.cos(angle)
            z = r*np.sin(angle)
            points.append([x, y, z])
            jcount = jcount + 1
        icount = icount + 1
    # okay, so... now what...
    # There are stacks of points that are 'angsteps' long
    # There are len(cylmat) stacks in the list that is 'points'
    '''
    At any point n, n+angsteps is the point radially outwards from that point
    In order to create the faces matrix,
    '''

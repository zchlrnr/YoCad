import numpy as np
import math
from stl import mesh
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
            angle = 360*(jcount/angsteps)*(np.pi/180)
            x = cylmat[icount][0]
            y = r*np.cos(angle)
            print(np.cos(angle))
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
    The first face will have an edge on the lower ordinal loop
    And the second face will have an edge on the higher ordinal loop
    '''
    faces = []
    facecount = 0
    icount = 0
    for i in cylmat:
        jcount = 0
        for j in range(angsteps-1):
            x = (icount*(angsteps-1)) + jcount
            y = (icount*(angsteps-1)) + angsteps + jcount
            z = (icount*(angsteps-1)) + angsteps + jcount + 1
            faces.append([x, y, z])
            jcount = jcount + 1
        kcount = 0
        for k in range(angsteps-1):
            x = (icount*(angsteps-1)) + kcount
            y = (icount*(angsteps-1)) + angsteps + kcount + 1
            z = (icount*(angsteps-1)) + kcount + 1
            faces.append([x, y, z])
            kcount = kcount + 1
        icount = icount + 1

    points = np.array(points)
    faces = np.array(faces)
    body = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            body.vectors[i][j] = points[f[j],:]
    body.save('body.stl')

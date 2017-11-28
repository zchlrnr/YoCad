def BearingSubtract(Sdata):
    import numpy as np
    from math import pi
    from washer import washer
    if Sdata[0] == 3:
        matrix = np.loadtxt('BearingSeatCoords_C.txt')
        matrix = np.delete(matrix, (0), axis=0)
        matrix = np.array(matrix)
        vtot = 826.45
    vtot = vtot + washer(matrix[len(matrix)-1,1],Sdata[1]/2, matrix[len(matrix)-1,0])
    return vtot

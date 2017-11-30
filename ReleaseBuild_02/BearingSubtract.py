def BearingSubtract(Bdata, Sdata):
    import numpy as np
    from math import pi
    from washer import washer
    # This code returns the subtracted volume of the bearing from the
    #... volume of the original blank. 
    if Sdata[0] == 3:
        matrix = Bdata
        matrix = np.delete(matrix, (0), axis=0)
        matrix = np.array(matrix)
        vtot = 826.45
    vtot = vtot + washer(matrix[len(matrix)-1,1],Sdata[1]/2, matrix[len(matrix)-1,0])
    return vtot

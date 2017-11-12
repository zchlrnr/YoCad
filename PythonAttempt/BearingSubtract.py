def BearingSubtract(btype):
    import numpy as np
    from math import pi
    from washer import washer
    # Where btype is the integer which denotes the type of bearing
    '''
        1 == Type A
        2 == Type B
        3 == Type C
        ... etc.
    '''
    # First, bearing must be broken up into a list of cylinders from the
    # ... bearing definition file
    # !!!!!!!!!THIS IS HARD CODED FOR NOW IN AN ATTEMPT TO DEBUG THINGS!!!!
    # BLAME PAST ZACH FOR ALL SUCH CRIMES AGAINST GOOD CODE
    if btype == 3:
        matrix = np.loadtxt('BearingSeatCoords_C.txt')
        matrix = np.delete(matrix, (0), axis=0)
        matrix = np.array(matrix)
        smat = np.genfromtxt('specs.txt', usecols = 0, delimiter = ',', dtype = float)
        counter = 0
        counter = int(counter)
        vtot = 0.0
        v = 0.0
        for i in range(0,len(matrix)-1):
            xflag = 0
            yflag = 0
            a = matrix[counter,0]
            b = matrix[counter,1]
            counter = counter + 1
            c = matrix[counter,0]
            d = matrix[counter,1]
            if a == c:
                yflag = 1
                low = b
                high = d
                length = a
                v = washer(low,high,length)
            vtot = vtot + v
        #First, need to connect last point in matrix to outer Radius
        #... defined by 'specs.txt'.  Meaning --
        #... matrix[len(matrix),0] is 'length',
        #...smat[1]/2 is 'high', and
        #...matrix[len(matrix),1] is 'low'; then
        vtot = 826.45
    vtot = vtot + washer(matrix[len(matrix)-1,1],smat[1]/2, matrix[len(matrix)-1,0])
    return vtot

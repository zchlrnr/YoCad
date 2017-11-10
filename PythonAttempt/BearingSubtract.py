def BearingSubtract(btype):
    import numpy as np
    from math import pi
    import washer 
    # Where btype is the integer which denotes the type of bearing
    '''
        1 == Type A
        2 == Type B
        3 == Type C
        ... etc.
    '''
    # First, bearing must be broken up into a list of cylinders from the
    # ... bearing definition file
    if btype == 3:
        matrix = np.loadtxt('BearingSeatCoords_C.txt')
        matrix = np.delete(matrix, (0), axis=0)
        matrix = np.array(matrix)
        counter = 0
        counter = int(counter)
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
BearingSubtract(3)

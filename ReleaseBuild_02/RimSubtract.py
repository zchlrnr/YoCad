def RimSubtract(Rx, Ry):
    import numpy as np
    from washer import washer
    smat = np.genfromtxt('specs.txt', usecols = 0, delimiter = ',', dtype = float)
    v = 0.0
    for i in range(0,len(Rx)-1):
        low = (Ry[i+1] + Ry[i])/2
        high = smat[1]/2
        length = Rx[i+1] - Rx[i]
        dv = washer(low, high, length)
        v = v + dv
    vtot = v
    return vtot

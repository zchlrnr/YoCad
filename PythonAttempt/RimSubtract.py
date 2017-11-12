def RimSubtract(Rx, Ry, RunningVolume):
    import numpy as np
    from washer import washer
    smat = np.genfromtxt('specs.txt', usecols = 0, delimiter = ',', dtype = float)
    v = 0.0
    for i in range(0,len(Rx)-1):
        low = 0.0
        high = smat[2]/2
        length = Rx[i+1] - Rx[i]
        dv = washer(low, high, length)
        v = v + dv
    vtot = v
    return vtot

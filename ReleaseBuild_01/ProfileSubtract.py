def ProfileSubtract(Px, Py):
    import numpy as np
    from washer import washer
    # This will basically be a numerical integration subroutine
    # ... That calls washer.py
    # (x2-x1)*((y2+y1)/2)
    smat = np.genfromtxt('specs.txt', usecols = 0, delimiter = ',', dtype = float)
    v = 0.0
    for i in range(0,len(Px)-1):
        low = (Py[i+1] + Py[i])/2
        high = smat[1]/2
        length = Px[i+1] - Px[i]
        dv = washer(low, high, length)
        v = v + dv
    vtot = v
    return vtot

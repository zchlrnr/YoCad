def CupSubtract(Cx, Cy):
    import numpy as np
    from washer import washer
    v = 0.0
    for i in range(len(Cx)-1):
        low = 0.0
        high = (Cy[i+1] + Cy[i])/2
        length = abs(Cx[i+1] - Cx[i])
        dv = washer(low, high, length)
        v = v + dv
    vtot = v
    return vtot

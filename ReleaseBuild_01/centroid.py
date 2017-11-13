def centroid(matrix):
    import numpy as np
    def PolygonArea(corners):
        n = len(corners) # of corners
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        area = abs(area) / 2.0
        return area
    area = PolygonArea(matrix)
    l = len(matrix)
    Cx = 0.0
    Cy = 0.0
    xnums = 0.0
    ynums = 0.0
    for i in range(0,l-1):
        xi = matrix[i,0]
        yi = matrix[i,1]
        xip = matrix[i+1,0]
        yip = matrix[i+1,1]
        xadd = (xi+xip)*((xi*yip)-(xip*yi))
        yadd = (yi+yip)*((xi*yip)-(xip*yi))
        xnums = xnums + xadd
        ynums = ynums + yadd
    Cx = abs((1/(6*area))*xnums)
    Cy = abs((1/(6*area))*ynums)
    Sdata = np.genfromtxt('specs.txt', usecols = 0, delimiter=',', dtype=None)
    RimWeightRatio = Cy/(Sdata[1]/2)
    return Cx, Cy, RimWeightRatio

import numpy as np
import matplotlib.pyplot as plt
def fracturearea(floatingminthick, thick_criteria, Sdata, prof, rim, cup):
    def dist(x1,y1,x2,y2):
        d = (((y2-y1)**2)+((x2-x1)**2))**0.5
        return d
    # if a starting point endsRegular up resulting in convergent distance
    # ... then it will save said distance to a list.
    fareax = []
    fareay = []
    goflag = 0
    noflag = 0
    for i in range(0,len(prof)):
        once=0
        for j in range(0,len(cup)):
            x1 = prof[i,0]
            y1 = prof[i,1]
            x2 = cup[j,0]
            y2 = cup[j,1]
            d = dist(x1,y1,x2,y2)
            if d <= thick_criteria and once == 0:
                once = 1
                fareax = np.append(fareax, prof[i,0])
                fareay = np.append(fareay, prof[i,1])
    for i in range(0,len(cup)):
        once = 0
        for j in range(0,len(prof)):
            x1 = prof[i,0]
            y1 = prof[i,1]
            x2 = cup[j,0]
            y2 = cup[j,1]
            d = dist(x1,y1,x2,y2)
            if d <= thick_criteria:
                fareax = np.append(fareax, cup[i,0])
                fareay = np.append(fareay, cup[i,1])
    farea = np.column_stack((fareax, fareay))
    print(farea)
    return farea

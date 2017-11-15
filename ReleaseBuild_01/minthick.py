def minthick(Bdata, Sdata, prof, rim, cup):
    import numpy as np
    # This function must take each curve pattern, and calculte minimum
    # ... wall thickness IN THE OVERALL. This will be done with a
    # ... difference subfunction
    def dist(x1,y1,x2,y2):
        d = (((y2-y1)**2)+((x2-x1)**2))**0.5
        return d
    floatingminthick = Sdata[1]/2
    # Need to loop through distance from cup to bearing and profile
    # First, must censor data in bearing file in order to eliminate
    # ... degenerate intersection point
    Bdata = np.delete(Bdata, (0), axis=0)
    for i in range(0,len(Bdata)):
        # Now need to measure the distance between each point and
        # ... each point in the cup
        for j in range(0,len(cup)):
            x1 = Bdata[i,0]
            y1 = Bdata[i,1]
            x2 = cup[j,0]
            y2 = cup[j,1]
            d = dist(x1,y1,x2,y2)
            if d <= floatingminthick:
                floatingminthick = d
    for i in range(0,len(prof)):
        for j in range(0,len(cup)):
            x1 = prof[i,0]
            y1 = prof[i,1]
            x2 = cup[j,0]
            y2 = cup[j,1]
            d = dist(x1,y1,x2,y2)
            if d <= floatingminthick:
                floatingminthick = d

    return floatingminthick

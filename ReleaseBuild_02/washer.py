def washer(low,high,length):
    import numpy as np
    from math import pi
    #this code calculates the volume of a cylinder by the washer method
    v = pi*length*((high**2)-(low**2))
    return v

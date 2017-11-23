import numpy as np
def Bulkmat(Px, Py, Rx, Ry, Cx, Cy, Bdata):
    prof = np.column_stack((Px, Py))
    rim = np.column_stack((Rx, Ry))
    cup = np.column_stack((Cx, Cy))
    megamat = np.concatenate((prof,rim,cup),axis=0)
    megamatx = np.concatenate((Px, Rx, Cx),axis=0)
    megamaty = np.concatenate((Py, Ry, Cy),axis=0)
    bulkmat = np.concatenate((Bdata,megamat), axis=0)
    return megamatx, megamaty, prof, rim, cup, bulkmat

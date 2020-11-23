import numpy as np
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def juliaset_cython(double [:] x, double [:] y, double complex c, double lim, int maxit):
    cdef:
        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)
        double tmp, zr, zi, lim2 = lim*lim
        double cr = c.real, ci = c.imag
        int ite, i, j, nx=x.size, ny=y.size

    for i in range(nx):
        for j in range(ny):
            zr = x[i] 
            zi = y[j]
            ite = 0
            while (zr*zr + zi*zi) < lim2 and ite < maxit:
                zr, zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                ite += 1
            julia[j, i] = ite

    return julia
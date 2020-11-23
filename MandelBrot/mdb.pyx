from numpy import empty, zeros
cimport numpy as np

cdef int mandelbrot_escape(float complex c, int n):
    cdef float complex z
    cdef int i
    z = 0
    for i in range(n):
        z = z*z + c
        if z.real*z.real + z.imag*z.imag > 4.0:
           break
    else:
        i = 0
    return i

def generate_mandelbrot(np.ndarray[float, ndim=1] xs, np.ndarray[float, ndim=1] ys, int n):
    cdef unsigned int i,j
    cdef unsigned int N = len(xs)
    cdef unsigned int M = len(ys)
    cdef float complex z
    
    cdef np.ndarray[int, ndim=2] d = empty(dtype='i', shape=(M, N))
    for j in range(M):
        for i in range(N):
            z = xs[i] + ys[j]*1j
            d[j,i] = mandelbrot_escape(z, n)
    return d
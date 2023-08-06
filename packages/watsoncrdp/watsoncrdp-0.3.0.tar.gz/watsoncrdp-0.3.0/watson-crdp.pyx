from libc.stdlib cimport malloc, free
from libc.string cimport memset
import random

cdef extern from "math.h":
    double sqrt(double theta)

cdef _c_rdp(double *x, double *y, int n, char* mask, double epsilon, int min_points, double *distances):
    stk = [(0, n - 1)]
    cdef int st, ed, index
    cdef double dmax, p0, p1, p2,dis
    cdef int num_points = n
    cdef int j = 0
    while stk:
        st, ed = stk.pop()
        dis = sqrt((y[st]-y[ed]) * (y[st]-y[ed]) + (x[st]-x[ed]) * (x[st]-x[ed]))
        p0 = y[st] - y[ed]
        p1 = x[st] - x[ed]
        p2 = x[st] * y[ed] - y[st] * x[ed]
        dmax = 0.0
        index = st
        for i from st < i < ed:
            d = abs(p0 * x[i] - p1 * y[i] + p2) / dis
            if d > dmax:
                index = i
                dmax = d
        if dmax > epsilon:
            stk.append((index, ed))
            stk.append((st, index))
            distances[index] = dmax
            j += 1
        elif (num_points - (ed -st)) > min_points:
            for i from st < i < ed:
                if mask[i]:
                    num_points -= 1
                mask[i] = 0
               

def rdp(points, double epsilon=0, int min_points=2):
    cdef int n
    n = len(points)
    cdef double *x = <double*> malloc(n * sizeof(double))
    cdef double *y = <double*> malloc(n * sizeof(double))
    cdef double *distances = <double*> malloc(n * sizeof(double))
    cdef char *mask = <char*> malloc(n)
    memset(mask, 1, n)
    for i from 0<=i<n:
        p = points[i]
        x[i] = p[0]
        y[i] = p[1]
    _c_rdp(x, y, n, mask, epsilon, min_points, distances)
    res = []
    d = []
    for i from 0<=i<n:
        if mask[i]:
            res.append(points[i])
        d.append(distances[i])
    free(x)
    free(y)
    return res, d
# to be filled with pytest's tests..

import numpy as np


def diamond(point0, point1, point2):
    '''diamond helper sdf function'''
    x, y, z = 2*np.pi*point0, 2*np.pi*point1, 2*np.pi*point2
    sin_x, sin_y, sin_z = np.sin(x), np.sin(y), np.sin(z)
    cos_x, cos_y, cos_z = np.cos(x), np.cos(y), np.cos(z)

    return sin_x*sin_y*sin_z+  sin_x*cos_y*cos_z+ cos_x*sin_y*cos_z+ cos_x*cos_y*sin_z

def func(i,j, k, func):
    return func(np.array([i,j,k]))

def filter():
    # ar = np.empty((1000,1000))
    # z= 1
    # return np.fromfunction(lambda i, j, k: func(i,j,k, diamond), (5760, 5760, 1), dtype=int)
    ys, xs = np.mgrid[0:5760:5760j, 0:3600:3600j]
    # density = np.sin(ys)-np.cos(xs)
    print(xs.shape)
    return diamond(xs, ys, 1).shape



print(filter())
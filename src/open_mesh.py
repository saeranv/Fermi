#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import pygmsh
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import math

from pprint import pprint
pp = pprint



def test():
    # disable all logging calls from pygmsh
    sys.stdout = open(os.devnull, 'w')

    # Characteristic length
    lcar = 0.25#1e-1

    # Coordinates of lower-left and upper-right vertices of a square domain
    xmin = 0.0
    xmax = 5.0
    ymin = 0.0
    ymax = 5.0

    # Vertices of a square hole
    squareHoleCoordinates = np.array([
        [2, 2, 0],
        [3, 2, 0],
        [3, 3, 0],
        [2, 3, 0]
        ])

    # Create geometric object
    geom = pygmsh.built_in.Geometry()

    # Create square hole
    squareHole = geom.add_polygon(
        squareHoleCoordinates, lcar,
        make_surface=False
        )

    # Create square domain with square hole
    geom.add_rectangle(
        xmin, xmax, ymin, ymax, 0.0, lcar,
        holes=[squareHole.line_loop]
        )

    points, cells, point_data, cell_data, field_data = pygmsh.generate_mesh(geom)

    sys.stdout = sys.__stdout__
    """
    print 'points'
    print points
    print 'cells'
    print cells
    print 'point data'
    print point_data
    print 'field_data'
    print field_data
    #"""

    return points, cells

def view_mesh(ptvec):

    ig = plt.figure()
    ax = plt.gca(projection="3d")
    ax.set_aspect("equal")
    ax.autoscale(enable=False, axis='both')

    # Get x,y,z coordinates as np arrays
    x = np.array([ptvec[i][0] for i in xrange(len(ptvec))])
    y = np.array([ptvec[i][1] for i in xrange(len(ptvec))])
    z = np.ones(len(ptvec))
    #print x

    # revise as parallel
    fscale = lambda x: x/5.
    x = [fscale(x_) for x_ in x]
    y = [fscale(y_) for y_ in y]

    f = lambda s,t: (s/t)*360.0*(math.pi/180.0)
    max_x = np.amax(x)
    min_x = np.amin(x)
    total_x = abs(max_x - min_x)

    max_y = np.amax(y)
    min_y = np.amin(y)
    total_y = abs(max_y - min_y)

    for i in xrange(len(ptvec)):
        stepx = float(abs(x[i]-min_x))
        xtheta = f(stepx,total_x)

        stepy = float(abs(y[i]-min_y))
        ytheta = f(stepy,total_y)

        z[i] = (math.sin(ytheta) + math.cos(xtheta)) * 0.125 + 0.5

    makeline = lambda x,y,z: ax.plot3D((x[i],x[i+1]), (y[i],y[i+1]), (z[i],z[i+1]), color="r")
    #[makeline(x,y,z) for i in xrange(len(ptvec)-1)]
    zz = np.ones(len(ptvec))
    ax.scatter3D(x, y, zz, c=z,cmap='viridis')


def plot():

    plt.show()

if __name__ == '__main__':

    pts, clls = test()
    view_mesh(pts)

    if len(sys.argv) > 1 and sys.argv[1] == "p":
        plot()

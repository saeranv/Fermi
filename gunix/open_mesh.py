#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import pygmsh
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

def test():
    # Characteristic length
    lcar = 1#e-1

    # Coordinates of lower-left and upper-right vertices of a square domain
    xmin = 0.0
    xmax = 5.0
    ymin = 0.0
    ymax = 5.0

    # Vertices of a square hole
    squareHoleCoordinates = np.array([
        [0,0,0],
        [5,0,0],
        [5,5,0],
        [0,5,0],
        ])
        #[1, 1, 0],
        #[4, 1, 0],
        #[4, 4, 0],
        #[1, 4, 0]
        #])

    # Create geometric object
    geom = pygmsh.built_in.Geometry()

    # Create square hole
    squareHole = geom.add_polygon(
        squareHoleCoordinates, lcar,
        make_surface=False
        )

    # Create square domain with square hole
    #geom.add_rectangle(
    #    xmin, xmax, ymin, ymax, 0.0, lcar,
    #    holes=[squareHole.line_loop]
    #    )

    points, cells, point_data, cell_data, field_data = pygmsh.generate_mesh(geom)

    #print 'points'
    #print points
    """
    print 'cells'
    print cells
    print 'point data'
    print point_data
    print 'field_data'
    print field_data
    """
    # TODO support for volumes of triangle6
    # ref = 16.0
    # from helpers import compute_volume
    # assert abs(compute_volume(points, cells) - ref) < 1.0e-2 * ref

    return points, cells

def view_mesh(ptvec):

    ig = plt.figure()
    ax = plt.axes(projection="3d")

    # Get x,y,z coordinates as np arrays
    x = np.array([ptvec[i][0] for i in xrange(len(ptvec))])
    y = np.array([ptvec[i][1] for i in xrange(len(ptvec))])

    ##f = lambda x,y: np.sqrt(x**2 + y**2)
    xx,yy = np.meshgrid(x,y)
    #z = f(xx,yy)
    #z = np.array([ptvec[i][2] for i in xrange(len(ptvec))])
    zz = np.zeros((len(ptvec), len(ptvec)))

    # This can be done in parallel
    ln = float(len(ptvec))
    r = 1.0
    f = lambda x: (x/(ln-1))*(360/r)*(math.pi/180.0)
    for i in xrange(len(ptvec)):
        theta = f(i)
        print i, theta
        zx = math.cos(theta)
        for j in xrange(len(ptvec)):
            theta = f(j)
            zy = 0#math.sin(theta)
            zz[i,j] = (zx)#*zy)
    #plt.plot(xx, yy, zz, marker='.', color='k', linestyle='none')
    ax.scatter3D(xx, yy, zz) #c=zpt, cmap="Reds")
    #ax.plot_surface(xx,yy, rstride=1, cstride=1, cmap="viridis", edgecolor="none")

    plt.show()


if __name__ == '__main__':
    import meshio
    meshio.write('hole_in_square.vtu', *test())
    pts, clls = test()
    view_mesh(pts)

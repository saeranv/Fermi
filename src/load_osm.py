from __future__ import print_function
from loadenv import *
import os
import sys
import pprint

"""
installation instructions:
pip install pythonnet
# https://github.com/NREL/OpenStudio/releases?after=v1.13.2

"""

pp = pprint.pprint

RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "src", "trnco_fe"))
OSM_TEST = os.path.join(RESOURCE_DIR,"in.osm")

import openstudio_python as ospy

def get_points(surface_vector):

    srf_mtx = np.array([None]*len(surface_vector))

    # Make nested list of openstudio Point3d objects
    for i in xrange(len(surface_vector)):
        vnum = surface_vector[i].vertices().Count
        vlst = [None]*vnum
        for j in xrange(vnum):
            vlst[j] = surface_vector[i].vertices()[j]
        srf_mtx[i] = vlst
    #vertice_matrix = np.asmatrix(vertice_matrix)

    return srf_mtx

def get_surface(osm,ops):


    outside_surface_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()=="Outdoors",
            osm.getSurfaces()))

    inside_surface_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()!="Outdoors",
            osm.getSurfaces()))

    out_pts = get_points(outside_surface_vector)
    ins_pts = get_points(inside_surface_vector)



if __name__ == "__main__":

    print("argv", sys.argv)

    if len(sys.argv) > 1:
        fpathosm = sys.argv[1]
        osm,ops = ospy.load_osm(fpathosm)
    else:
        print("loading example osm from Fermi/trnco_fe")
        osm, ops = ospy.load_osm(OSM_TEST)
        print("osm model is 'osm' and OpenStudio lib is 'ops'")
        get_surface(osm, ops)

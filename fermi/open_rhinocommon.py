#from __future__ import print_function
import os
import sys
import clr

import pprint

import numpy as np
import pandas as pd


import openstudio_python

clr.AddReference("System")
import System
pp = lambda p: pprint.pprint(p)

BIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "bin"))

if BIN_DIR not in sys.path:
    sys.path.append(BIN_DIR)

rhinocommon_dll = os.path.join(BIN_DIR,"Rhino3dmIO.dll")
clr.AddReference("Rhino3dmIO")
#clr.AddReferenceToFileAndPath("Rhino3dmIO)

import Rhino as rc

def osm_points_from_outdoor_boundary():

    osm_file_path = "C:\\ladybug\\hb_office\\OpenStudio\\hb_office.osm"
    osm = openstudio_python.load_osm(osm_file_path)

    surface_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()=="Outdoors",
            osm.getSurfaces()))

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


def rhino_mesh(srf_mtx):

    # Cast to rhino points
    for i in xrange(len(srf_mtx)):
        for j in xrange(len(srf_mtx[i])):
            v = srf_mtx[i][j]
            srf_mtx[i][j] = rc.Geometry.Point3d(v.x(),v.y(),v.z())

    # Make into curves

    for i in xrange(len(srf_mtx)):
        point_array = System.Array.CreateInstance(rc.Geometry.Point3d, len(srf_mtx[i]))
        for j in xrange(len(srf_mtx[i])):
            point_array[j] = srf_mtx[i][j]
        srf_mtx[i] = rc.Geometry.Curve.CreateControlPointCurve(point_array,1)

    #public static Mesh CreateFromPlanarBoundary(
	#Curve boundary,
	#MeshingParameters parameters,
	#double tolerance

    #jagged_and_faster = MeshingParameters.Coarse;
    #smooth_and_slower = MeshingParameters.Smooth;
    #default_mesh_params = MeshingParameters.Default;
    #minimal = MeshingParameters.Minimal;

    if True:#for i in xrange(len(srf_mtx)):
        msh_param = rc.Geometry.MeshingParameters.Coarse
        #print rc.Geometry.Mesh.CreateFromPlanarBoundary#(srf_mtx[i], msh_param)
        pp(dir(rc.Geometry.Mesh))
        #print msh_face
    return srf_mtx

if __name__ == "__main__":

    vertex_matrix = osm_points_from_outdoor_boundary()
    out = rhino_mesh(vertex_matrix)

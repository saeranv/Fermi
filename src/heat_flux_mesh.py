import os
import sys

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import openstudio_python

import pprint
pp = lambda p: pprint.pprint(p)

def plot_flux():

    osm_file_path = "C:\\ladybug\\hb_office\\OpenStudio\\hb_office.osm"
    osm = openstudio_python.load_osm(osm_file_path)


    surf_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()=="Outdoors",
            osm.getSurfaces()))

    L = map(lambda s:s.vertices(),surf_vector)

    L = pd.Series(L)
    print L
    """
    for i in xrange(len(surf_vector)):
        pt_vector = surf_vector[i].vertices()
        surf_vector[i]
        for i in xrange(pt_vector.Count):
            print pt_vector[i].x(), pt
    """

if __name__ == "__main__":
    out = plot_flux()

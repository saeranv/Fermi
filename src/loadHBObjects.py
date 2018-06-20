#
# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
#
# This file is part of Honeybee.
#
# Copyright (c) 2013-2018, Mostapha Sadeghipour Roudsari <mostapha@ladybug.tools>
# Honeybee is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 3 of the License,
# or (at your option) any later version.
#
# Honeybee is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
#
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Load Honeybee Objects

Use this component to load Honeybee objects from a file on your system.
The valid files are created by dump Honeybee objects component.
-
Provided by Honeybee 0.0.63

    Args:
        _HBObjects: A list of Honeybee objects
        _filePath: A valid path to a file on your drive (e.g. c:\ladybug\20ZonesExample.HB)
        _load: Set to True to load the objects from the file
    Returns:
        readMe!: ...
"""

import pickle
#import scriptcontext as sc
#import Grasshopper.Kernel as gh
import os
import uuid
import sys
#from Rhino.Geometry import *
#import Rhino as rc

#from __future__ import print_function

#import clr

import pprint

#import numpy as np
#import pandas as pd
#import openstudio_python
"""
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
"""
CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))

# Set the uwg path
#UWG_DIR = os.path.join(CURR_DIRECTORY, "..", "honeybee")
#if "UWG" not in sys.modules:
#    sys.path.insert(0, UWG_DIR)
#try:
#    __import__("UWG")
#except ImportError as e:
#    raise ImportError("Failed to import UWG: {}".format(e))

#import UWG


def loadHBObjects(HBData):
    print(HBData)
    """
    hb_EPZone = sc.sticky["honeybee_EPZone"]
    hb_EPSrf = sc.sticky["honeybee_EPSurface"]
    hb_EPZoneSurface = sc.sticky["honeybee_EPZoneSurface"]
    hb_EPSHDSurface = sc.sticky["honeybee_EPShdSurface"]
    hb_EPFenSurface = sc.sticky["honeybee_EPFenSurface"]
    hb_hive = sc.sticky["honeybee_Hive"]()

    # a global dictonary to collect data
    ids = HBData["ids"]
    objs = HBData["objs"]
    HBObjects = {}

    def loadHBZone(HBZoneData):
        # programs is set to default but will be overwritten
        HBZone = hb_EPZone(HBZoneData['geometry'],
                           HBZoneData['num'], HBZoneData['name'],
                           ('Office', 'OpenOffice'), HBZoneData['isConditioned'])

        # update fields in HBZone
        for key, value in HBZoneData.iteritems():
            HBZone.__dict__[key] = value

        HBObjects[HBZone.ID] = HBZone

    def loadHBSurface(HBSurfaceData):
        # EPFenSurface
        if HBSurfaceData['type'] == 5:
            HBBaseSurface = HBObjects[HBSurfaceData['parent']]
            HBSurface = hb_EPFenSurface(HBSurfaceData['geometry'],
                                        HBSurfaceData['num'], HBSurfaceData['name'], HBBaseSurface, 5)

        elif HBSurfaceData['type'] == 6:
            HBSurface = hb_EPSHDSurface(HBSurfaceData['geometry'],
                                        HBSurfaceData['num'], HBSurfaceData['name'])
        else:
            HBSurface = hb_EPZoneSurface(HBSurfaceData['geometry'],
                                         HBSurfaceData['num'], HBSurfaceData['name'])

        for key, value in HBSurfaceData.iteritems():
            HBSurface.__dict__[key] = value

        HBObjects[HBSurface.ID] = HBSurface

    def updateHoneybeeObjects():
        for id, HBObject in HBObjects.iteritems():
            if HBObject.objectType == 'HBZone':
                HBObject.surfaces = [HBObjects[id] for id in HBObject.surfaces]
                HBObject.HVACSystem = HBObjects[HBObject.HVACSystem]
                continue

            # replace parent ID with the object
            if HBObject.parent != None:
                # replace parent object with ID
                HBObject.parent = HBObjects[HBObject.parent]

            if not HBObject.isChild and HBObject.hasChild:
                HBObject.childSrfs = [HBObjects[id] for id in HBObject.childSrfs]
                HBObject.calculatePunchedSurface()

            if HBObject.type == 6:
                HBObject.childSrfs = [HBObjects[id] for id in HBObject.childSrfs]

            if HBObject.type != 6 and HBObject.BCObject.lower() == "outdoors":
                HBObject.BCObject = outdoorBCObject()

            if HBObject.type != 6 and HBObject.BC.lower() == "surface":
                # replace parent object with ID
                HBObject.BCObject = HBObjects[HBObject.BCObject]

    for id, HBO in objs.iteritems():
        if HBO['objectType'] == 'HBSurface' and HBO['type'] == 5:
            continue
        if HBO['objectType'] == 'HBSurface' and HBO['type'] != 5:
            loadHBSurface(HBO)
        elif HBO['objectType'] == 'HBZone':
            loadHBZone(HBO)

    # create Fenestration surfaces
    for id, HBO in objs.iteritems():
        if HBO['objectType'] == 'HBSurface' and HBO['type'] == 5:
            loadHBSurface(HBO)

    # replace ids with objects in surfaces
    updateHoneybeeObjects()

    # return new Honeybee objects
    # try:
    #    return hb_hive.addToHoneybeeHive([HBObjects[id] for id in HBData["ids"]], ghenv.Component)
    # except:
    #    return hb_hive.addNonGeoObjToHive([HBObjects[id] for id in HBData["ids"]][0], ghenv.Component)
    """

if __name__ == "__main__":
        #if len(sys.argv) > 1:
        filePath = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\bin\\hb_dump_1.HB" # sys.argv[1]

        if not os.path.isfile(filePath):
            raise ValueError("Can't find {}".format(filePath))

        with open(filePath, "rb") as inf:
            HBObjects = loadHBObjects(pickle.load(inf, encoding='latin1'))

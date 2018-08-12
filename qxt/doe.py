from __future__ import print_function
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pprint


pp = pprint.pprint

CURR_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

# Set the uwg path
UWG_DIR = os.path.join(CURR_DIRECTORY,"..","..","urbanWeatherGen")

if "UWG" not in sys.modules:
    sys.path.insert(0, UWG_DIR)

try:
    __import__("UWG")
except ImportError as e:
    raise ImportError("Failed to import: {}".format(e))

#from UWG import UWG
from UWG.readDOE import readDOE


    # DOE Building Types
BLDTYPE = [
    'FullServiceRestaurant',    # 1
    'Hospital',                 # 2
    'LargeHotel',               # 3
    'LargeOffice',              # 4
    'MedOffice',                # 5
    'MidRiseApartment',         # 6
    'OutPatient',               # 7
    'PrimarySchool',            # 8
    'QuickServiceRestaurant',   # 9
    'SecondarySchool',          # 10
    'SmallHotel',               # 11
    'SmallOffice',              # 12
    'StandAloneRetail',         # 13
    'StripMall',                # 14
    'SuperMarket',              # 15
    'WareHouse']                # 16

BUILTERA = [
    'Pre80',                    # 1
    'Pst80',                    # 2
    'New'                       # 3
    ]

ZONETYPE = [
    '1A (Miami)',               # 1
    '2A (Houston)',             # 2
    '2B (Phoenix)',             # 3
    '3A (Atlanta)',             # 4
    '3B-CA (Los Angeles)',      # 5
    '3B (Las Vegas)',           # 6
    '3C (San Francisco)',       # 7
    '4A (Baltimore)',           # 8
    '4B (Albuquerque)',         # 9
    '4C (Seattle)',             # 10
    '5A (Chicago)',             # 11
    '5B (Boulder)',             # 12
    '6A (Minneapolis)',         # 13
    '6B (Helena)',              # 14
    '7 (Duluth)',               # 15
    '8 (Fairbanks)'             # 16
    ]

if __name__ == "__main__":
    # no serializeation
    bld, bem, sched = readDOE(False)

    doedoc = ""

    padding = lambda x: "----" if x==0 else "-"*abs(int(math.log10(x))-4)
    doedoc += "BLDTYPE\n"
    for i in xrange(16): indexdocstr += "{0}{1}{2}".format(i, padding(i) , BLDTYPE[i]+"\n")
    doedoc += "BUILTERA\n"
    for i in xrange(3): indexdocstr += "{0}{1}{2}".format(i, padding(i) , BUILTERA[i]+"\n")
    doedoc += "ZONETYPE\n"
    for i in xrange(16): indexdocstr += "{0}{1}{2}".format(i, padding(i) , ZONETYPE[i]+"\n")

    print("Created bld, bem, sched => 3d matrices of building, BEMdef, and Schedule objects.\ndoedoc => Matrix index table.")

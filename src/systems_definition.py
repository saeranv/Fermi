from __future__ import print_function
import sys
import os

import math
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

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
    raise ImportError("Failed to import UWG: {}".format(e))

import UWG

# Script

# areas
total_area = 15009.0
# office st
office_area = 3383.0
office_support = 776.0
colab_space = 442.0

# lab st
lab_area = 4797.0
lab_support = 1353.0
acf = 1496.0

# support st
bld_support = 2762.0

#pd.DataFrame = ()

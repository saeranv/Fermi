from __future__ import print_function
import sys
import os

import math
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('dark_background')

import pprint
pp = pprint.pprint

CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))

"""
# Set the uwg path
uwg_DIR = os.path.join(CURR_DIRECTORY,"..","urbanWeatherGen")
if "uwg" not in sys.modules:
    sys.path.insert(0, uwg_DIR)
try:
    __import__("uwg")
except ImportError as e:
    raise ImportError("Failed to import uwg: {}".format(e))

import uwg
"""
x_example = np.arange(math.pi*2*10)
y_example = [math.sin(x_) for x_ in x_example]
print("\nplt.plot(x_example, y_example)")

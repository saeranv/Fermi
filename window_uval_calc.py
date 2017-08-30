#uval_calcs

"""
%matplotlib inline
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from IPython.display import clear_output
from mpl_toolkits.mplot3d import Axes3D
import math
"""


# -------------------------------------------------------------------------
# DOE REFERENCE WINDOW
# Pre-1980s Construction, Houston, Commercial
# -------------------------------------------------------------------------
U_DOE = 5.84    # Window Assembly U Factor [W m-2 K-1]
SHGC = 0.54     # Window Assembly Solar Heat Gain Factor [-]

# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Steel Frame
# -------------------------------------------------------------------------
k_steel = 2.5   # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 0.4
A_window = 0.5
A_steel = A_window - A_glass
WK_window = U_DOE * A_window # W K-1

# Derive conductance of glass
WK_frame = k_steel * A_steel
WK_glass = WK_window - WK_frame
k_glass = WK_glass / A_glass
U_steel_window = U_DOE

# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Wood Frame
# -------------------------------------------------------------------------
k_wood = 1.0                    # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 0.3
A_window = 0.6
A_wood = A_glass - A_window

# Derive window U value
U_wood_window = k_glass * A_glass + k_wood * A_wood

print U_wood_window
print U_steel_window

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

# Material,
#     Std Wood 6inch,          !- Name
#     MediumSmooth,            !- Roughness
#     0.15,                    !- Thickness {m}
#     0.12,                    !- Conductivity {W/m-K}
#     540.0000,                !- Density {kg/m3}
#     1210,                    !- Specific Heat {J/kg-K}
#     0.9000000,               !- Thermal Absorptance
#     0.7000000,               !- Solar Absorptance
#     0.7000000;               !- Visible Absorptance! Common Materials




# Q?? Should we be multiplying by thermal/solar absorptances??

# -------------------------------------------------------------------------
# DOE REFERENCE WINDOW
# Pre-1980s Construction, Houston, Commercial
# -------------------------------------------------------------------------
U_DOE = 5.84    # Window Assembly U Factor [W m-2 K-1]
U_steel_window = U_DOE

# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Steel Frame
# -------------------------------------------------------------------------
k_steel_ = 10.1073                    # 2.18-1.78 [btu h-1 ft-2 -F] non-thermally broken aluminum
k_steel = k_steel_                    # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 1.3414
A_window = 1.9718
A_steel = A_window - A_glass

WK_window = U_DOE * A_window # W K-1

# Derive conductance of glass
WK_frame = k_steel * A_steel
print 'framewk', WK_frame
print 'winwk', WK_window
print 'area frame', A_steel
print 'area window', A_window
print 'k_wood', k_steel
print 'u window', U_DOE
print '--'

WK_glass = WK_window - WK_frame
k_glass = WK_glass / A_glass

# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Wood Frame
# -------------------------------------------------------------------------
frame_depth = 0.10
k_wood = 0.12*0.8/frame_depth        # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 2.3405
A_window = 4.3530
A_wood = A_window - A_glass

# Derive window U value
U_wood_window = (k_glass * A_glass + k_wood * A_wood) / (A_wood + A_glass)

print U_steel_window # 5.84
print U_wood_window # 2.5056

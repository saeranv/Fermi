#uval_calcs
"""
Objective:

Input: ref U value,  ref frame conductance, ref area of window, ref area of glass
Output: glass conductivity

Input: glass conductance, frame conductance, area of window, area of glass
Output: window U value

Purpose:
FX: glass_conductivity_from_frame_and_window(U_window_,C_frame_,A_window_,A_frame_)
Calculates the conductivity of the glazing via referenced material
conductivities, areas, and DOE reference U-values for window assemblies.

FX: u_value_from_area_and_conductance(C_frame_,C_glass_,A_frame_,A_glass_)
Calculates U-value of window assembly from conductance and areas of
glass and frame.

Limitations:
    - conductance differences between edge of glass vs Center of glass
    - Absorptance value is approximate
    - film coefficient not used for frames
"""

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

def glass_conductivity_from_frame_and_window(U_window_,C_frame_,A_window_,A_frame_):
    A_glass_ = A_window_ - A_frame_
    WK_window_ = U_window_ * A_window_  # W K-1

    # Derive conductance of glass
    WK_frame_ = C_frame_ * A_frame_
    WK_glass_ = WK_window_ - WK_frame_
    C_glass_ = WK_glass_ / A_glass_
    return C_glass_

def u_value_from_area_and_conductance(C_frame_,C_glass_,A_frame_,A_glass_):
    # Derive window U value
    U_window_ = (C_glass_ * A_glass_ + C_frame_ * A_frame_) / (A_frame_ + A_glass_)
    return U_window_


# -------------------------------------------------------------------------
# REFERENCES
# -------------------------------------------------------------------------

U_DOE = 5.84                            # Window Assembly U Factor [W m-2 K-1], pre-1980s Construction, Houston, Commercial

# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Steel Frame
# -------------------------------------------------------------------------
U_steel_window = U_DOE
C_steel = 10.1073                       # 2.18-1.78 [btu h-1 ft-2 -F] non-thermally broken aluminum
                                        # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 1.3414
A_window = 1.9718

C_glass = glass_conductivity_from_frame_and_window(U_steel_window,C_steel,A_window,A_window - A_glass)


# -------------------------------------------------------------------------
# LOVETT HALL WINDOW
# Wood Frame
# -------------------------------------------------------------------------
wood_absorptivity = 0.8
frame_depth = 0.10
C_wood = 0.12*wood_absorptivity/frame_depth        # Conductance [W m-2 K-1] from Engineering Toolbox Reference
A_glass = 2.3405
A_window = 4.3530

U_wood_window = u_value_from_area_and_conductance(C_wood,C_glass,A_window - A_glass,A_glass)

print U_steel_window # 5.84
print U_wood_window # 2.5056


# References:
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

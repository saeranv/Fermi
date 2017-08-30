#uval_calcs
%matplotlib inline
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from IPython.display import clear_output
from mpl_toolkits.mplot3d import Axes3D

import math

#Define graph constants
plt.xlabel('X')
plt.ylabel('Y')
plt.title("X vs Y")
plt.grid()


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
k_frame = 2.5   # [W m-2 K-1] from Engineering Toolbox Reference
A_frame = 10.0  # [m2] from CAD


#def calculate_k_from_U(U_base_):
U_partial_component_ = A_partial_component_ * k_partial_component_
U_base

x = np.arange(-50,50,1)

#natural decay y=e-kt
y1 = map(lambda x_: math.pow(math.e,x_*-1), x)
plt.plot(x,y1,'k')
#natural growth y=ekt
y2 = map(lambda x_: math.pow(math.e,x_), x)
plt.plot(x,y2,'k:')
#plot graphics
plt.axis([-5,20,0,10])
plt.show()

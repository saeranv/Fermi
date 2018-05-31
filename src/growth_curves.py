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
character description
'-'       solid line style
'--'      dashed line style
'-.'      dash-dot line style
':'       dotted line style
'.'       point marker
','       pixel marker
'o'       circle marker
'v'       triangle_down marker
'^'       triangle_up marker
'<'       triangle_left marker
'>'       triangle_right marker
'1'       tri_down marker
'2'       tri_up marker
'3'       tri_left marker
'4'       tri_right marker
's'       square marker
'p'       pentagon marker
'*'       star marker
'h'       hexagon1 marker
'H'       hexagon2 marker
'+'       plus marker
'x'       x marker
'D'       diamond marker
'd'       thin_diamond marker
'|'       vline marker
'_'       hline marker

"""

# Ref: http://www2.phy.ilstu.edu/~wenning/slh/Common%20Graph%20Forms.pdf

#Define graph constants
plt.xlabel('X')
plt.ylabel('Y')
plt.title("X vs Y")
plt.grid()


# -------------------------------------------------------------------------
# Exponential Relationship: change the 2^x
# -------------------------------------------------------------------------

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


# -------------------------------------------------------------------------
# Power law Relationship: change the x^2
# -------------------------------------------------------------------------

x = np.arange(0,50,1)
#up opening parabola
y1 = map(lambda x_: math.pow(x_,2), x)
plt.plot(x,y1,'k')
#side opening parabola
y2 = map(lambda x_: math.pow(x_,0.5), x)
plt.plot(x,y2,'k:')

#plot graphics
plt.axis([-5,20,0,10])
plt.show()

# -------------------------------------------------------------------------
# Natural log Relationship:
# -------------------------------------------------------------------------

x = np.arange(1,50,1)
#natural log
y1 = map(lambda x_: math.log(x_), x)
plt.plot(x,y1,'k')

#plot graphics
plt.axis([-5,20,0,10])
plt.show()

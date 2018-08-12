#%matplotlib inline
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#from IPython.display import clear_output
from mpl_toolkits.mplot3d import Axes3D

import math

# -------------------------------------------------------------------------
# 3D plotting
# -------------------------------------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-5.0, 5.0, 0.05)
X, Y = np.meshgrid(x, y)
L = []
for x_,y_ in  zip(np.ravel(X), np.ravel(Y)):
    z_ = math.sin(x_) + math.sin(y_)
    L.append(z_)
#print L
zs = np.array(L)

Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

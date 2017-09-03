""" Fermi Plots!

Args:
    fx:    # list of function arguments
    x1:    # start domain
    x2:    # end domain
    y1:    # start range
    y2:    # end range

Returns:
    A matplotlib.pyplot

How to add this to systems path
import sys
sys.path.append("..")

"""

import matplotlib.pyplot as plt
import numpy as np
import math
import fermiplot

color_lst = ['b','g','r','c','m','y','k','w']
style_lst = [
'-','--','-.',':','.',',',
'o','v','^','<','>','1','2',
'3','4','s','p','*','h','H',
'+','x','D','d','|','_'
]

x1,x2,y1,y2 = 0,30,0,30
x_lst = np.arange(x1,x2,0.1)
fxlstlen = len(x_lst)
k_lst = np.arange(0,1,1/float(fxlstlen))

fx_lst = [None] * fxlstlen
for ki in xrange(fxlstlen):
    k = k_lst[ki]
    #print k
    fx_lst[ki] = lambda proxy: math.pow(math.e,k*proxy)

#for i in fx_lst:
#    print i
#x_lst = np.arange(x1,x2,(x2-x1)/float(len(fx_lst)))
for i in xrange(len(fx_lst)):
    fx = fx_lst[i]
    ylst = map(lambda x: fx(x), x_lst)
    lin = color_lst[i%len(color_lst)]
    plt.plot(x_lst,ylst,lin)
    #print 'fx {}'.format(i)
    #xy_matrix(xlst,ylst)

plt.axis([x1,x2,y1,y2])
plt.grid()
plt.show()

#fx_lst = [fx_1,fx_2]
#plot(fx_lst,x1,x2,y1,y2)

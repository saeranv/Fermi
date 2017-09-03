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



linestyle = [
'-',      # solid line style
'--',     # dashed line style
'-.',     # dash-dot line style
':',      # dotted line style
'.',      # point marker
',',      # pixel marker
'o',      # circle marker
'v',      # triangle_down marker
'^',      # triangle_up marker
'<',      # triangle_left marker
'>',      # triangle_right marker
'1',      # tri_down marker
'2',      # tri_up marker
'3',      # tri_left marker
'4',      # tri_right marker
's',      # square marker
'p',      # pentagon marker
'*',      # star marker
'h',      # hexagon1 marker
'H',      # hexagon2 marker
'+',      # plus marker
'x',      # x marker
'D',      # diamond marker
'd',      # thin_diamond marker
'|',      # vline marker
'_'       # hline marker
]


def xy_matrix(xlst_,ylst_):
    matrix = [xlst_,ylst_]
    transposed_matrix = zip(*matrix) # transpose matrix
    #for xy in transposed_matrix:
    #    print xy
    #print '--0.5'

def plot(fxlst,x1=-10,x2=10,y1=-5,y2=10.0):
    xlst = np.arange(x1,x2+1,1)
    if type(fxlst) != type([]):
        fxlst = [fxlst]

    # define the axis
    x_axis_lst = map(lambda x: 0, xlst)
    plt.plot(xlst,x_axis_lst,'r-')
    plt.plot([0]*len(xlst),xlst,'r-')

    for i in xrange(len(fxlst)):
        fx = fxlst[i]
        ylst = map(lambda x: fx(x), xlst)
        plt.plot(xlst,ylst,'k'+linestyle[i])
        print 'fx {}'.format(i)
        xy_matrix(xlst,ylst)

    plt.axis([x1,x2,y1,y2])
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print 'Remember: if use log make sure to change x constraints'
    fx_1 = lambda x: math.pow(math.e,0.5*x)
    fx_2 = lambda x: math.pow(math.e,0.25*x)
    fx_lst = [fx_1,fx_2]
    plot(fx_lst,x1=0,x2=20,y2=50)

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


color_lst = ['b','g','r','c','m','y','k','w']
style_lst = [
'-','--','-.',':','.',',',
'o','v','^','<','>','1','2',
'3','4','s','p','*','h','H',
'+','x','D','d','|','_'
]


def xy_matrix(xlst_,ylst_):
    matrix = [xlst_,ylst_]
    transposed_matrix = zip(*matrix) # transpose matrix
    #for xy in transposed_matrix:
    #    print xy
    #print '--0.5'

def plot(fx_lst_,x1=-10,x2=10,y1=-5,y2=10.0):
    xlst = np.arange(x1,x2+1,1)
    if type(fx_lst_) != type([]):
        fx_lst_ = [fx_lst_]

    # define the axis
    x_axis_lst = map(lambda x: 0, xlst)
    plt.plot(xlst,x_axis_lst,'r-')
    plt.plot([0]*len(xlst),xlst,'r-')

    for i in xrange(len(fx_lst_)):
        fx = fx_lst_[i]
        ylst = map(lambda xin_: fx(xin_), xlst)
        plt.plot(xlst,ylst,'k'+style_lst[i%len(style_lst)])
        #print 'fx {}'.format(i)
        #xy_matrix(xlst,ylst)

    plt.axis([x1,x2,y1,y2])
    plt.grid()
    plt.show()

if __name__ == "__main__":
    fx_lst = []
    for k in range(2,4,1):
        print 1/float(k)
        func = lambda x_: math.pow(math.e, 1/float(k) * x_)
        fx_lst.append(func)
    #fx_lst = [lambda x: math.pow(math.e, frac * x) for x in range(100)]
    #for i in fx_lst:
    #    for j in range(10):
    #        print i(j)
    #    print 'end'
    fx_1 = lambda x: math.pow(math.e,0.5*x)
    fx_2 = lambda x: math.pow(math.e,0.33*x)
    fx_lst += [fx_1,fx_2]
    plot(fx_lst,0,10,0,20)

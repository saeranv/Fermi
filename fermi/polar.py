import math
import numpy as np
import matplotlib.pyplot as plt
import sys

def cheat():
    """ numpy cheat """
    vec = np.array([1.,2.,3.])
    mat = np.array([[1.,2.,3.],[4.,5.,6.]])
    vec2 = np.arange(3)
    mat2 = np.arange(12).reshape(4,3)
    pdb.set_trace()
    # We can perform vectorized functions on this!
    vec *= 2
    #print vec
    vecdot = vec.dot(vec2)
    #print vecdot

def rsq_deep():
    # https://stackoverflow.com/questions/4788892/draw-square-with-polar-coordinates
    ce = 360
    st = 5
    rad = []
    c = 0
    for phi in np.arange(0,ce,st):
        #print c
        #c+=1
        #print  "deg ", phi, (phi+45)%90-45, "cos ", math.cos(phi)
        phi_ = ((phi+45)%90-45)/180.*math.pi
        #phi_ = phi*180.*math.pi
        r = 5./math.cos(phi_)
        rad.append(r)

    theta = np.arange(0,ce/st)

    for inc in xrange(3):
        inc = inc
        x = map(lambda t: math.cos(t*st*math.pi/180.)*(rad[t] - (5.+rad[t])), theta)
        y = map(lambda t: math.sin(t*st*math.pi/180.)*(rad[t] - (5.+rad[t])), theta)

        plt.plot(x,y,'r')


def plot():
    plt.plot(np.arange(-20,21,1), [0]*41,'b') # x axis
    plt.plot([0]*41,np.arange(-20,21,1),'b')

    plt.grid()
    plt.axis([-20,20,-20,20])
    plt.show()

if __name__ == "__main__":
    rsq_deep()

    # ctrl w to close plot window
    if len(sys.argv)> 1 and sys.argv[1]=="p":
        plot()

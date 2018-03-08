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
    rsq = [1]*((ce)/st)
    for phi in np.arange(0,ce,st):
        phi_ = ((phi+45)%90-45)/180.0*math.pi
        radius = 1./math.cos(phi_)
        rsq[int(phi/st)] = radius
        phi = phi/180.*math.pi
        print  "phi: ", phi*180./math.pi
        print "sqphi: ", (phi*180./math.pi+45)%90-45
        print 'rad ', radius
        if not (abs(phi%90)<1e-10):
            print "xof phi: ", round(math.cos(phi),2), " * ", round(1/math.cos(phi),2),\
                " = ", math.cos(phi)#(1./math.cos(phi))
        else:
            print "xof phi: zero div error"
        print "xof sqphi: ", round(math.cos(phi),2), " * ", round(1/math.cos(phi_),2),\
            " = ", math.cos(phi)*(1./math.cos(phi_))
        print "yof sqphi: ", round(math.sin(phi),2), " * ", round(1/math.cos(phi_),2),\
            " = ", math.sin(phi)*(1./math.cos(phi_))


        print '---------------------'

    theta = np.arange(0,ce/st)

    x = map(lambda t: math.cos(t*st*math.pi/180.)*rsq[t]*10, theta)
    y = map(lambda t: math.sin(t*st*math.pi/180.)*rsq[t]*10, theta)
    plt.plot(x,y,'r')


def main():
    """
    Use polar coordinates to draw a square
    """
    r = 10
    theta = np.arange(0,361,1)
    x = map(lambda t: math.cos(t*math.pi/180.)*r, theta)
    y = map(lambda t: math.sin(t*math.pi/180.)*r, theta)
    plt.plot(x,y,'r')

    rsq = lambda t:10./math.cos(((t+45)%90-45)/180.*math.pi)

    x = map(lambda t: math.cos(t*math.pi/180.)*rsq(t), theta)
    y = map(lambda t: math.sin(t*math.pi/180.)*rsq(t), theta)
    plt.plot(x,y,'r')

def plot():
    plt.plot(np.arange(-20,21,1), [0]*41,'b') # x axis
    plt.plot([0]*41,np.arange(-20,21,1),'b')

    plt.grid()
    plt.axis([-20,20,-20,20])
    plt.show()

if __name__ == "__main__":
    #main()
    rsq_deep()

    # ctrl w to close plot window
    if len(sys.argv)> 1 and sys.argv[1]=="p":
        plot()

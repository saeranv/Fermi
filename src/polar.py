import math
import numpy as np
import matplotlib.pyplot as plt
import sys

"""
function getLengthForDeg(phi){
    phi = ((phi+45)%90-45)/180*Math.PI;
    return 1/Math.cos(phi);
"""
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

def circle_to_square():
    """ https://stackoverflow.com/questions/4788892/draw-square-with-polar-coordinates """
    st = 60
    ce = 360 + st
    rad = []
    c = 0
    sqlen = 10
    for phi in np.arange(0,ce,st):
        #print  "deg ", phi, (phi+45)%90-45, "cos ", math.cos(phi)
        phi_ = ((phi*45.0) % 90.0-45.0) * (math.pi/180.0)
        #phi_ = phi*180.*math.pi
        r = sqlen/math.cos(phi_)
        rad.append(r)

    theta = np.arange(0,ce/st)


    x = [1]*len(theta)
    y = [1]*len(theta)

    for t in xrange(len(theta)):
        delta = (rad[t] - sqlen)
        r = rad[t] - delta*1/5.
        x[t] = math.cos(t*st*math.pi/180.)*r
        y[t] = math.sin(t*st*math.pi/180.)*r
    plt.plot(x,y,'r')

def circle_to_square_iterative():
    """ https://stackoverflow.com/questions/4788892/draw-square-with-polar-coordinates """
    st = 5
    ce = 360 + st
    rad = []
    c = 0
    sqlen = 10
    for phi in np.arange(0,ce,st):
        #print  "deg ", phi, (phi+45)%90-45, "cos ", math.cos(phi)
        phi_ = ((phi*45) % 90-45) * (math.pi/180.0)
        # phi_ = phi*180.*math.pi
        r = sqlen/math.cos(phi_)
        rad.append(r)

    theta = np.arange(0,ce/st)

    max_inc = 7
    for inc in xrange(max_inc):
        inc = inc
        x = [1]*len(theta)
        y = [1]*len(theta)
        for t in xrange(len(theta)):
            delta = (rad[t] - sqlen)
            r = rad[t] - delta*inc/(max_inc-1)
            x[t] = math.cos(t*st*math.pi/180.)*r
            y[t] = math.sin(t*st*math.pi/180.)*r
        plt.plot(x,y,'r')


def plot():
    plt.plot(np.arange(-20,21,1), [0]*41,'b') # x axis
    plt.plot([0]*41,np.arange(-20,21,1),'b')

    plt.grid()
    plt.axis([-20,20,-20,20])
    plt.show()

def circle_to_square_dot():
    """
    Better method since it's clearer how we use the
    projection formula to derive the polar coordinates
    :return:
    """
    theta = range(90)
    radius = 10.0
    xlst = []
    ylst = []
    ref_vec = np.array([0,1])

    for deg in theta:
        x = math.cos(deg * math.pi/180.0) * radius
        y = math.sin(deg * math.pi/180.0) * radius
        vec = np.array([x,y])
        unit_vec = vec/np.linalg.norm(vec)
        proj_vec = np.dot(unit_vec, ref_vec) * ref_vec * radius
        proj_vec = proj_vec + np.array([radius,0])
        xlst.append(proj_vec[0])
        ylst.append(proj_vec[1])
    print(ref_vec)
    plt.plot(xlst, ylst,'r')

if __name__ == "__main__":
    #circle_to_square_iterative()
    #circle_to_square()
    circle_to_square_dot()

    # ctrl w to close plot window
    if len(sys.argv)> 1 and sys.argv[1]=="p":
        plot()

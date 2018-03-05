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
    for phi in np.arange(0,361,5):
        print phi, (phi+45)%90-45
        phi_ = ((phi+45)%90-45)/180.*math.pi
        radius = 10./math.cos(phi_)
        #plt.plot(np.arange(
        #plt.plot(

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

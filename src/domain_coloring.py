import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import hsv_to_rgb

# https://github.com/hernanat/dcolor

def plot():
    plt.grid()
    plt.axis([-2,2,-2,2])
    plt.show()

def z(x, y):
    """
    return complex number x+iy
    If inputs are arrays, then it returns an array
    with corresponding x_j+iy_j values
    """
    return x + 1j * y

def make_domain():
    """Create the domains for Real (x) and Imaginary (y) values respectively"""
    samples = 10
    xdomain = 1
    yrange = 1
    x = np.linspace(-xdomain,xdomain, samples)
    y = np.linspace(-yrange,yrange,samples)
    xx, yy=np.meshgrid(x,y)
    return xx,yy

def main():
    xx,yy = make_domain()
    zz = z(xx,yy)

    H = np.angle(zz) # get angle from complex value
    S = np.abs(zz)/1.0
    V = np.abs(zz)/1.0 # get distance

    rgb = hsv_to_rgb(np.dstack((H,S,V)))

    #plt.scatter(xx,yy)
    fig = plt.figure(figsize=(2, 2), dpi=100)
    plt.imshow(rgb)


main()
plot()
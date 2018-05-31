from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sys
from pprint import pprint
pp = pprint

def main():
    """
    Testing methods to view mesh or surfaces in matplotlib
    """
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    """
    #Lines
    zline = np.linspace(0,15,1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    # Points
    zpt = 15 * np.random.random(100)
    xpt = np.sin(zpt) + 0.1 * np.random.randn(100)
    ypt = np.cos(zpt) + 0.1 * np.random.randn(100)
    ax.scatter3D(xpt, ypt, zpt) #c=zpt, cmap="Reds")
    """

    f = lambda x,y: np.sin(np.sqrt(x**2 + y**2))
    x = np.linspace(-10,10,50)
    y = np.linspace(-10,10,50)
    xx,yy = np.meshgrid(x,y)
    z = f(xx,yy)

    #pp(x)
    #pp(xx)
    pp(z)

    ax.plot_surface(xx,yy,z, rstride=1, cstride=1, cmap="viridis", edgecolor="none")
    ax.set_title("surface")

    # Rotate view by:
    # - elevation: 60 degrees aboce x,y plane
    # - azimuth: 35 counter clockwise from z-axis
    ax.view_init(60,35)

def plot():
    plt.show()

if __name__ == "__main__":
    main()

    if len(sys.argv) > 1 and sys.argv[1] == "p":
        plot()

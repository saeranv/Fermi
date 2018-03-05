import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Use polar coordinates to draw a square
    """
    x = np.array(xrange(10))
    y = np.array(xrange(10))

    plt.plot(x,y,'r')

def plot():
    plt.plot(xrange(-20,21,1), [0]*41,'b') # x axis
    plt.plot([0]*41,xrange(-20,21,1),'b')

    plt.grid()
    plt.axis([-20,20,-20,20])
    plt.show()

if __name__ == "__main__":
    main()
    plot()
    # ctrl w to close plot window

import math
import numpy as np
import matplotlib as plt

def main():
    """
    Use polar coordinates to draw a square
    """
    x = np.array(xrange(10))
    y = np.array(xrange(10))

    plt.plot(x,y,'r')

    plt.axis([-5,20,0,10])
    plt.show()

if __name__ == "__main__":
    main()

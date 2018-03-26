import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
    #sin
    theta = np.arange(0,359)
    tinit = 2 # C
    p = 20 # period

    Tout = map(lambda x: math.sin(x*math.pi/180.),theta)
    Tf = lambda P,t: P * math.pow(math.e, -0.01*t)

    Tdecay = []
    Tx = []
    for i in xrange(360):
        if i%p==0:
            Tdecay.append(Tf(Tout[i],i))
            Tx.append(i)

    #print pd.Series(Tout)
    #print pd.Series(Tdecay)



    plt.plot(Tx, Tdecay , 'k')
    plt.plot(theta,Tout,'r')


    # ctrl w to close plot window
    if len(sys.argv)> 1 and sys.argv[1]=="p":
        plot(0,360,-2,2,p)

def plot(minx,maxx,miny,maxy,period):

    plt.plot(np.arange(minx,maxx,1), [0]*(maxx-minx),'b') # x axis
    for n in xrange((maxx-minx)/period):
        plt.plot([n*period]*(maxy-miny+1), np.arange(miny,maxy+1,1),'b:') # y axis

    plt.grid()
    plt.axis([minx,maxx,miny,maxy])
    plt.show()

if __name__ == "__main__":
    main()

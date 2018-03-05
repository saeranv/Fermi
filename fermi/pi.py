%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import math

# find pi = 2*pi*r / 2*r # perimeter:diameter ratio
# r = sqrt(x2 + y2) # distance between n-dim pts

r = 50.
p = .01

xlst = np.arange(-r,r+p,p)

ylst1 = map(lambda x: math.pow(abs(r*r - x*x),.5), xlst)
ylst2 = map(lambda x: -1*math.pow(abs(r*r - x*x),.5), xlst)

plt.plot(xlst,ylst1,'k')
plt.plot(xlst,ylst2,'k')

# get the integral
d = 0
for i in xrange(len(xlst)-1):
    x_ = xlst[i+1] - xlst[i]
    y_ = ylst1[i+1]  - ylst1[i]
    d += math.pow(x_*x_ + y_*y_,.5)

print 'perimter actual: ', 2 * math.pi * r
print 'perimter calc: ', d*2
print 'pi?', d/r

#plot graphics
plt.axis([-2*r,2*r,-2*r,2*r])
plt.show()

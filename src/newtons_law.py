import fermiplot
import math

"""Newton's Law of Cooling
Represents a boiling cup of water cooling to room T

Ta = 25 C
Ti @ 0m is 100 C
Ti @ 30m is 50 C

    dy/dt = ky
    y = Ti - Ta
so...
    Ti = y + Ta
    dT/dt = dy/dt = dTa
          = dy/dt
    dT/dt = dy/dt

now let's solve:

    ky = Ti - Ta
and...
    ky = C * e^kt
so...
    C * e^kt = Ti - Ta
    Ti = C * e^kt - Ta
    log((Ti-Ta)/C) = log(e^kt)
sub in values from measured decay
    k = -0.0462
Therefore:
    Ti = 100 * e^(-0.0462 * t)

"""


fx1 = lambda x: 25 + (100 * math.pow(math.e, x* -0.0462)) # Ti
fx2 = lambda x: 25 # room ambient Ta

fermiplot.plot([fx1,fx2],0,100,0,100)

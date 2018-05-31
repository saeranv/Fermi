%matplotlib inline
from matplotlib.pyplot import *
import numpy as np
import math

# -------------------------------------------------------------------------
# Logistic growth
# -------------------------------------------------------------------------

alpha = 0.2
r = 1.0

def fx(u,t):
    return alpha * u *(1 - u/r)

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*fx(u[k], t[k])
    return u, t

u,t = ForwardEuler(r, 0.1, 40, 400)

plot(t,u)
show()

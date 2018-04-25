import numpy as np
import pandas as pd
import bash_epw
import math

import matplotlib.pyplot as plt
import matplotlib


#Define graph constants
plt.xlabel('X')
plt.ylabel('Y')
plt.title("X vs Y")
plt.grid()
plt.axis([0,8760,0,40])

def main():
    bash_epw.set_uwg()
    uwg = bash_epw.main()
    epw = uwg.weather
    pp = bash_epw.pp

    #doc = epw.__doc__

    turbine_ht = 60.0   # m
    turbine_swept_area = 7.5  # m2
    turbine_dir = 3*math.pi/2. # West in radians
    z0r = 0.25
    von_karman = 0.4
    zero_plane = 0.05#0.75*16.
    air_density = 1.225     #kg/m3
    wind_prof = uwg.RSM.windProf

    v_z = lambda v_epw: v_epw * math.ln((turbine_ht-zero_plane)/z0)/von_karman

    u_spd = np.array(epw.staUmod) # m/s
    u_dir = np.array(map(lambda d: d*math.pi/180., epw.staUdir)) # deg to radians

    P = np.zeros(8760)
    E = np.zeros(8760)
    V = np.zeros(8760)

    h = 1 # infinitisemal timestep
    #print wind_prof
    # Forward Euler method to calculate wind differential
    # https://www.engineeringtoolbox.com/wind-power-d_1214.html
    for t in xrange(8760-1):
        #v_z = (u_spd[t + 1]/von_karman)  * math.log((turbine_ht-zero_plane)/z0r)       # logarthmic wind profile
        v_z = u_spd[t + 1] * ((math.log(turbine_ht/0.5)) / (math.log(10.0/0.5))) # from LB

        v_z = v_z * math.sin(u_dir[t + 1])   # account for direction of wind
        v_z = 0.0 if v_z > 0.0 else abs(v_z) # if posivitve then coming from East side

        #print v_z, (u_dir[t+1]-math.pi)*180./math.pi, epw.staUdir[t+1]

        P[t+1] = (0.5 * v_z**3 * air_density * turbine_swept_area) * 0.4 / 1000.0 # Power (kW) at time step t
        E[t+1] = E[t] + h * P[t] # kWh
        V[t+1] = u_spd[t+1] * math.sin(u_dir[t + 1])#v_z
        #print P[t+1], E[t+1], round(v_z,2)#, epw.staUmod[t+1]

    print E[-1]

    E = map(lambda x: x/1000.0, E)
    plt.plot(range(8760),E)
    plt.plot(range(8760),P,'r')
    plt.plot(range(8760),V,'k')
    plt.show()

    return epw

if __name__ == "__main__":
    epw = main()

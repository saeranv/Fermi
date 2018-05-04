import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pprint
pp = pprint.pprint

CURR_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

# Set the uwg path
UWG_DIR = os.path.join(CURR_DIRECTORY,"..","..","urbanWeatherGen")
if "UWG" not in sys.modules:
    sys.path.insert(0, UWG_DIR)
try:
    __import__("UWG")
except ImportError as e:
    raise ImportError("Failed to import UWG: {}".format(e))

import UWG

class EPW(object):
    """
    https://bigladdersoftware.com/epx/docs/8-3/auxiliary-programs/energyplus-weather-file-epw-data-dictionary.html
    http://bigladdersoftware.com/epx/docs/8-2/auxiliary-programs/epw-csv-format-inout.html

    properties
        location  # location name
        staTemp   % air temperature (C)
        staRhum   % air relative humidity (%)
        staPres   % air pressure (Pa)
        staInfra  % horizontal Infrared Radiation Intensity (W m-2)
        staHor    % horizontal radiation\n
        staDir    % normal solar direct radiation (W m-2)
        staDif    % horizontal solar diffuse radiation (W m-2)
        staUdir   % wind direction ()
        staUmod   % wind speed (m s-1)
        staRobs   % Precipitation (mm h-1)
        staHum    % specific humidty (kg kg-1)
    """

    def __init__(self,epw_file="CAN_ON_Toronto.716240_CWEC.epw", uwg_param_file="initialize.uwg", epw_dir=None,uwg_param_dir=CURR_DIRECTORY):
        self.epw_dir = epw_dir if epw_dir!=None else os.path.join(CURR_DIRECTORY, "..", "resources", "epw")
        self.epw_file = epw_file
        self.uwg_param_dir = uwg_param_dir
        self.uwg_param_file = uwg_param_file

        self.mth_str = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.mth_day = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.mth_hr = [0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016]

    def read_epw(self):
        # Initialize the UWG object
        self.uwg = UWG.UWG(self.epw_dir, self.epw_file, self.uwg_param_dir, self.uwg_param_file)
        self.uwg.read_epw()
        self.uwg.read_input()

        return self.uwg

    def run_uwg(self):
        self.uwg.hvac_autosize()
        self.uwg.simulate()
        self.uwg.write_epw()

        # check this later
        self.epw_file = self.epw_file.strip(".epw") + "_UWG.epw"
        self.read_epw()

        return self.uwg

    def tofile(self,epw_vec,filename="rawepwcalc.txt"):
        #epw_method = list of values, should make this into a pandas matrix

        f = open(filename, "w")

        map(lambda v:
            f.write(str(epw_val) +"\n"),
                epw_vec)

        f.close()

    def ppmtx(self,ymtx,f=lambda x: round(x,2)):
        """ pretty print matrix """
        return map(lambda v: map(lambda v_: f(v_), v), ymtx)

    def epw_mtx(self,epw_vector):

        # Create a monthly matrix for numpy by preallocate array and assign
        # array of hours in month
        # N.B. could be changed to sparse matrix for extra boost, or ndarray
        self.ymtx = [[0]*(self.mth_day[i]*24) for i in xrange(12)]

        # Add data
        yhr = 0
        for i in xrange(12):
            for j in xrange(self.mth_day[i]*24):
                self.ymtx[i][yhr - self.mth_hr[i]] = epw_vector[yhr]
                yhr += 1

        # Graveyard of abandoned ways to do this...
        #ydf = pd.DataFrame(np.zeros((1,12)),columns=mth_str)
        #ydf.loc[mth_str[i],:] = pd.Series(np.ones(mth_day[i]))

        return self.ymtx

    def epw_heatmap(self):
        # https://matplotlib.org/users/pyplot_tutorial.html
        ymtx_dbt = self.epw_mtx(self.uwg.weather.staTemp)

        yvec = reduce(lambda a,b: a+b, ymtx_dbt)

        z = np.array([[0.0]*24 for i in xrange(365)])

        i = 0
        for ix in xrange(365):
            for iy in xrange(24):
                z[ix,iy] = yvec[i]
                i += 1

        z = z.transpose()
        plt.imshow(z,origin="lower",interpolation=None,aspect="auto")

        #plt.title("test")
        #plt.ylabel("y")
        #plt.xlabel("x")

        plt.show()

        # )


if __name__ == "__main__":

    #Inputs
    epw_file = "USA_PA_Philadelphia.Intl.AP.724080_TMY3.epw"
    uwg_param_file = "initialize_PHILA.uwg"
    add_micro_climate = False
    # Run
    w = EPW(epw_file,uwg_param_file)
    uwg = w.read_epw()
    # Expose some parameters
    w.uwg.Month = 1
    w.uwg.Day = 1
    w.uwg.nDay = 365
    w.uwg.set_input()

    if add_micro_climate:
        uwg = run_uwg()

    epw = w.uwg.weather
    doc = epw.__doc__

    # make heatmap
    #epw_mtx = w.epw_mtx(epw.staTemp)
    w.epw_heatmap()

from __future__ import print_function
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pprint
pp = pprint.pprint

CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))
print(CURR_DIRECTORY)
# Set the uwg path
UWG_DIR = os.path.join(CURR_DIRECTORY,"..","urbanWeatherGen")
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
        staTdp    % dry bulb
        staRhum   % air relative humidity (%)
        staPres   % air pressure (Pa)
        staInfra  % horizontal Infrared Radiation Intensity (W m-2)
        staHor    % horizontal radiation
        staDir    % normal solar direct radiation (W m-2)
        staDif    % horizontal solar diffuse radiation (W m-2)
        staUdir   % wind direction ()
        staUmod   % wind speed (m s-1)
        staRobs   % Precipitation (mm h-1)
        staHum    % specific humidty (kg kg-1)
    """

    def __init__(self,epw_file="CAN_ON_Toronto.716240_CWEC.epw", uwg_param_file="initialize.uwg", epw_dir=None,uwg_param_dir=CURR_DIRECTORY):
        self.epw_dir = epw_dir if epw_dir!=None else os.path.join(CURR_DIRECTORY, "..", "urbanWeatherGen", "resources", "epw")
        self.epw_file = epw_file
        self.uwg_param_dir = uwg_param_dir
        self.uwg_param_file = uwg_param_file

        self.mth_str = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.mth_day = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.mth_hr = [0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016]

    def read_epw(self):
        # Initialize the UWG object
        self.uwg = UWG.UWG(self.epw_file, self.uwg_param_file, self.epw_dir, self.uwg_param_dir)
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

        # It'd be good to turn this into a dataframe
        #self.mth_str = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        #ydf = pd.DataFrame()
        #ydf["test"] = range(10)
        #ydf["test2"] = range(11)

        return self.ymtx

    def epw_heatmap(self):
        # https://matplotlib.org/users/pyplot_tutorial.html
        #ymtx_dbt = self.epw_mtx(self.uwg.weather.staTemp)
        #yvec = reduce(lambda a,b: a+b, ymtx_dbt)

        f = lambda x: x-273.15

        yvec = map(f, self.uwg.weather.staTemp)
        #yvec = self.uwg.weather.staTdp

        z = np.array([[0.0]*24 for i in xrange(365)])

        i = 0
        for ix in xrange(365):
            for iy in xrange(24):
                z[ix,iy] = yvec[i]
                i += 1

        z = z.transpose()

        im = plt.imshow(z,origin="lower",interpolation=None,aspect="auto")
        ax = plt.gca();

        # Labels for major ticks
        #ax.set_xticklabels(np.arange(1, 6, 1))
        #ax.set_yticklabels(np.arange(1, 12, 1))
        # Minor ticks
        ax.set_xticks(np.arange(0, 365, 1), minor=True)
        ax.set_yticks(np.arange(0, 24, 1), minor=True)

        #ax.grid(which='major', color='w', linestyle='-', linewidth=1)
        ax.grid(which='minor', color='w', linestyle='-', linewidth=0.4)

        #plt.title("test")
        #plt.ylabel("y")
        #plt.xlabel("x")

        plt.show()

        # )



if __name__ == "__main__":

    #Inputs
    epw_file = "USA_PA_Philadelphia.Intl.AP.724080_TMY3.epw"
    epw_dir_in = os.path.join(CURR_DIRECTORY,"resources","epw")
    uwg_param_file = "initialize.uwg"
    uwg_param_dir_in = os.path.join(CURR_DIRECTORY,"src")
    add_micro_climate = False

    # Run
    w = EPW(epw_file,uwg_param_file,epw_dir=epw_dir_in, uwg_param_dir = uwg_param_dir_in)
    uwg = w.read_epw()
    # Expose some parameters
    w.uwg.Month = 1
    w.uwg.Day = 1
    w.uwg.nDay = 365

    w.uwg.read_epw()
    w.uwg.set_input()
    w.uwg.init_BEM_obj()
    w.uwg.init_input_obj()

    if add_micro_climate:
        uwg = run_uwg()

    # make heatmap
    #epw_mtx = w.epw_mtx(epw.staTemp)
    # w.epw_heatmap()

    doc_1 = "{}\n".format(
        "\nw: wrapper class obj\nepw: Weather object\ndoc: docstrings for epw."
        )
    doc_2 = "{}\n".format(
        "\nTo nest by month:\n\tyrmtx = w.epw_mtx(epw.staTemp)"
        "\nTo make dataframe:"
        "\n\tdbT = pd.DataFrame({'temp': epw.staTemp}) # dry bulb"
        "\n\tdnr = pd.DataFrame({'temp': epw.staDir})  # direct normal radiation"
        )
    doc_3 = "{}".format(
        "\nTo export to excel:"
        "\n\t>>> writer = pd.ExcelWriter('epw_analysis.xlsx')"
        "\n\t>>> dbT.to_excel(writer,'Sheet1')"
        "\n\t>>> dnr.to_excel(writer,'Sheet2')"
        "\n\t>>> writer.save()"
        )

    doc_4 = "{}".format(
        "\nGet max all year in dataframe:\n\tdfmax = pd.DataFrame({'tempmax': [max(month) for month in w.epw_mtx(epw.staTemp)]})"
    )

    doc_5 = "{}".format(
        "\nTo load in qtconsole:\n\t>>ipython qtconsole\n\t>>%load src/epw.py"
    )

    epw = w.uwg.weather
    epwdoc = epw.__doc__ + doc_1 + doc_2 + doc_3 + doc_4

    print(epwdoc)

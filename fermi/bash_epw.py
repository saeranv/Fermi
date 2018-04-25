import math
import numpy as np
import pandas as pd
import sys
import os
import pprint

pp = lambda x: pprint.pprint(x)

"""
Weather
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

def set_uwg():
    uwg_dir = "C:\\Users\\631\\Documents\\GitHub\\urbanWeatherGen"

    if "UWG" not in sys.modules:
        sys.path.insert(0, uwg_dir)
    try:
        __import__("UWG")
    except ImportError as e:
        raise ImportError('Failed to import {}:\n\t{}'.format(lib, e))

    return 1

def main():

    import UWG

    CURR_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
    #epw_directory = "P:\\890 UTM New Science Building\\2. Design\\2.5 Research\\2.5.1 RED Report\\Macro_Climate_Break_Out\\CAN_ON_Toronto.716240_CWEC\\"
    epw_directory = os.path.join(CURR_DIRECTORY, "..", "resources", "epw")
    epw_filename = "CAN_ON_Toronto.716240_CWEC.epw"      # EPW file name
    uwg_param_directory = CURR_DIRECTORY                # .uwg file directory
    uwg_param_filename = "initialize.uwg"               # .uwg file name
    
    # Initialize the UWG object
    uwg = UWG.UWG(epw_directory, epw_filename, uwg_param_directory, uwg_param_filename)
    uwg.read_epw()
    uwg.read_input()
    uwg.set_input()
    #
    #uwg.hvac_autosize()
    #uwg.simulate()

    return uwg


#def todewpoint(uwg):
#return map(lambda tdb,w,p: uwg.psychrometrics(tdb,w,p), uwg.epw.staTemp, uwg.epw.staRhum, uwg.epw.sta)



def tofile(epw_vec,filename="rawepwcalc.txt"):
    #epw_method = list of values, should make this into a pandas matrix

    f = open(filename, "w")

    map(lambda v:
        f.write(str(epw_val) +"\n"),
            epw_vec)

    f.close()

if __name__ == "__main__":
    set_uwg()
    uwg = main()
    epw = uwg.weather
    doc = epw.__doc__

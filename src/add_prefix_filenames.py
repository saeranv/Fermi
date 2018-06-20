from __future__ import print_function
import sys
import os

import math
#import pandas as pd
#import numpy as np

#import matplotlib.pyplot as plt

import pprint
pp = pprint.pprint


if __name__ == "__main__":
    img_dir = "P:\\890 UTM New Science Building\\2. Design\\2.5 Research\\2.5.6 Simulation\\Sensitivity_Analysis_Workflow\\160617Colibri"
    data_csv_path = os.path.join(img_dir,"data.csv")

    lstdir = os.listdir(img_dir)

    pp(lstdir)
    """
    # open data csv
    file_ = open(data_csv_path,"r")
    gen_ = csv_reader(file_, delimiter=",")
    L = map(lambda r: r,gen_)
    file_.close()

    print(L)
    """

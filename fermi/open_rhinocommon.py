import os
import sys
import clr

import pprint

pp = lambda p: pprint.pprint(p)

BIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "bin"))

def load_rhinocommon():

    if BIN_DIR not in sys.path:
        sys.path.append(BIN_DIR)

    rhinocommon_dll = os.path.join(BIN_DIR,"Rhino3dmIO.dll")
    clr.AddReference("Rhino3dmIO")
    #clr.AddReferenceToFileAndPath("Rhino3dmIO)

    import Rhino as rc


    pt = rc.Geometry.Point3d(1.,1.,1.)
    print pt

    #pp(dir(rc.Geometry.Point3d))
    return 1

if __name__ == "__main__":

    out = load_rhinocommon()

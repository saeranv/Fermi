from __future__ import print_function
import os
import sys


RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "resources"))
OSM_TEST = os.path.join(RESOURCE_DIR,"Office.osm")

def load_osm(osm_file_path):

    openstudio_dir_1_12 = "C:\\Program Files\\OpenStudio 1.12.0\\CSharp\\openstudio"
    openstudio_dir_1_10 = "C:\\Program Files\\OpenStudio 1.10.0\\CSharp\\openstudio"
    #openstudio_dir_1_10 = "C:\\openstudio-2.4.0\\CSharp\\openstudio"



    if os.path.exists(openstudio_dir_1_12):
        openstudio_dir = openstudio_dir_1_12
    elif os.path.exists(openstudio_dir_1_10):
        print("using openstudio 1.10")
        openstudio_dir = openstudio_dir_1_10
    else:
        print("No openstudio installation exists.")

    if openstudio_dir not in sys.path:
        sys.path.append(openstudio_dir)

    # Make sure to add openstudio dir to path before importing clr
    import clr
    clr.AddReference("OpenStudio")
    

    import OpenStudio as ops

    if not os.path.exists(osm_file_path):
        print("error at ", osm_file_path)
        return 0

    osm_path = ops.Path(osm_file_path)

    osm = ops.Model.load(osm_path).get()

    return osm

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        fpathosm = sys.argv[1]
        osm = load_osm(fpathosm)
    else:
        print("loading example osm from resources")
        osm = load_osm(OSM_TEST)
        thisvar = "kar"
        #print("need to add a fpath to osm file.")
        print(osm)
    print("hello")

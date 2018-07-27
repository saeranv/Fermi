from __future__ import print_function
import os
import sys
import pprint

pp = pprint.pprint

RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "src", "trnco_fe"))
OSM_TEST = os.path.join(RESOURCE_DIR,"in.osm")

def load_osm(osm_file_path):

    #PINVOKE ERROR
    #openstudio_dir = r"C:\Program Files\OpenStudio 1.10.0\CSharp\openstudio"
    #openstudio_dir = r"C:\openstudio-2.4.0\CSharp\openstudio"

    # WORKING
    #openstudio_dir = r"C:\openstudio-2.5.0\CSharp\openstudio" # @kt
    openstudio_dir = r"C:\Program Files\OpenStudio 1.12.0\CSharp\openstudio" # @home

    #print(openstudio_dir)
    #print(openstudio_dir_1_12)
    """
    if os.path.exists(openstudio_dir_1_12):
        print("using openstudio 1.12")
        openstudio_dir = openstudio_dir_1_12
    elif os.path.exists(openstudio_dir_1_10):
        print("using openstudio 1.10")
        openstudio_dir = openstudio_dir_1_10
    else:
        print("No openstudio installation exists.")
    """
    if openstudio_dir not in sys.path:
        sys.path.insert(0,openstudio_dir)

    # Make sure to add openstudio dir to path before importing clr
    import clr
    clr.AddReference("OpenStudio")


    import OpenStudio as ops

    if not os.path.exists(osm_file_path):
        print("error at ", osm_file_path)
        return 0,ops

    osm_path = ops.Path(osm_file_path)

    osm = ops.Model.load(osm_path).get()

    # sql file
    #sqlfile = os.path.join(RESOURCE_DIR, "office\\ModelToIdf\\in.sql")
    #sqlfileops = ops.SqlFile(ops.Path(sqlfile))
    #sqlfileops.setSqlFile()

    return osm,ops

if __name__ == "__main__":

    print("argv", sys.argv)

    if len(sys.argv) > 1:
        fpathosm = sys.argv[1]
        osm,ops = load_osm(fpathosm)
    else:
        print("loading example osm from Fermi/trnco_fe")
        osm,ops = load_osm(OSM_TEST)
        thisvar = "kar"
        #print("need to add a fpath to osm file.")
        print("osm model is 'osm' and OpenStudio lib is 'ops'")

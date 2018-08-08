from __future__ import print_function
import os
import sys
import pprint

pp = pprint.pprint

RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname("__file__"), "src", "trnco_fe"))
OSM_TEST = os.path.join(RESOURCE_DIR,"in.osm")



def load_ops_helper(openstudio_dir):

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

    if not os.path.exists(OSM_TEST):
        print("error at ", OSM_TEST)

    osm_path_test = ops.Path(OSM_TEST) # will fail if ops not loaded correctly

    return ops

def load_ops():

    #PINVOKE ERROR
    #openstudio_dir = r"C:\Program Files\OpenStudio 1.10.0\CSharp\openstudio"
    #openstudio_dir = r"C:\openstudio-2.4.0\CSharp\openstudio"
    # WORKING
    openstudio_dir_2_5 = r"C:\openstudio-2.5.0\CSharp\openstudio" # @kt
    openstudio_dir_1_12 = r"C:\Program Files\OpenStudio 1.12.0\CSharp\openstudio" # @home

    try:
        ops = load_ops_helper(openstudio_dir_2_5)
    except:
        ops = load_ops_helper(openstudio_dir_1_12)

    return ops

def load_osm(osm_file_path, ops):

    ops_file_path = ops.Path(osm_file_path)

    osm = ops.Model.load(ops_file_path).get()

    # sql file
    #sqlfile = os.path.join(RESOURCE_DIR, "office\\ModelToIdf\\in.sql")
    #sqlfileops = ops.SqlFile(ops.Path(sqlfile))
    #sqlfileops.setSqlFile()

    return osm

def save_osm(new_file_path, osm, ops):
    
    osm.save(ops.Path(new_file_path), True))

if __name__ == "__main__":

    print("use load_osm.py to load openstudio files.")

import os
import sys


RESOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "resources"))
RESOURCE_OSM = os.path.join(RESOURCE_DIR, "Office.osm")

def load_osm(osm_file_path=0):

    openstudio_dir = "C:\\Program Files\\OpenStudio 1.12.0\\CSharp\\openstudio"

    if openstudio_dir not in sys.path:
        sys.path.append(openstudio_dir)

    # Make sure to add openstudio dir to path before importing clr
    import clr
    clr.AddReference("OpenStudio")
    import OpenStudio as ops


    if not osm_file_path:
        osm_file_path = RESOURCE_OSM

    if not os.path.exists(osm_file_path):
        print "error at ", osm_file_path
        return 0

    osm_path = ops.Path(osm_file_path)

    osm = ops.Model.load(osm_path).get()

    return osm

if __name__ == "__main__":
    osm = load_osm()

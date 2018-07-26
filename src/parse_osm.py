from __future__ import print_function
from loadenv import *
import openstudio_python as pyops



OSM_TEST = os.path.join(RESOURCE_DIR, "in.osm")

def main():
    osm, ops = pyops.load_osm(OSM_TEST)


if __name__ == "__main__":
    main()

from __future__ import print_function
from loadenv import *
import openstudio_python as pyops



RESOURCE_DIR = os.path.join(CURR_DIR, "src", "trnco_fe")
OSM_TEST = os.path.join(RESOURCE_DIR, "in.osm")


def main():
    osm, ops = pyops.load_osm(OSM_TEST)

    space_array = np.array(map(lambda s: s, osm.getSpaces()))

    #pp(dir(space_array[0])) # load this into memory

    floor_areas = map(lambda s: s.get_floorArea(), space_array)

    N = space_array.size

    df = pd.DataFrame(index=range(N))
    #df['spaces
    df['x'] = range(N)
    df['y'] = floor_areas

    colnum, rownum = df.shape[0], df.shape[1]

    return df, osm, ops


if __name__ == "__main__":
    
    df, osm, ops = main()

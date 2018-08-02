from __future__ import print_function
from loadenv import *
import osm_load

"""
installation instructions:
pip install pythonnet
# https://github.com/NREL/OpenStudio/releases?after=v1.13.2
"""

DEFAULT_OSM_PATH = os.path.join(CURR_DIR, "src", "trnco_fe","in.osm")
DEFAULT_OSM_DIR = "C:\\Users\\631\\Desktop\\openstudioapp"

def get_points(surface_vector):

    srf_mtx = np.array([None]*len(surface_vector))

    # Make nested list of openstudio Point3d objects
    for i in xrange(len(surface_vector)):
        vnum = surface_vector[i].vertices().Count
        vlst = [None]*vnum
        for j in xrange(vnum):
            vlst[j] = surface_vector[i].vertices()[j]
        srf_mtx[i] = vlst
    #vertice_matrix = np.asmatrix(vertice_matrix)

    return srf_mtx

def get_surface(osm,ops):

    outside_surface_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()=="Outdoors",
            osm.getSurfaces()))

    inside_surface_vector = np.array(
        filter(lambda s: s.outsideBoundaryCondition()!="Outdoors",
            osm.getSurfaces()))

    out_pts = get_points(outside_surface_vector)
    ins_pts = get_points(inside_surface_vector)

def main(ops):
    osm = osm_load.load_osm(DEFAULT_OSM_PATH, ops)

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

def get_default_osm():

    subdir = os.listdir(DEFAULT_OSM_DIR)
    subdir_num_lst = map(lambda n: int(n),
        map(lambda d: d.split("_")[1] if "in_" in d else "0", subdir)
        )
    subdir_num_lst.sort()
    subdir_name = "in_" + str(subdir_num_lst[-1])
    default_osm_path = os.path.join(DEFAULT_OSM_DIR, subdir_name, "in.osm")

    if not os.path.exists(default_osm_path):
        print("The in.osm does not exist in the {} directory.".format(subdir_name))

    return default_osm_path

if __name__ == "__main__":

    ops = osm_load.load_ops()

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if "-default" in arg:
            fpathosm = get_default_osm()
        else:
            fpathosm = sys.argv[1]
        osm = osm_load.load_osm(fpathosm, ops)

    else:
        fpathosm = DEFAULT_OSM_PATH
        df, osm, ops = main(ops)

    print("osm, ops generated from {}".format(fpathosm))

from __future__ import print_function
from loadenv import *
import osm_load
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.collections import LineCollection   # was `PolyCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection

"""
installation instructions:
pip install pythonnet
# https://github.com/NREL/OpenStudio/releases?after=v1.13.2
"""

DEFAULT_OSM_PATH = os.path.join(CURR_DIR, "qxt", "trnco_fe","in.osm")
DEFAULT_OSM_DIR = "C:\\Users\\631\\Desktop\\openstudioapp"


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

def osm2pt(osm_pt):
    return (osm_pt.x(), osm_pt.y(), osm_pt.z())

def get_points(surface_vector):

    """
    Returns m x n=3 matrix of pt objects in surfaces
    np.matrix(
        [[pt1, pt2, pt3],    # surface 1
         [pt1, pt2, pt3],    # surface 2
         ...
         [pt1, pt3, pt3]])   # surface 3
    """
    srf_mtx = [] # matrix of surfaces


    # Make nested list of openstudio Point3d objects by surface
    for i in range(len(surface_vector)):
        vlst = [v for v in surface_vector[i].vertices()]
        srf_mtx.append(vlst)

    return np.matrix(srf_mtx)

def filter_surfaces(osm,srfs=None):

    helper_chk_bc = lambda bc: bc =="Outdoors" or bc == "Ground"

    if srfs==None: srfs = osm.getSurfaces()

    out_lst, in_lst = [], []
    for i in range(srfs.Count):
        if srfs[i].surfaceType()=="Wall":
            is_out = helper_chk_bc(srfs[i].outsideBoundaryCondition())
            if is_out:
                out_lst.append(srfs[i])
            else:
                in_lst.append(srfs[i])

    return out_lst, in_lst

def get_surfaces_mtx(osm):
    """
    # getter 3D matrix of surfaces by spaces
    [
    [[pt1,pt2,pt3..ptn],[pt1,pt2,pt3..ptn]]                    # space1
    [[pt1,pt2,pt3..ptn],[pt1..ptn],[pt1,pt2,pt3..ptn]]          # space2
    ...
    [[pt1,pt2,pt3..ptn],[pt1,pt2,pt3..ptn],[pt1,pt2,pt3..ptn]]  # spacen
    ]
    """

    space_array = np.array(map(lambda s: s, osm.getSpaces()))
    outsrf_mtx = []
    insrf_mtx = []
    for i in range(len(space_array)):

        space_srfs = space_array[i].surfaces

        outsrf_vec, insrf_vec = filter_surfaces(osm, space_srfs)

        outsrf_mtx.append(get_points(outsrf_vec))
        insrf_mtx.append(get_points(insrf_vec))

    return outsrf_mtx, insrf_mtx

def plot_osm_surface_2d(space_vec,linecolor='b'):
    # loop through all outside srf matrix in space_vec

    #fig, axs = plt.subplots(2, 2)

    for i in range(len(space_vec)):

        space_ = space_vec[i]

        x = []
        y = []


        len_srf = np.size(space_,0) # rows = surfaces
        len_pts = np.size(space_,1) # cols = vertices

        for j in range(len_srf):
            for k in range(len_pts):
                v = space_.item((j,k))
                p = osm2pt(v)
                x.append(p[0])
                y.append(p[1])
        plt.plot(x,y,linecolor)



def plot_osm_surface_3d(space_vec,linecolor='b'):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    #ax = Axes3D(fig)
    ax.set_aspect("equal")

    # loop through all outside srf matrix in space_vec
    for i in range(len(space_vec)):

        space_ = space_vec[i]


        verts = []
        zs_ = []

        len_srf = np.size(space_,0) # matrix rows = surfaces
        len_pts = np.size(space_,1) # matrix cols = vertices

        for j in range(len_srf):
            xs_ = []
            ys_ = []

            for k in range(len_pts):
                v = space_.item((j,k))
                p = osm2pt(v)
                xs_.append(p[0])
                ys_.append(p[1])
                zs_.append(p[2])

            verts.append(list(zip(xs_,ys_)))

        poly = Line3DCollection(verts)
        ax.add_collection3d(poly, zs=zs_,zdir='z')

        #plt.plot(x,y,linecolor)
        #ax.plot(xs_, ys_, zs_,c='g')


def main(ops):
    """
    [matrix([[<OpenStudio.Point3d object at 0x000000000DE1F438>,
         <OpenStudio.Point3d object at 0x000000000DE1F470>,
         <OpenStudio.Point3d object at 0x000000000DE1F4A8>,
         <OpenStudio.Point3d object at 0x000000000DE1F4E0>]], dtype=object),
    matrix([[<OpenStudio.Point3d object at 0x000000000DE1B860>,
         <OpenStudio.Point3d object at 0x000000000DE1B780>,
         <OpenStudio.Point3d object at 0x000000000DE19940>,
         <OpenStudio.Point3d object at 0x000000000DE1F668>]], dtype=object)]
    """
    osm = osm_load.load_osm(DEFAULT_OSM_PATH, ops)

    outsrf_mtx, insrf_mtx = get_surfaces_mtx(osm)

    for i in range(len(outsrf_mtx)):
        plot_osm_surface_2d(outsrf_mtx[i],"b")
    for i in range(len(insrf_mtx)):
        plot_osm_surface_2d(insrf_mtx[i],"r")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

    #pp(dir(space_array[0])) # load this into memory
    #floor_areas = map(lambda s: s.get_floorArea(), space_array)
    #N = space_array.size
    #df = pd.DataFrame(index=range(N))
    #df['spaces
    #df['x'] = range(N)
    #df['y'] = floor_areas
    #colnum, rownum = df.shape[0], df.shape[1]

    return osm, ops


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
        osm, ops = main(ops)

    print("\nosm, ops generated from {}".format(fpathosm))

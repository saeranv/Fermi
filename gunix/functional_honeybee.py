ghenv.Component.Name = "Honeybee_Decompose Based On Type"
ghenv.Component.NickName = 'decomposeByType'
ghenv.Component.Message = 'VER 0.0.63\nJAN_20_2018'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "00 | Honeybee"
#compatibleHBVersion = VER 0.0.56\nFEB_21_2016
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc

import rhinoscriptsyntax as rs
import Rhino as rc
import scriptcontext as sc
import math


from pprint import pprint
pp = pprint

# Debug
dbg = []


"""
Functional programming with Honeybee.

For more intuitive data management.

"""

def list_to_tree(input, none_and_holes=True, source=[0]):
    #https://gist.github.com/piac/ef91ac83cb5ee92a1294
    #Transforms nestings of lists or tuples to a Grasshopper DataTree
    from Grasshopper import DataTree as Tree
    from Grasshopper.Kernel.Data import GH_Path as Path
    from System import Array

    def proc(input,tree,track):
        path = Path(Array[int](track))
        if len(input) == 0 and none_and_holes: tree.EnsurePath(path); return
        for i,item in enumerate(input):
            if hasattr(item, '__iter__'): #if list or tuple
                track.append(i); proc(item,tree,track); track.pop()
            else:
                if none_and_holes: tree.Insert(item,path,i)
                elif item is not None: tree.Add(item,path)
    if input is not None: t=Tree[object]();proc(input,t,source[:]);return t

def nest_lst_by_prop(z,f):
    D = {}
    for i in xrange(len(z)):
        key = f(z[i])
        if key in D:
            D[key].append(z[i])
        else:
            D[key] = [z[i]]
    # Get as nested list
    return [D[k] for k in D.keys()]

def get_srf_lst(zone):
    walls = []
    interiorWalls = []
    windows = []
    interiorWindows = []
    skylights =[]
    roofs = []
    ceilings = []
    floors = []
    exposedFloors = []
    groundFloors = []
    undergroundWalls = []
    undergroundSlabs = []
    undergroundCeilings = []
    shadings = []
    airWalls = []

    for srf in zone.surfaces:
        # WALL
        if srf.type == 0:
            if srf.BC.upper() == "SURFACE" or srf.BC.upper() == "ADIABATIC":
                if srf.hasChild:
                    interiorWalls.append(srf)
                    for childSrf in srf.childSrfs:
                        interiorWindows.append(childSrf)
                else:
                    interiorWalls.append(srf)

            else:
                if srf.hasChild:
                    walls.append(srf)

                    for childSrf in srf.childSrfs:
                        windows.append(childSrf)
                else:
                    walls.append(srf)

        # underground wall
        elif srf.type == 0.5:
            undergroundWalls.append(srf)

        # Roof
        elif srf.type == 1:
            if srf.hasChild:
                roofs.append(srf)
                for childSrf in srf.childSrfs:
                    skylights.append(childSrf)
            else:
                roofs.append(srf)

        # underground ceiling
        elif srf.type == 1.5:
            undergroundCeilings.append(srf)

        elif srf.type == 2: floors.append(srf)
        elif srf.type == 2.25: undergroundSlabs.append(srf)
        elif srf.type == 2.5: groundFloors.append(srf)
        elif srf.type == 2.75: exposedFloors.append(srf)
        elif srf.type == 3: ceilings.append(srf)
        elif srf.type == 4: airWalls.append(srf)
        elif srf.type == 6: shadings.append(srf)


    return [walls, interiorWalls, airWalls, windows, interiorWindows, skylights, roofs, \
           ceilings, floors, exposedFloors, groundFloors, undergroundWalls, \
           undergroundSlabs, undergroundCeilings, shadings]

def is_near_zero(n,eps=1e-14):
    return abs(n) < eps

import functools

def memoize(obj):
    #https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

def apply2depth(L,d=-1,f=lambda x:x):
    @memoize
    def get_depth(L_,d_):
        # Assume balanced tree
        if type(L_)!=type([]):
            return d_
        else:
            return get_depth(L_[0],d_+1)

    def apply2depth_(L_, d_, dinc_, f_):
        # Applies function f to node d
        if is_near_zero(d_ - dinc_):
            return f(L_)
        else:
            return [apply2depth_(L_[i],d_,dinc_+1,f_) for i in xrange(len(L_))]

    #dmax: max depth
    #d: target depth
    #dinc: current depth

    dmax = get_depth(L,0) # to make sure 0 is == first index start at -1
    d = d if d > -0.5 else dmax + d + 1  # Modify d if negative index is used as target depth

    return apply2depth_(L,d,0,f)

def get_wall_by_direction(srf,refv,tol=45):
    srf.normalVector.Unitize()
    orient_vector = rc.Geometry.Vector3d(refv[0],refv[1],refv[2])
    # Calculate the tolerance as the dot product
    tol_as_dot = 1.0 - math.cos(tol*(math.pi/180.0))
    dot_prod = srf.normalVector * orient_vector

    if is_near_zero(dot_prod-1.0,tol_as_dot):
        return srf.geometry
    else:
        return None

# Call the objects from the lib
hb_hive = sc.sticky["honeybee_Hive"]()
zonelst = hb_hive.visualizeFromHoneybeeHive(hbzone)

#-----------------------------------------------------#
# Add hb room from honeybee_room.py

# Use dictionary to sort into nested list by program
nested_zone = nest_lst_by_prop(zonelst, lambda z: z.name.split("_")[0])

# List index for surface types
# 0  walls
# 1  interiorWalls
# 2  airWalls
# 3  windows
# 4  interiorWindows
# 5  skylights
# 6  roofs
# 7  ceilings
# 8  floors
# 9  exposedFloors
# 10 groundFloors
# 11 undergroundWalls
# 12 undergroundSlabs
# 13 undergroundCeilings
# 14 shadings

# nest_srf: tree depth structure
# 0 program type
# 1 zone type
# 2 surfaces list [[wallsrfs][roofsrfs]...[ceilingsrfs]]
# 3 list of surface types
# 4 surfaces

# N.B to get the nested surfaces use srf.geometry
# or srf.punchedGeometry

# Go to root (zones) and replace zone objects with list of surfaces
nest_srf = apply2depth(nested_zone,d=-1,f=get_srf_lst)

# Get ceilings
nest_ceiling = apply2depth(nest_srf,2,lambda srflst: [s.geometry for s in srflst[7]])

# Get floors
nest_floor = apply2depth(nest_srf,2,lambda srflst: [s.geometry for s in srflst[8]])

# Get walls
nest_wall = apply2depth(nest_srf,2,lambda srflst: [s for s in srflst[0]])

# Get wall by orientation
nest_wall_N = apply2depth(nest_wall,d=-2,f=lambda srflst:
    filter(lambda n: n!=None, [get_wall_by_direction(s,(0,1,0)) for s in srflst]))
nest_wall_E = apply2depth(nest_wall,d=-2,f=lambda srflst:
    filter(lambda n: n!=None, [get_wall_by_direction(s,(1,0,0)) for s in srflst]))
nest_wall_S = apply2depth(nest_wall,d=-2,f=lambda srflst:
    filter(lambda n: n!=None, [get_wall_by_direction(s,(0,-1,0)) for s in srflst]))
nest_wall_W = apply2depth(nest_wall,d=-2,f=lambda srflst:
    filter(lambda n: n!=None, [get_wall_by_direction(s,(-1,0,0)) for s in srflst]))

# Map back to GH trees
ceiling = list_to_tree(nest_ceiling)
floor = list_to_tree(nest_floor)
exterior_wall_N = list_to_tree(nest_wall_N)
exterior_wall_E = list_to_tree(nest_wall_E)
exterior_wall_S = list_to_tree(nest_wall_S)
exterior_wall_W = list_to_tree(nest_wall_W)


# now do the data management

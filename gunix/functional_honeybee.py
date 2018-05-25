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
import scriptcontext as sc

from pprint import pprint
pp = pprint


"""
Functional programming with Honeybee.

For more intuitive data management.

"""



# Debug
dbg = []

get_program = lambda z: z.name.split("_")[0]

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


# Call the objects from the lib
hb_hive = sc.sticky["honeybee_Hive"]()
zonelst = hb_hive.visualizeFromHoneybeeHive(hbzone)



# See object properties
#dbg.extend(dir(zonelst[0]))

# Use dictionary to sort into nested list by program
nested_zone = nest_lst_by_prop(zonelst,get_program)

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

nested_srf = [
        [get_srf_lst(nested_zone[i][j]) for j in xrange(len(nested_zone[i]))]
            for i in xrange(len(nested_zone))]

# Get the nested surfaces
# use srf.geometry or srf.punchedGeometry

get_geo = lambda s:[s[i].geometry for i in xrange(len(s))]

# Get ceilings
nest_ceiling = [
        [get_geo(nested_srf[i][j][7]) for j in xrange(len(nested_srf[i]))]
            for i in xrange(len(nested_srf))]

# Get floors
nest_floor = [[
                [s.geometry                                     # operation
                    for s in nested_srf[i][j][8]]               # surfaces
                        for j in xrange(len(nested_srf[i]))]    # zones
                            for i in xrange(len(nested_srf))]   # program types

#get_north = lambda s: s.
# Get floors
#nest_wall_N = [
#        [get_north(nested_srf[i][j][0].geometry) for j in xrange(len(nested_srf[i]))]
#            for i in xrange(len(nested_srf))]
dbg.extend(dir(nested_srf[0][0][0][0]))
ceiling = list_to_tree(nest_ceiling)
floor = list_to_tree(nest_floor)

#exterior_wall_N = list_to_tree(nest_wall_N)

"""
forfirst = False
NL = nested_srf
for i in xrange(len(NL)):
    #for each type
    type = NL[i]
    print nested_zone[i][0].name
    for j in xrange(len(type)):
        # for each list of surface_lists in type
        srflst = type[j]
        if True:#if forfirst==False:
            anlysrf = srflst[6]
            dbg.extend(anlysrf)
            print len(anlysrf)
            #forfirst = True
    print '--'
"""

#print 'dbg'
#print dbg

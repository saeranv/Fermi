import Rhino as rc
import rhinoscriptsyntax as rs
import pprint
import scriptcontext as sc

pp = pprint.pprint

def tree_to_list(input, retrieve_base = lambda x: x[0]):
    """Returns a list representation of a Grasshopper DataTree"""
    def extend_at(path, index, simple_input, rest_list):
        target = path[index]
        if len(rest_list) <= target: rest_list.extend([None]*(target-len(rest_list)+1))
        if index == path.Length - 1:
            rest_list[target] = list(simple_input)
        else:
            if rest_list[target] is None: rest_list[target] = []
            extend_at(path, index+1, simple_input, rest_list[target])
    all = []
    for i in range(input.BranchCount):
        path = input.Path(i)
        extend_at(path, 0, input.Branch(path), all)
    return retrieve_base(all)

if sc.sticky.has_key('honeybee_release'):
    if sc.sticky["honeybee_folders"]["OSLibPath"] != None:
        # openstudio is there
        openStudioLibFolder = sc.sticky["honeybee_folders"]["OSLibPath"]
        openStudioIsReady = True

        # check the version of OpenStudio.
        try:
            osVersion = openStudioLibFolder.split('-')[-1].split('/')[0]
        except:
            pass

        import clr
        clr.AddReferenceToFileAndPath(openStudioLibFolder+"\\openStudio.dll")

        import sys
        if openStudioLibFolder not in sys.path:
            sys.path.append(openStudioLibFolder)

        import OpenStudio as ops
    else:
        openStudioIsReady = False
        # let the user know that they need to download OpenStudio libraries
        msg1 = "You do not have OpenStudio installed on Your System.\n" + \
            "You wont be able to use this component until you install it.\n" + \
            "Download the latest OpenStudio for Windows from:\n"
        msg2 = "https://www.openstudio.net/downloads"
        print msg1
        print msg2
        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg1)
        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg2)
else:
    openStudioIsReady = False


def is_near_zero(val, eps=1e-6):
    return abs(val) < eps

if openStudioIsReady:
    osm = ops.Model()

    breplst = tree_to_list(srftree)



    # BREP
    for i in range(len(breplst)):
        brep = breplst[i]
        #print 'brep'

        osm_space = ops.Space(osm)
        osm_space.setName("space_{}".format(i))

        #surf_vector = ops.SurfaceVector()

        # SURFACES
        for j in range(len(brep)):
            face_loop = brep[j]
            points = rs.PolylineVertices(face_loop)
            points.reverse()
            #points = points[:len(points)-2]

            srf_point_vector = ops.Point3dVector()

            # POINTS
            for k in range(len(points)):

                pt = points[k]

                ops_pt = ops.Point3d(pt.X, pt.Y, pt.Z)

                srf_point_vector.Add(ops_pt)

            # Make SURFACE
            osm_srf = ops.Surface(srf_point_vector, osm)
            osm_srf.setName("surface_{}_{}".format(i,j))
            osm_srf.setSpace(osm_space)
            #surf_vector.Add(osm_srf)


    
    starting_surfaces = osm.getSurfaces()
    print "Starting # surfaces: ", starting_surfaces.Count

    space_lst = osm.getSpaces()

    bounding_boxes = []
    for i in range(space_lst.Count):
      bounding_boxes.append(space_lst[i].boundingBox())


    # Intersect Masses
    for i in range(space_lst.Count):
        curr_space = space_lst[i]
        for j in range(space_lst.Count):
            chk_space = space_lst[j]

            # Check if within extents or same sapce
            if is_near_zero(i-j):
                continue

            if True==True:#bounding_boxes[i].intersects(bounding_boxes[j]):
                #print 'int exists'
                #try:
                #print [s for s in curr_space.surfaces]
                curr_space.intersectSurfaces(chk_space)
                # curr_space.nameString(), chk_space.nameString(),
                print curr_space.surfaces.Count, chk_space.surfaces.Count
                #print '---'
                #Util.show($"Intersected and matched {sp.nameString()} with {bSpace.nameString()}");
                #except:
                #  print 'fail to intersect'
    #print dir(ops.Model)
    finishing_surfaces = osm.getSurfaces()

    print "Finishing # surfaces: ", finishing_surfaces.Count

    space_lst = osm.getSpaces()
    # Convert back to Rhino
    intersected = []
    for i in range(space_lst.Count):
        surfaces = space_lst[i].surfaces
        for j in range(surfaces.Count):
            osm_points = surfaces[j].vertices()

            rc_points = [rc.Geometry.Point3d(p.x(), p.y(), p.z()) for p in osm_points]

            crv = rc.Geometry.Curve.CreateControlPointCurve(rc_points,1)

            intersected.append(crv)

            #rc.Geometry.Surface.Create

    osm.save(ops.Path("intersect.osm"), True)

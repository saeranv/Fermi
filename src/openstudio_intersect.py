import Rhino as rc
import rhinoscriptsyntax as rs
import pprint
import scriptcontext as sc
import ghpythonlib as ghlib

pp = pprint.pprint

"""
https://github.com/NREL/OpenStudio/search?q=intersect&unscoped_q=intersect
https://github.com/NREL/OpenStudio/blob/7865ba413ef52e8c41b8b95d6643d68eb949f1c4/openstudiocore/sketchup_plugin/openstudio/sketchup_plugin/user_scripts/Alter%20or%20Add%20Model%20Elements/Intersect_Space_Geometry.rb
https://github.com/NREL/OpenStudio/blob/7865ba413ef52e8c41b8b95d6643d68eb949f1c4/openstudiocore/sketchup_plugin/openstudio/sketchup_plugin/sketchup/Geom.rb
"""

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


def get_vectors(face, points, brep_vec):
    face_cpt = rc.Geometry.Vector3d(rs.CurveAreaCentroid(face)[0])

    vec_A = rc.Geometry.Vector3d(points[1]-points[0])
    vec_B = rc.Geometry.Vector3d(points[2]-points[1])

    normal = rc.Geometry.Vector3d.CrossProduct(vec_A, vec_B)
    normal = (face_cpt + normal) - face_cpt
    normal_reverse = (face_cpt + normal) - face_cpt
    normal_reverse.Reverse()

    normal_reverse.Unitize()
    normal.Unitize()

    return normal, normal_reverse, face_cpt

def get_norm_dist(face,points, brep_vec):

    normal, normal_reverse, face_cpt = get_vectors(face, points, brep_vec)

    norm_dist = (brep_vec - (face_cpt + normal)).Length
    norm_reverse_dist = (brep_vec - (face_cpt + normal_reverse)).Length

    return norm_dist, norm_reverse_dist


def get_norm_vec(face,points, brep_vec):

    normal, normal_reverse, face_cpt = get_vectors(face, points, brep_vec)

    return face_cpt, normal, normal_reverse

TOL = sc.doc.ModelAbsoluteTolerance

if not openStudioIsReady:
    print "Problem loading OSM. Have you let HB fly?"

else:
    osm = ops.Model()

    # BREP
    for i in range(len(breps)):
        brep = breps[i]

        osm_space = ops.Space(osm)
        osm_space.setName("space_{}".format(i))

        # ghlib methods
        faces = ghlib.components.DeconstructBrep(rs.coercebrep(brep))[0]
        brep_vec = rs.coerce3dvector(ghlib.components.Area(brep)[1])

        # SURFACES
        for j in range(len(faces)):

            face = faces[j]

            edges = ghlib.components.DeconstructBrep(face)[1]

            face_curve = rc.Geometry.Curve.JoinCurves(edges, TOL)[0]
            nc = face_curve.ToNurbsCurve()
            points = [nc.Points[i_].Location for i_ in xrange(nc.Points.Count)]
            points.pop()

            # Sort the face normals of your space
            ndist, rndist = get_norm_dist(face_curve, points, brep_vec)

            if (ndist < rndist):
                points.reverse()

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


    starting_surfaces = osm.getSurfaces()

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

            if bounding_boxes[i].intersects(bounding_boxes[j]):
                curr_space.intersectSurfaces(chk_space)
                #Util.show($"Intersected and matched {sp.nameString()} with {bSpace.nameString()}");

    finishing_surfaces = osm.getSurfaces()

    space_lst = osm.getSpaces()

    # Convert back to Rhino
    intersected = []
    for i in range(space_lst.Count):
        surfaces = space_lst[i].surfaces
        brep_faces = []
        for j in range(surfaces.Count):
            osm_points = surfaces[j].vertices()
            rc_points = [rc.Geometry.Point3d(p.x(), p.y(), p.z()) for p in osm_points]
            rc_points += [rc_points[0]]
            crv = rc.Geometry.Curve.CreateControlPointCurve(rc_points,1)

            face = ghlib.components.BoundarySurfaces(crv)
            brep_faces.append(face)

        joined_brep = ghlib.components.BrepJoin(brep_faces)[0]
        intersected.append(joined_brep)
    #osm.save(ops.Path("intersect.osm"), True)

    print "{} additional surfaces were added to your {} breps.".format(
        finishing_surfaces.Count - starting_surfaces.Count,
        osm.getSpaces().Count
        )

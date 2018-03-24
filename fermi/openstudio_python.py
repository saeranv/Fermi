import os
import sys
import math

def main():

    openstudio_dir = "C:\\Program Files\\OpenStudio 1.12.0\\CSharp\\openstudio"

    resource_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "resources"))

    if openstudio_dir not in sys.path:
        sys.path.append(openstudio_dir)

    # Make sure to add openstudio dir to path before importing clr
    import clr
    clr.AddReference("OpenStudio")
    import OpenStudio as ops

    #print dir(ops.Model)

    osm_file_path = os.path.join(resource_dir, "Office.osm")

    if not os.path.exists(osm_file_path):
        print "error at ", osm_file_path
        return 0
    """
    f = open(osm_file_path)
    for i,line in enumerate(f):
        print line
        if i > 10:
            break
    f.close()
    """

    #print ops.Model.__doc__
    #print ops.Model.load(osm_file_path)
    osm_path = ops.Path(osm_file_path)
    #print ops.Model.load.__doc__

    office = ops.Model.load(osm_path).get()
    surface_vector = office.getSurfaces()

    print surface_vector.Count

    #for i in xrange(surface_vector.Count):
    #    print i
    #for d in dir(ops.Model):
    #    print d

    return 1

if __name__ == "__main__":
    is_run = main()

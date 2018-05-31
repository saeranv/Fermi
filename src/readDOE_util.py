
indexdocstr = ""

    padding = lambda x: "----" if x==0 else "-"*abs(int(log10(x))-4)
    indexdocstr += "BLDTYPE\n"
    for i in xrange(16): indexdocstr += "{0}{1}{2}".format(i, padding(i) , BLDTYPE[i]+"\n")
    indexdocstr += "BUILTERA\n"
    for i in xrange(3): indexdocstr += "{0}{1}{2}".format(i, padding(i) , BUILTERA[i]+"\n")
    indexdocstr += "ZONETYPE\n"
    for i in xrange(16): indexdocstr += "{0}{1}{2}".format(i, padding(i) , ZONETYPE[i]+"\n")

    print "Created bld, bem, sched => 3d matrices of building, BEMdef, and Schedule objects.\nindexdocstr => Matrix index table."

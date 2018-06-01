import os
import sys

import subprocess
import rhinoscriptsyntax as rs
import scriptcontext as sc

#script = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\helloworld.py"
script = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\pyqt_jupyter.py"
cmd = "C:\\Users\\631\\AppData\\Local\\Continuum\\Anaconda2\\python.exe"

def coerce_brep(guidlst):
    return [rs.coercebrep(guid) for guid in guidlst]

def call_from_hive(hb_objects):
    hb_hive = sc.sticky["honeybee_Hive"]()
    return hb_hive.visualizeFromHoneybeeHive(hb_objects)

p = None
if launch:

    hbz = call_from_hive(
            coerce_brep(hbz)
            )

    p = subprocess.Popen([cmd, script], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print p.communicate()


else:
    if p!=None:
        p.kill()

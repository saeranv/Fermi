import os
import sys
import subprocess
import rhinoscriptsyntax as rs
import scriptcontext as sc
import shutil


# https://news.ycombinator.com/item?id=16318677
CURR_DIR = os.path.dirname(os.path.abspath(fpath))


def coerce_brep(guidlst):
    return [rs.coercebrep(guid) for guid in guidlst]


def call_from_hive(hb_objects):
    hb_hive = sc.sticky["honeybee_Hive"]()
    return hb_hive.visualizeFromHoneybeeHive(hb_objects)


def dynamic_output():
    ghcomp_output = [
        (0, "Test some stuff."),
        (1, "This could be a thing."),
        (2, "More."),
        (3, "Yo dude."),
    ]

    for i in xrange(len(ghcomp_output)):
        output_num = ghcomp_output[i][0]
        output_name = ghcomp_output[i][1]
        try:
            ghenv.Component.Params.Output[output_num].NickName = output_name
            ghenv.Component.Params.Output[output_num].Name = output_name
            ghenv.Component.Params.Output[output_num].Description = output_name
        except:
            print "Probably need to add more outputs."


p = None
if launch:

    #hbz = call_from_hive(
    #        coerce_brep(hbz)
    #        )

    # script = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\helloworld.py"
    os.chdir(os.path.join(CURR_DIR,".."))
    if "631" in CURR_DIR:
        cmd = "C:\\Users\\631\\AppData\\Local\\Continuum\\Anaconda2\\python.exe"
    else:
        cmd = "C:\\Users\\user\\Anaconda2\\python.exe"
    script = os.path.join(CURR_DIR, "pyqt_jupyter.py")

    #p = subprocess.Popen([cmd, script, argstr], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print p.communicate()
    p = subprocess.Popen([cmd,script,argstr], shell=True) #stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print p.communicate()

    file_src = os.path.join(CURR_DIR,"grsshppr_gunix.py")
    file_dst = os.path.join(CURR_DIR,"grsshppr_gunix_tmp.py")
    if not os.path.exists(file_dst):
        shutil.copyfile(file_src, file_dst)

    dynamic_output()

else:
    if p!=None:
        p.kill()

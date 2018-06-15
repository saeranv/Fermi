import os
import sys

import subprocess
import rhinoscriptsyntax as rs
import scriptcontext as sc
import shutil

# https://news.ycombinator.com/item?id=16318677

#script = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\helloworld.py"
script = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\pyqt_jupyter.py"
cmd = "C:\\Users\\631\\AppData\\Local\\Continuum\\Anaconda2\\python.exe"

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
        (3, "Even More."),
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

    #p = subprocess.Popen([cmd, script], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print p.communicate()

    file_src = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\grsshppr_gunix.py"
    file_dst = "C:\\Users\\631\\Documents\\GitHub\\Fermi\\src\\grsshppr_gunix_tmp.py"
    if not os.path.exists(file_dst):
        shutil.copyfile(file_src, file_dst)

    dynamic_output()

else:
    if p!=None:
        p.kill()

"""
#HB update code from source file.
def getAllTheComponents(onlyGHPython = True):

    components = []

    document = ghenv.Component.OnPingDocument()

    objects = list(document.Objects)

    # check if there is any cluster and collect the objects inside clusters
    for obj in objects:
        if type(obj) == gh.Special.GH_Cluster:
            clusterDoc = obj.Document("")
            if not clusterDoc:
                continue
            for clusterObj in  clusterDoc.Objects:
                objects.append(clusterObj)

    for component in objects:
        if onlyGHPython and type(component)!= type(ghenv.Component):
            pass
        else:
            components.append(component)

    return components

def updateTheComponent(component, newUOFolder, lb_preparation):

    def isNewerVersion(currentUO, component):
        #check if the component has a newer version than the current userObjects

        # get the code insider the userObject
        ghComponent = currentUO.InstantiateObject()

        # version of the connected component
        if component.Message == None:
            return True, ghComponent.Code
        if len(component.Message.split("\n"))<2:
            return True, ghComponent.Code

        ghVersion, ghDate = component.Message.split("\n")
        ghCompVersion = map(int, ghVersion.split("VER ")[1].split("."))
        month, day, ghYear  = ghDate.split("_")
        # print version, date
        month = lb_preparation.monthList.index(month.upper()) + 1
        ghCompDate = int(lb_preparation.getJD(month, day))

        # this is not the best way but works for now!
        # should be a better way to compute the component and get the message
        componentCode = ghComponent.Code.split("\n")
        UODate = ghCompDate - 1
        # version of the file
        for lineCount, line in enumerate(componentCode):
            if lineCount > 200: break
            if line.strip().startswith("ghenv.Component.Message"):
                #print line
                # print line.split("=")[1].strip().split("\n")
                version, date = line.split("=")[1].strip().split("\\n")

                # in case the file doesn't have an standard Ladybug message let it be updated
                try:
                    UOVersion = map(int, version.split("VER ")[1].split("."))
                except Exception, e:
                    return True, ghComponent.Code
                month, day, UOYear  = date.split("_")
                month = lb_preparation.monthList.index(month.upper()) + 1
                UODate = int(lb_preparation.getJD(month, day))
                break

        # check if the version of the code is newer
        if int(ghYear.strip()) < int(UOYear[:-1].strip()):
                return True, ghComponent.Code
        elif ghCompDate < UODate:
            return True, ghComponent.Code
        elif ghCompDate == UODate:
            for ghVer, UOVer in zip(UOVersion, UOVersion):
                if ghVer > UOVer: return False, " "
            return True, ghComponent.Code
        else:
            return False, " "

    # check if the userObject is already existed in the folder
    try:
        filePath = os.path.join(newUOFolder, component.Name + ".ghuser")
        newUO = gh.GH_UserObject(filePath)
    except:
        # there is no newer userobject with the same name so just return
        return

    # if is newer remove
    isNewer, newCode = isNewerVersion(newUO, component)
    # replace the code inside the component with userObject code
    if isNewer:
        if component.CodeInputParam == None:
            component.Code = newCode
            component.ExpireSolution(True)
        else:
            warning = "Failed to update %s. Remove code input from the component and try again!"%component.Name
            print warning
            ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, warning)
"""

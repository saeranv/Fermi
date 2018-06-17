
# http://www.ironpython.info/index.php?title=Watching_the_FileSystem
from System.IO import FileSystemWatcher
from System.Threading import Thread

watcher = FileSystemWatcher()
watcher.Path = 'c:\\Temp'

def onChanged(source, event):
    print 'Changed:', event.ChangeType, event.FullPath

def onRenamed(source, event):
    print 'Renamed:', event.OldFullPath, event.FullPath

watcher.Changed += onChanged
watcher.Created += onChanged
watcher.Deleted += onChanged
watcher.Renamed += onRenamed

watcher.EnableRaisingEvents = True 

# wait for an hour
Thread.Sleep(60 * 1000 * 60)

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


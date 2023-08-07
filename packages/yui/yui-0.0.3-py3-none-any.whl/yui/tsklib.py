#!/usr/bin/env python
import os, glob, yaml
from appdata import AppDataPaths

Title="Yui"
cmd="yui"

def tskpath():
    default=cmd
    home = os.getenv("YUI_HOME", default)
    path = AppDataPaths(home).app_data_path
    os.makedirs(path, exist_ok=True)
    return path
    pass

def getTaskFilenameById(id, location="*"):
    files = findTaskFiles( location, "*."+id+".md")
    if len(files) == 0:
        suffix = ""
        if location !="*":
            suffix = " in "+location
        print("task with id="+id+" not found"+suffix)
        exit(1)
    pass;
    if len(files) != 1:
        print("more than one task with id="+id+" found. That should never happen")
        exit(1)
    pass;
    return files[0]
    pass

def findTaskFiles(location, pattern):
    return glob.glob( tskpath() + "/"+location+"/*/"+pattern)
    pass

def getConfigParam(param):
    return loadYaml( tskpath() + "/config.yaml" )[param]
    pass

def loadYaml(filename):
    with open( filename ) as f:
        return next(yaml.load_all(f, Loader=yaml.loader.UnsafeLoader))
        pass
    pass

def saveYaml(filename, data):
    with open( filename, 'w' ) as f:
        yaml.dump( data, f )
        pass
    pass

def gitInitIfNotPresent():
    workingdir = tskpath()
    if os.path.isdir( workingdir+"/.git"):
        return
        pass
    curpath = os.getcwd();
    os.chdir(workingdir);
    os.system("git init > /dev/null");
    os.chdir(curpath);
    pass

def gitAddCommitTask(message):
    gitInitIfNotPresent()
    curpath = os.getcwd();
    os.chdir(tskpath());
    os.system("git add ./*.md > /dev/null && git commit -m '"+message+"' > /dev/null");
    os.chdir(curpath);
    pass

def getLastId():
    files = findTaskFiles("*", "*.md")
    maxId = -1
    for filename in files :
        # Open the file and load the file
        id = loadYaml( filename )["id"]
        if id > maxId:
            maxId = id
            pass
        pass
    return maxId
    pass

def newScope():
    return {
        "project":"",
        "context":""
        }
    pass

def loadScope():
    scope = newScope()
    try:
        data = loadYaml( tskpath()+"/scope.yaml")
        for key in scope:
            try:
                scope[key] = data[key]
            except:
                pass
            pass
    except:
        pass
    return scope
    pass

def mergeScope( orig, changes ):
    scope = orig
    for key in changes:
        if changes[key] == "":
            continue
        scope[key] = changes[key]
    return scope
    pass

def parseFilter( filterstring ):
    scope = newScope()
    if filterstring == "":
        return scope
        pass
    # split by ,
    pairs = filterstring.split(",")
    for pair in pairs:
        keyvalue = pair.split(":")
        key = keyvalue[0]
        value = keyvalue[1]
        if key == "c":
            key = "context"
            pass
        if key == "p":
            key = "project"
            pass
        scope[key] = value
        pass
    return scope
    pass

def getScope():
    scope = loadScope()
    scope = mergeScope( scope, parseFilter(os.getenv("YET","")) )
    for key in scope:
        scope[key] = os.getenv("YET_" + key.upper(), scope[key])
        pass
    return scope
    pass

def saveScope( scope ):
    saveYaml( tskpath()+"/scope.yaml", scope)
    pass

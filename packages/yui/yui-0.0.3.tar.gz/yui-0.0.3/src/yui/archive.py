#!/usr/bin/env python
import os, sys, glob, yaml, subprocess, datetime
from yui import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        Usage:
            """+tsklib.cmd+""" archive %date%      - move done tasks from .yet/cur to archive with specific date
        Example:
            """+tsklib.cmd+""" archive today // bug here, uses UTC date, instead of local date
            """+tsklib.cmd+""" archive yesterday
            """+tsklib.cmd+""" archive 2023-01-03
            """)
        exit(1);
        pass;
    date = argv[0]
    if( date == "today" ):
        date = datetime.date.today().strftime("%Y-%m-%d")
        pass
    if( date == "yesterday" ):
        date = (datetime.date.today() - datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
        pass

    files = tsklib.findTaskFiles("cur", "*.md")
    if len(files) == 0:
        print("No tasks found")
        exit(1)
        pass

    for filename in files:
        task =  tsklib.loadYaml(filename) 
        if task["status"] != "done":
            continue
        pass
        targetPath = tsklib.tskpath() + "/"+date+"/"+task["status"]
        os.makedirs(targetPath, exist_ok=True)
        print("moving " + task["filename"] + " to "+date+" .. ", end="")
        os.rename( filename, targetPath + "/" + task["filename"]);
        print("done")
    pass
    tsklib.gitAddCommitTask("reset "+str(id));
    pass

if __name__=="__main__":
    main()
    pass

#!/usr/bin/env python
import os, sys, glob, yaml, subprocess
from yui import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        Usage:
            """+tsklib.cmd+""" pick %taskId%   - pick single task to current day
        Example:
            """+tsklib.cmd+""" pick 3
            """)
        exit(1);
        pass;
    id = argv[0]
    filename = tsklib.getTaskFilenameById(id, "heap")
    task = tsklib.loadYaml(filename)
    targetPath = tsklib.tskpath() + "/cur/" + task["status"]
    os.makedirs(targetPath, exist_ok=True)
    os.rename( filename, targetPath + "/" + task["filename"]);
    tsklib.gitAddCommitTask("pick "+id);
    pass

if __name__=="__main__":
    main()
    pass


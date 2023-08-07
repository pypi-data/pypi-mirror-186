#!/usr/bin/env python
import os, sys, glob, yaml, subprocess
from yui import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        Usage:
            """+tsklib.cmd+""" open %taskId%   - open single task with text editor ( see ~/.tsk/config.yaml )
        Example:
            """+tsklib.cmd+""" open 3
            """)
        exit(1);
        pass;
    id = argv[0]
    filename = tsklib.getTaskFilenameById(id)
    try:
        editor = tsklib.getConfigParam("editor")
    except:
        candidates = [ os.getenv("EDITOR"), "mcedit","nano", "vim", "vi","ee"]
        for candidate in candidates:
            if subprocess.call("which " + candidate + "> /dev/null", shell=True) == 0:
                editor = candidate+" %"
                break
            pass
    if editor=="":
        print("Can't detect text editor, use "+tsklib.tskpath()+"/config.yaml to specify");
        exit(1);
        pass

    cmd = editor.replace("%", filename)
    subprocess.call( cmd, shell=True );
    pass

if __name__=="__main__":
    main()
    pass

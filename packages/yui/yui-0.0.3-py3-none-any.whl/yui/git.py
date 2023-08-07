#!/usr/bin/env python
import os, sys
from yui import tsklib


def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    home = os.path.expanduser("~");
    curpath = os.getcwd();
    os.chdir(tsklib.tskpath());
    os.system("git "+' '.join(argv));
    os.chdir(curpath);
    pass

if __name__=="__main__":
    main()
    pass




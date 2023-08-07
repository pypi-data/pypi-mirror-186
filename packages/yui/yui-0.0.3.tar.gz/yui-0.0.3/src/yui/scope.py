#!/usr/bin/env python
import os, sys, glob, yaml, subprocess, datetime
from yui import tsklib
from pathlib import Path

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
    Usage:
        """+tsklib.cmd+""" scope reset
        """+tsklib.cmd+""" scope context contextName
        """+tsklib.cmd+""" scope project projectName
        """+tsklib.cmd+""" scope list
            """)
        exit(1);
        pass;

    command = argv[0]
    scope = tsklib.getScope();
    if command == "list":
        for key in scope:
            print("Name: "+key+" = "+scope[key] )
        exit(0)
        pass

    if command == "reset":
        tsklib.saveScope({})
        exit(0)
        pass

    if not command in scope.keys():
        print("Unexpected parameter "+command)
        exit(1)
        pass

    argv.pop(0)
    value = " ".join(argv)
    scope[command] = value
    tsklib.saveScope( scope )
    pass

if __name__=="__main__":
    main()
    pass

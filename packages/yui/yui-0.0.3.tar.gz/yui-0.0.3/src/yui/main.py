#!/usr/bin/env python
import os, sys;
from yui import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
    Usage:
        """+tsklib.cmd+""" create %taskname%   - create new task, return taskId and filename
        # """+tsklib.cmd+""" list                - show current tasks
        """+tsklib.cmd+""" list heap           - show tasks from heap
        """+tsklib.cmd+""" list cur            - show tasks for current date
        """+tsklib.cmd+""" pick %taskId%       - move tsak from heap to current date
        """+tsklib.cmd+""" lastid              - show last insert id
        """+tsklib.cmd+""" open %taskId%       - open task in kate (parallel kate filename.md)
        """+tsklib.cmd+""" reset               - move not finished tasks back to heap
        """+tsklib.cmd+""" archive             - move done tasks from cur to archive with date
        """+tsklib.cmd+""" scope               - change/reset scope ( current context and project ) affects avironment variables """+tsklib.cmd+"""_CONTEXT, """+tsklib.cmd+"""_PROJECT
        """+tsklib.cmd+""" drop                - Use with care! completely remove task with specific id
        """+tsklib.cmd+""" git %attributes%    - run git on ./"""+tsklib.cmd+""" folder
        
    Environmant variables:
        """+tsklib.cmd.upper()+"""_CONTEXT             - set context
        """+tsklib.cmd.upper()+"""_PROJECT             - set project
        """+tsklib.cmd.upper()+"""                     - short version for setting both project and context
        """+tsklib.cmd.upper()+"""_HOME                - working folder name inside AppData/home (~/."""+tsklib.cmd+"""_agavestorm is default value for Linux)
        
        Examples:
            """+tsklib.cmd.upper()+"""_PROJECT=myproj """+tsklib.cmd+""" create task decription
                                 - will create task with project parameter set to `myproj`
            """+tsklib.cmd.upper()+"""_CONTEXT=personal """+tsklib.cmd+""" list cur
                                 - will show only tasks in `personal` scope
            """+tsklib.cmd.upper()+"""=context:personal - equivalent for`"""+tsklib.cmd.upper()+"""_CONTEXT=personal
            """+tsklib.cmd.upper()+"""=context:personal,project:myproj
                                 - equivalent for `"""+tsklib.cmd.upper()+"""_CONTEXT=personal """+tsklib.cmd.upper()+"""_PROJECT=myproj """+tsklib.cmd+""" ...`
            """+tsklib.cmd.upper()+"""=p:proj,c:context - equivalent for `"""+tsklib.cmd.upper()+"""=context:personal,project:myproj` parameter order does not matter
            
        Priorities:
            """+tsklib.cmd.upper()+"""_CONTEXT, """+tsklib.cmd.upper()+"""_PROJECT - high
            """+tsklib.cmd.upper()+"""                      - middle
            scope.yaml               - low
            """);
        exit(1);
        pass

    os.system(tsklib.cmd+"-"+' '.join(argv)); # works same as tsklib.cmd-$@ in bash
    pass

if __name__=="__main__":
    main()
    pass

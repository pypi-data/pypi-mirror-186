# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
import sys
import os
from pathlib import Path
from fkb.object import Object
from fkb.initialize import Initialize
from fkb.filesystem import *

def Add(args: Dict[str, str], config: Dict[str, str]):
    '''
    Add an object specified by args to the FKB database.

    Arguments:

    args            - a dictionary containing the following fields:
                        file        - the relative filepath of the
                            object to be added
                        title       - title of object
                        category    - category of object
                        author      - author of the object
                        tags        - tags of the object
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    if len(args['file']) == 0:
        print('Please specify a file for the new object')
        sys.exit(1)

    db = Initialize(config)

    for fname in args['file']:
        if IsDirectory(fname):
            continue
        

        absPath = Path(os.getcwd(), fname).resolve()
        if not absPath.is_relative_to(config['PATH_FKB_ROOT']):
            print('File ' + str(absPath) + ' isn\'t contained in KB Root: ' + config['PATH_FKB_ROOT'])
            sys.exit(1)
        
        relPath = str(absPath.relative_to(config['PATH_FKB_ROOT']))

        if not os.path.exists(absPath):
            print('File ' + str(absPath) + ' wasn\'t found')
            sys.exit(1)

        if db.GetObjectByPath(relPath) is not None:
            print('File ' + str(absPath) + ' is already registered, skipping')
            continue
        
        id = None
        path = relPath
        title = args['title'] if args['title'] is not None else GetFileBasename(fname)
        category = args['category']
        tags = args['tags']
        author = args['author']

        # Create file into an Object and add to database
        obj = Object(id, path, title, category, tags, author)

        db.AddObject(obj)
    pass
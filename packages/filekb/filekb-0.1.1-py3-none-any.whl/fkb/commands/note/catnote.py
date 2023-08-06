# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
import os
from pathlib import Path
from fkb.object import Object
from fkb.initialize import Initialize
from fkb.filesystem import *

def CatNote(args: Dict[str, str], config: Dict[str, str]):
    '''
    Find an object given args and cat its note to terminal.

    Arguments:

    args            - a dictionary containing the following fields:
                        viewID      - id of object's viewID from list
                        title       - title of object
                        category    - category of object
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    db = Initialize(config)

    if args['viewID'] is not None:
        objID = db.GetObjectIDFromHistoryViewID(args['viewID'])
        obj = db.GetObjectByID(objID)
        if obj is not None:
            CatObjectNote(obj, config)
    elif args['title'] is not None:
        if args['category'] is not None:
            obj = db.GetObjectByName(args['title'], args['category'])
            if obj is not None:
                CatObjectNote(obj, config)
        else:
            # Try to infer category if there is only 1 object with this title
            objs = db.GetObjectsByTitle(args['title'], strict = True)
            if len(objs) == 1:
                CatObjectNote(objs[0], config)
            elif len(objs) > 1:
                print('Error: multiple objects with title \"' + args['title'] + '\" exist in the database')

def CatObjectNote(obj : Object, config: Dict[str, str]):
    '''
    Given an FKB Object, access the note and cat it to the terminal

    Arguments:

    obj             - an FKB object
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    fileExt = '.txt'
    editFileFullPath = str(Path(config['PATH_FKB_DATA'], obj.path)) + fileExt

    # If editable file doesn't exist, nothing to do
    if not os.path.exists(editFileFullPath):
        return

    # Cat the file to terminal
    with open(editFileFullPath) as file:
        for line in file:
            print(line.strip('\n'))
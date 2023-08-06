# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from fkb.initialize import Initialize
from fkb.object import Object
from fkb.filesystem import *

def Delete(args: Dict[str, str], config: Dict[str, str]):
    '''
    Find an object given args and delete it.

    Arguments:

    args            - a dictionary containing the following fields:
                        viewID      - id of object's viewID from list
                        title       - title of object
                        category    - category of object
                        force       - whether to force deletion w/o prompt
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    db = Initialize(config)

    if args['viewID'] is not None:
        for viewID in args['viewID']:
            objID = db.GetObjectIDFromHistoryViewID(viewID)
            obj = db.GetObjectByID(objID)
            if DeletionConfirmation(obj, force = args['force']):
                db.DeleteObjectByID(objID)
        return
    elif args['title'] is not None:
        if args['category'] is not None:
            obj = db.GetObjectByName(args['title'], args['category'])
            if DeletionConfirmation(obj, force = args['force']):
                db.DeleteObjectByID(obj.id)
            return
        else:
            # Try to infer category if there is only 1 object with this title
            objs = db.GetObjectsByTitle(args['title'], strict = True)
            if len(objs) == 1:
                if DeletionConfirmation(objs[0], force = args['force']):
                    db.DeleteObjectByID(objs[0].id)
                return
            elif len(objs) > 1:
                print('Error: multiple objects with title \'' + args['title'] + '\' exist in the database')
                return

def DeletionConfirmation(obj: Object, force: bool = False) -> bool:
    '''
    Query user for object deletion confirmation

    Arguments:

    obj             - an fkb object
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    if obj is None:
        print('No object found to delete')
        return False

    if force:
        return True
    
    answer = input(
        'Are you sure you want to delete \'{title}\' in category \'{category}\'? [y/n]'
        .format(category=obj.category, title=obj.title)
        )
    return not (answer.lower() not in ['y','yes'])
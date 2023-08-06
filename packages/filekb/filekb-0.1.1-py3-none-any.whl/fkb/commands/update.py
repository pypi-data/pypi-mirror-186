# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from fkb.object import Object
from fkb.initialize import Initialize

def Update(args: Dict[str, str], config: Dict[str, str]):
    '''
    Find an object given args and cat its note to terminal.

    Arguments:

    args            - a dictionary containing the following fields:
                        viewID      - id of object's viewID from list
                        title       - title to update
                        category    - category to update
                        tags        - tags to update
                        author      - author to update
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    db = Initialize(config)

    objID = db.GetObjectIDFromHistoryViewID(args['viewID'])

    newObj = Object(None, None, args['title'], args['category'], args['tags'], args['author'])

    db.UpdateObjectByID(objID, newObj)
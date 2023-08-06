# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from fkb.printer.search import *
from fkb.initialize import Initialize
from fkb.filesystem import *

def Search(args: Dict[str, str], config: Dict[str, str]):
    '''
    Search through objects and print out results

    Arguments:

    args            - a dictionary containing the following fields:
                        path        - relative path of object to
                            config['PATH_FKB_ROOT']
                        title       - title of object
                        category    - category of object
                        tags        - tags of object
                        strict      - whether to apply strict searching
                        noColor     - whether to print in no color mode
                        verbose     - whether to use verbose print mode
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    db = Initialize(config)

    strict = args['strict']

    tags_list = None
    if args['tags'] is not None and args['tags'] != '':
        tags_list = args['tags'].split(';')\

    # If filter applied, do search, else give everything
    if  args['path']        is not None or \
        args['title']       is not None or \
        args['category']    is not None or \
        args['tags']        is not None or \
        args['author']      is not None:
        rows = db.GetObjectsByFilter(
            path = args['path'],
            title = args['title'],
            category = args['category'],
            tags = tags_list,
            author = args['author'],
            strict = strict
        )
    else:
        rows = db.GetAllObjects()

    if len(rows) == 0:
        return

    sortedRows = sorted(rows, key = lambda row : row.title)
    
    db.WriteSearchToHistoryFile(sortedRows)
    
    color = False if args['noColor'] else True

    if args['verbose']:
        PrintSearchResultVerbose(sortedRows, config, color = color)
    else:
        PrintSearchResult(sortedRows, config, color = color)
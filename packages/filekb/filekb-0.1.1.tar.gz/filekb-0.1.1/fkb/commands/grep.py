# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from pathlib import Path
import re
import collections
from fkb.object import Object
from fkb.initialize import Initialize
from fkb.filesystem import *
from fkb.printer.grep import *

def Grep(args: Dict[str, str], config: Dict[str, str]):
    '''
    Search through object's notes using a regex

    Arguments:

    args            - a dictionary containing the following fields:
                        path        - relative path of object to
                            config['PATH_FKB_ROOT']
                        title       - title of object
                        category    - category of object
                        tags        - tags of object
                        strict      - whether to apply strict searching
                        caseInsensitive
                                    - whether ot apply case insensitive
                                      searching
                        regex       - the regex to search through notes
                        noColor     - whether to print in no color mode
                        matches     - whether to just print regex matches
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

    caseInsensitive = args['caseInsensitive']
    regex = args['regex']
    fileExt = '.txt'

    if caseInsensitive:
        pattern = re.compile(regex, re.IGNORECASE)
    else:
        pattern = re.compile(regex)

    matches = []
    for rowID, obj in enumerate(rows):
        filePath = str(Path(config['PATH_FKB_DATA'], obj.path)) + fileExt
        
        if not os.path.exists(filePath):
            continue
        
        try:
            with open(filePath) as handle:
                for i, line in enumerate(handle):
                    match = pattern.search(line)
                    linenumber = i + 1
                    if match:
                        matches.append((rowID, obj.id, linenumber, line.strip()))
        except UnicodeDecodeError:
            # In this case the file is binary,
            # so we don't search through binary files
            continue
    
    if len(matches) == 0:
        return
    
    color = False if args['noColor'] else True

    objIDHitCounts = collections.defaultdict(int)
    for match in matches:
        objIDHitCounts[match[1]] += 1

    # If user specified --matches -> just show matching lines and exit
    # Do this before removing rows without hits so that rowID is still a valid index
    if args['matches']:
        PrintGrepMatches(rows, matches, objIDHitCounts, config, color = color)
        return
    
    # Filter out objects without any hits. RowID will no longer be a valid index, use object id to see if a match came from a specific object
    rows = [row for row in rows if objIDHitCounts[row.id] > 0]

    sortedRows = sorted(rows, key = lambda row : objIDHitCounts[row.id], reverse = True)

    db.WriteSearchToHistoryFile(sortedRows)

    if args['verbose']:
        PrintGrepResultVerbose(sortedRows, objIDHitCounts, config, color = color)
    else:
        PrintGrepResult(sortedRows, objIDHitCounts, config, color = color)
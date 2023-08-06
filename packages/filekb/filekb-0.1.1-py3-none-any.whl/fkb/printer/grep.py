# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import List, Dict
from fkb.printer.style import ALT_BGROUND, BOLD, UND, RESET
from fkb.object import Object
import collections
import math

def PrintGrepResult(grepResult: List[Object], grepHits: collections.defaultdict(int), config: Dict[str, str], color: bool = True) -> None:
    '''
    Print kb query search results
    Arguments:
    grepResult      - the list of Artifacts to print
                      in the form of search result
    grepHits        - a dict containing number of matches
                      for each object ID
    config          - a configuration dictionary as specified
                      in fkb/config.py
    color           - a boolean, True if color is enabled
    '''
    minLength = 20
    lenViewID = max(len(str(len(grepResult) - 1)), 2)

    lenTitle        = max(max([len(obj.title)       for obj in grepResult]), minLength)
    lenCategory     = max(max([len(obj.category)    for obj in grepResult]), minLength)
    lenTags         = max(max([len(obj.tags)        if obj.tags     is not None else 0 for obj in grepResult]), minLength)

    lenHits         = max(max(grepHits.values()), len('Hits'))

    header = '   [ {id} ]  {title} {category} {hits} {tags}'.format(
        id='ID'.rjust(lenViewID),
        title='Title'.ljust(lenTitle),
        category='Category'.ljust(lenCategory),
        hits='Hits'.ljust(lenHits),
        tags='Tags'.ljust(lenTags)
    )

    if color:
        print(UND + BOLD + header + RESET)
    else:
        print(header)
    print()

    # Print results
    for viewID, obj in enumerate(grepResult):
        tags = obj.tags if obj.tags else ''

        result_line = '   [ {id} ]  {title} {category} {hits} {tags}'.format(
            id=str(viewID).rjust(lenViewID),
            title=obj.title.ljust(lenTitle),
            category=obj.category.ljust(lenCategory),
            hits=str(grepHits[obj.id]).ljust(lenHits),
            tags=tags.ljust(lenTags)
        )

        if color and (viewID % 2 == 0):
            print(ALT_BGROUND + result_line + RESET)
        else:
            print(result_line)


def PrintGrepResultVerbose(grepResult: List[Object], grepHits: collections.defaultdict(int), config: Dict[str, str], color: bool = True) -> None:
    '''
    Print kb query search results
    Arguments:
    grepResult      - the list of Artifacts to print
                      in the form of search result
    grepHits        - a dict containing number of matches
                      for each object ID
    config          - a configuration dictionary as specified
                      in fkb/config.py
    color           - a boolean, True if color is enabled
    '''
    minLength = 20
    secondaryMinLength = 10
    lenViewID       = max(max([len(str(obj.id)) for obj in grepResult]), 2)

    lenTitle        = max(max([len(obj.title)       for obj in grepResult]), minLength)
    lenCategory     = max(max([len(obj.category)    for obj in grepResult]), minLength)
    lenTags         = max(max([len(obj.tags)        if obj.tags     is not None else 0 for obj in grepResult]), minLength)
    lenAuthor       = max(max([len(obj.author)      if obj.author   is not None else 0 for obj in grepResult]), secondaryMinLength)

    pathHeader = 'Path rel. to ' + config['PATH_FKB_ROOT']

    lenPath         = max(max([len(obj.path)        for obj in grepResult]), max(secondaryMinLength, len(pathHeader)))

    lenHits         = max(max(grepHits.values()), len('Hits'))
    
    header = '   [ {id} ]  {title} {category} {hits} {tags} {author} {path}'.format(
        id='ID'.rjust(lenViewID),
        title='Title'.ljust(lenTitle),
        category='Category'.ljust(lenCategory),
        hits='Hits'.ljust(lenHits),
        tags='Tags'.ljust(lenTags),
        author='Author'.ljust(lenAuthor),
        path=pathHeader.ljust(lenPath)
    )

    if color:
        print(UND + BOLD + header + RESET)
    else:
        print(header)

    # Print results
    for viewID, obj in enumerate(grepResult):
        tags = obj.tags if obj.tags else ''
        author = obj.author if obj.author else ''

        result_line = '   [ {id} ]  {title} {category} {hits} {tags} {author} {path}'.format(
            id=str(viewID).rjust(lenViewID),
            title=obj.title.ljust(lenTitle),
            category=obj.category.ljust(lenCategory),
            hits=str(grepHits[obj.id]).ljust(lenHits),
            tags=tags.ljust(lenTags),
            author=author.ljust(lenAuthor),
            path=obj.path.ljust(lenPath)
        )

        if color and (viewID % 2 == 0):
            print(ALT_BGROUND + result_line + RESET)
        else:
            print(result_line)

def PrintGrepMatches(searchResult: List[Object], grepMatches: List[tuple], objIDHitCounts: collections.defaultdict(int), config: Dict[str, str], color: bool = True):
    minLength = 20

    lenTitle        = max(max([len(obj.title)       for obj in searchResult if objIDHitCounts[obj.id] > 0]), minLength)
    lenCategory     = max(max([len(obj.category)    for obj in searchResult if objIDHitCounts[obj.id] > 0]), minLength)
    lenLineNumber   = max(max([math.floor(math.log10(match[2])) for match in grepMatches]) + 1, len('Matched Text'))
    lenMatchedText  = max(max([len(match[3]) for match in grepMatches]), len('Line'))
    
    header = ' {title} {category} {lineNumber} {matchedText}'.format(
        title='Title'.ljust(lenTitle),
        category='Category'.ljust(lenCategory),
        lineNumber='Line Number'.ljust(lenLineNumber),
        matchedText='Matched Text'.ljust(lenMatchedText)
    )

    if color:
        print(UND + BOLD + header + RESET)
    else:
        print(header)

    
    for viewID, match in enumerate(grepMatches):
        obj = searchResult[match[0]]
        lineNumber = match[2]
        matchedText = match[3]

        result_line = ' {title} {category} {lineNumber} {matchedText}'.format(
            title=obj.title.ljust(lenTitle),
            category=obj.category.ljust(lenCategory),
            lineNumber=str(lineNumber).ljust(lenLineNumber),
            matchedText=matchedText.ljust(lenMatchedText)
        )

        if color and (viewID % 2 == 0):
            print(ALT_BGROUND + result_line + RESET)
        else:
            print(result_line)
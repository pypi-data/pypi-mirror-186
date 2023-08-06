# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import List, Dict
from fkb.printer.style import ALT_BGROUND, BOLD, UND, RESET
from fkb.object import Object

def PrintSearchResult(searchResult: List[Object], config: Dict[str, str], color: bool = True) -> None:
    '''
    Print kb query search results
    Arguments:
    search_result   - the list of Artifacts to print
                      in the form of search result
    config          - a configuration dictionary as specified
                      in fkb/config.py
    color           - a boolean, True if color is enabled
    '''
    minLength = 20
    lenViewID = max(len(str(len(searchResult) - 1)), 2)

    lenTitle        = max(max([len(obj.title)       for obj in searchResult]), minLength)
    lenCategory     = max(max([len(obj.category)    for obj in searchResult]), minLength)
    lenTags         = max(max([len(obj.tags)        if obj.tags     is not None else 0 for obj in searchResult]), minLength)

    header = '   [ {id} ]  {title} {category} {tags}'.format(
        id='ID'.rjust(lenViewID),
        title='Title'.ljust(lenTitle),
        category='Category'.ljust(lenCategory),
        tags='Tags'.ljust(lenTags)
    )

    if color:
        print(UND + BOLD + header + RESET)
    else:
        print(header)
    print()

    # Print results
    for viewID, obj in enumerate(searchResult):
        tags = obj.tags if obj.tags else ''

        result_line = '   [ {id} ]  {title} {category} {tags}'.format(
            id=str(viewID).rjust(lenViewID),
            title=obj.title.ljust(lenTitle),
            category=obj.category.ljust(lenCategory),
            tags=tags.ljust(lenTags)
        )

        if color and (viewID % 2 == 0):
            print(ALT_BGROUND + result_line + RESET)
        else:
            print(result_line)


def PrintSearchResultVerbose(searchResult: List[Object], config: Dict[str, str], color: bool = True) -> None:
    '''
    Print kb query search results
    Arguments:
    search_result   - the list of Artifacts to print
                      in the form of search result
    config          - a configuration dictionary as specified
                      in fkb/config.py
    color           - a boolean, True if color is enabled
    '''
    minLength = 20
    secondaryMinLength = 10
    lenViewID       = max(max([len(str(obj.id)) for obj in searchResult]), 2)

    lenTitle        = max(max([len(obj.title)       for obj in searchResult]), minLength)
    lenCategory     = max(max([len(obj.category)    for obj in searchResult]), minLength)
    lenTags         = max(max([len(obj.tags)        if obj.tags     is not None else 0 for obj in searchResult]), minLength)
    lenAuthor       = max(max([len(obj.author)      if obj.author   is not None else 0 for obj in searchResult]), secondaryMinLength)

    pathHeader = 'Path rel. to ' + config['PATH_FKB_ROOT']

    lenPath         = max(max([len(obj.path)        for obj in searchResult]), max(secondaryMinLength, len(pathHeader)))
    
    header = '   [ {id} ]  {title} {category} {tags} {author} {path}'.format(
        id='ID'.rjust(lenViewID),
        title='Title'.ljust(lenTitle),
        category='Category'.ljust(lenCategory),
        tags='Tags'.ljust(lenTags),
        author='Author'.ljust(lenAuthor),
        path=pathHeader.ljust(lenPath)
    )

    if color:
        print(UND + BOLD + header + RESET)
    else:
        print(header)

    # Print results
    for viewID, obj in enumerate(searchResult):
        tags = obj.tags if obj.tags else ''
        author = obj.author if obj.author else ''

        result_line = '   [ {id} ]  {title} {category} {tags} {author} {path}'.format(
            id=str(viewID).rjust(lenViewID),
            title=obj.title.ljust(lenTitle),
            category=obj.category.ljust(lenCategory),
            tags=tags.ljust(lenTags),
            author=author.ljust(lenAuthor),
            path=obj.path.ljust(lenPath)
        )

        if color and (viewID % 2 == 0):
            print(ALT_BGROUND + result_line + RESET)
        else:
            print(result_line)
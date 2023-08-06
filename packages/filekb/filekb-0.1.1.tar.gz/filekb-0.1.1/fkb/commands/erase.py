# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from fkb.filesystem import *

def Erase(args: Dict[str, str], config: Dict[str, str]):
    '''
    Find an object given args and cat its note to terminal.

    Arguments:

    args            - a dictionary containing the following fields:
                        db          - whether to delete database only
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    if args['db']:
        answer = input(
            'Are you sure you want to erase the FileKB database ? [YES/NO]')
        if answer.lower() == 'yes':
            try:
                RemoveFile(config['PATH_FKB_DB'])
                RemoveFile(config['PATH_FKB_HIST'])
                RemoveDirectory(config['PATH_FKB_DATA'])
                print('FileKB database deleted successfully!')
            except FileNotFoundError:
                pass
    else:
        answer = input(
            'Are you sure you want to erase the whole knowledge base ? [YES/NO]')
        if answer.lower() == 'yes':
            try:
                RemoveDirectory(config['PATH_FKB'])
                print('FileKB knowledge base deleted successfully!')
            except FileNotFoundError:
                pass
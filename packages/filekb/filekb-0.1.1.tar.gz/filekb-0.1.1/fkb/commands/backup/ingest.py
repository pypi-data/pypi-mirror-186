# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
import tarfile
from fkb.filesystem import *

def Ingest(args: Dict[str, str], config: Dict[str, str]):
    '''
    Import a backup of the current fkb knowledge base.
    Arguments:
    args            - a dictionary containing the following fields:
                      file -> a string representing the path to the archive
                        to be imported
    config          - a configuration dictionary containing at least
                      the following keys:
                      PATH_FKB           - the main path of FKB
    '''
    if args['file'].endswith('.tar.gz'):
        answer = input('You are about to import a whole knowledge base '
                       'are you sure you want to wipe your previous '
                       ' fkb data ? [YES/NO]')
        if answer.lower() == 'yes':
            print('Previous fkb knowledge base data wiped...')
            try:
                RemoveDirectory(config['PATH_FKB'])
            except FileNotFoundError:
                pass
            tar = tarfile.open(args['file'], 'r:gz')
            tar.extractall(config['PATH_FKB'])
            tar.close()
            print('fkb archive {fname} imported'.format(fname=args['file']))
    else:
        print('Please provide a file exported through fkb with fkb.tar.gz extension')
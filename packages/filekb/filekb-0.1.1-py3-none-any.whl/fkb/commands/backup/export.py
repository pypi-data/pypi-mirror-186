# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
import time
import tarfile
from pathlib import Path
from fkb.filesystem import *

def Export(args: Dict[str, str], config: Dict[str, str]):
    '''
    Export the entire fkb knowledge base.
    Arguments:
    args:           - a dictionary containing the following fields:
                      file -> a string representing the wished output
                        filename
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_FKB           - the main path of FKB
    '''
    fname = args['file'] or time.strftime('%d_%m_%Y-%H%M%S')
    archive_ext = '.fkb.tar.gz'
    if not fname.endswith(archive_ext):
        fname = fname + archive_ext

    with tarfile.open(fname, mode='w:gz') as archive:
        archive.add(config['PATH_FKB'], arcname='', recursive=True)
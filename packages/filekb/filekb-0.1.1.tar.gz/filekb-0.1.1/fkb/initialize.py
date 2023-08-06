# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

import os
from typing import Dict
from fkb.filesystem import *
from fkb.database import Database
import json

def IsInitialized(config : Dict[str, str]) -> bool:
    '''
    Check whether all fkb files are initialized.
    Arguments:
    config          - a configuration dictionary as specified
                      in fkb/config.py
    Returns:
    A bool representing whether all fkb files are initialized
    '''
    # Check if each path exists already
    for path in [config['PATH_FKB'], config['PATH_FKB_DB'], config['PATH_FKB_DATA'], config['PATH_FKB_HIST'], config['PATH_FKB_CONFIG']]:
        if not os.path.exists(path):
            return False
    
    # All checks passed
    return True

def Initialize(config : Dict[str, str]) -> Database:
    '''
    Initialize the fkb files.
    Arguments:
    config          - a configuration dictionary as specified
                      in fkb/config.py
    Returns:
    A Database object connected to the fkb database
    '''
    if not IsInitialized(config):
        CreateFKBFiles(config)

    # Now that files exist, create DB object and return it
    return Database(config)

def InitializeDB(config : Dict[str, str]) -> Database:
    '''
    Initialize just the fkb database
    Arguments:
    config          - a configuration dictionary as specified
                      in fkb/config.py
    Returns:
    A Database object connected to the fkb database
    '''
    return Database(config)

def CreateFKBFiles(config : Dict[str, str]):
    '''
    Create all the directories and files for fkb.
    Arguments:
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    # Create home directory
    CreateDirectory(config['PATH_FKB'])

    # Create directory to store data files in
    CreateDirectory(config['PATH_FKB_DATA'])

    # If DB file doesn't exist, create it
    if not os.path.exists(config['PATH_FKB_DB']):
        TouchFile(config['PATH_FKB_DB'])

    # If history file doesn't exist, create it
    if not os.path.exists(config['PATH_FKB_HIST']):
        TouchFile(config['PATH_FKB_HIST'])

    # If config file doesn't exist, create it
    if not os.path.exists(config['PATH_FKB_CONFIG']):
        TouchFile(config['PATH_FKB_CONFIG'])
        with open(config['PATH_FKB_CONFIG'], 'w') as configFile:
            json.dump(config, configFile)



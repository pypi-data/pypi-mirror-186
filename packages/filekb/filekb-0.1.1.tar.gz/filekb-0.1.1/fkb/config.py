# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from pathlib import Path
import os
from typing import Dict
import json
from fkb.initialize import CreateFKBFiles

BASE_PATH = Path(Path.home(), '.local', 'share','fkb')

DEFAULT_CONFIG = {
    'PATH_FKB' : str(Path(BASE_PATH)),
    'PATH_FKB_DB' : str(Path(BASE_PATH, 'fkb.db')),
    'PATH_FKB_HIST' : str(Path(BASE_PATH, 'recent.hist')),
    'PATH_FKB_DATA' : str(Path(BASE_PATH, 'data')),
    'PATH_FKB_CONFIG' : str(Path(BASE_PATH, 'config.json')),
    'PATH_FKB_ROOT' : str(Path.home()),
    'EDITOR': os.environ.get('EDITOR', 'nano')
}

def GetConfig() -> Dict[str, str]:
    '''
    Search for the fkb config file.
    First query the location specified by $PATH_FKB env. variable,
    else look in the default ~/.local/share/fkb/ directory,
    else prompt user whether to setup config
    Returns:
    A dict with all the config values
    '''
    configPath = os.environ.get('PATH_FKB')
    
    # Default place to look if env variable is not set
    if configPath is None:
        configPath = DEFAULT_CONFIG['PATH_FKB']

    # If the config file exists, open it and return config
    configFile = str(Path(configPath, 'config.json'))
    if os.path.exists(configFile):
        with open(configFile, 'r') as configFile:
            config = json.load(configFile)
            return config
    else:
        # Config file doesn't exist yet, prompt user to create config
        print('No config file detected.')
        print('If config setup was done before make sure the PATH_FKB environment variable is set to the root data directory of fkb.')
        answer = input('Create config file now? [y/n]')
        if answer.lower() in ['y', 'yes']:
            config = UserPromptCreateConfig()
            CreateFKBFiles(config)
            return config
        else:
            return None

def UserPromptCreateConfig() -> Dict[str, str]:
    '''
    Prompt user to setup config for fkb
    Returns:
    A dict with all the config values
    '''
    config = {}

    print()
    print('Where to store fkb internal data files?')
    print('NOTE: This setting cannot be changed!')
    print('Default: ', DEFAULT_CONFIG['PATH_FKB'])
    print()
    acceptDefault = input('Accept default? [y/n]').lower() in ['y', 'yes']
    if (acceptDefault):
        config['PATH_FKB'] = DEFAULT_CONFIG['PATH_FKB']
    else:
        print()
        pathFKB = input('Input base directory for fkb internal data files')
        config['PATH_FKB'] = pathFKB

        print()
        print('Since the fkb base path was modified, add the following environment variable for fkb to find your config file:')
        print('PATH_FKB = ', pathFKB)
        input('Press enter to confirm you understand the config will not be found without this environment variable.')
    
    # These don't need to be modified by the user.
    config['PATH_FKB_DB'] = str(Path(config['PATH_FKB'],'fkb.db'))
    config['PATH_FKB_HIST'] = str(Path(config['PATH_FKB'],'recent.hist'))
    config['PATH_FKB_DATA'] = str(Path(config['PATH_FKB'],'data'))
    config['PATH_FKB_CONFIG'] = str(Path(config['PATH_FKB'],'config.json'))

    print()
    print('What is the root directory for all tracked fkb files?')
    print('NOTE: This setting cannot be changed!')
    print('Default: ', DEFAULT_CONFIG['PATH_FKB_ROOT'])
    print()
    acceptDefault = input('Accept default? [y/n]').lower() in ['y', 'yes']
    if (acceptDefault):
        config['PATH_FKB_ROOT'] = DEFAULT_CONFIG['PATH_FKB_ROOT']
    else:
        print()
        pathFKB = input('Input root directory for all tracked fkb files')
        config['PATH_FKB_ROOT'] = pathFKB

    print()
    print('Which command line text editor to use?')
    print('Default: ', DEFAULT_CONFIG['EDITOR'])
    print()
    acceptDefault = input('Accept default? [y/n]').lower() in ['y', 'yes']
    if (acceptDefault):
        config['EDITOR'] = DEFAULT_CONFIG['EDITOR']
    else:
        print()
        pathFKB = input('Input which editor to use')
        config['EDITOR'] = pathFKB

    print()
    print('Config finished')
    return config

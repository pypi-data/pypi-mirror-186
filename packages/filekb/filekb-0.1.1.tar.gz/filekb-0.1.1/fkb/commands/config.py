# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
import json
from fkb.filesystem import *

def Config(args: Dict[str, str], config: Dict[str, str]):
    '''
    Handle config given command line arguments

    Arguments:

    args            - a dictionary containing the following fields:
                        None
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    print('The current config file is ', config['PATH_FKB_CONFIG'])
    print()
    modify = input('Would you like to modify the config file? [y/n]').lower() in ['y', 'yes']

    if modify:
        ModifyConfig(config)
        
        # Rewrite changed config
        with open(config['PATH_FKB_CONFIG'], 'w') as configFile:
            json.dump(config, configFile)

def ModifyConfig(config: Dict[str, str]):
    '''
    Handle config given command line arguments

    Arguments:

    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    print()
    print('Directory tostore fkb internal data files: ', config['PATH_FKB'])
    print('This config setting cannot be changed.')
    print()
    input('Press enter to confirm.')
    

    print()
    print('Root directory for all tracked fkb files: ', config['PATH_FKB_ROOT'])
    print('This config setting cannot be changed.')
    print()
    input('Press enter to confirm.')

    print()
    print('Which command line text editor to use?')
    print('Current setting: ', config['EDITOR'])
    print()
    acceptCurrent = input('Accept current? [y/n]').lower() in ['y', 'yes']

    if not acceptCurrent:
        print()
        pathFKB = input('Input which editor to use:\n')
        config['EDITOR'] = pathFKB

    print()
    print('Config finished')

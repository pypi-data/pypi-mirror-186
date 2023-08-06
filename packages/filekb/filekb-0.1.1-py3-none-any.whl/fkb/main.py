# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

import sys

from fkb.config import GetConfig
from fkb.cl_parser import ParseArgs

from fkb.commands.add import Add
from fkb.commands.delete import Delete
from fkb.commands.note.editnote import EditNote
from fkb.commands.note.catnote import CatNote
from fkb.commands.note.deletenote import DeleteNote
from fkb.commands.update import Update
from fkb.commands.search import Search
from fkb.commands.grep import Grep
from fkb.commands.erase import Erase
from fkb.commands.backup.ingest import Ingest
from fkb.commands.backup.export import Export
from fkb.commands.watch import Watch
from fkb.commands.config import Config

NOTE_SUBCOMMANDS = {
    'edit' : EditNote,
    'cat' : CatNote,
    'delete' : DeleteNote,
}

BACKUP_SUBCOMMANDS = {
    'import' : Ingest,
    'export' : Export
}

COMMANDS = {
    'add': Add,
    'delete': Delete,
    'note': NOTE_SUBCOMMANDS,
    'update': Update,
    'list': Search,
    'grep': Grep,
    'erase': Erase,
    'backup' : BACKUP_SUBCOMMANDS,
    'watch': Watch,
    'config': Config,
}

def Dispatch(*args, **kwargs):
    '''
    Dispatch command line action to proper
    fkb function
    '''
    if type(COMMANDS[args[0]['command']]) is not dict:
        return (COMMANDS[args[0]['command']])(*args, **kwargs)
    else:
        return(COMMANDS[args[0]['command']][args[0]['subcommand']])(*args, **kwargs)

def Main():
    args = ParseArgs(sys.argv[1:])
    cmd_params = vars(args)
    
    config = GetConfig()

    if config is None:
        print('No config found, exiting!')
    else:
        Dispatch(cmd_params, config = config)
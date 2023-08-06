# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Sequence
import argparse
import sys
from fkb import __version__

def ParseArgs(args: Sequence[str]) -> argparse.Namespace:
    '''
    Parses command line arguments.
    Arguments:
    args            - args from the command line
    Returns:
    An argparse.Namespace object containing command line args
    '''
    parser = argparse.ArgumentParser(prog='fkb', description='Description')

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__))

    subParsers = parser.add_subparsers(help='commands', dest='command')
    subParsers.required = True

    # Main Commands
    addParser = subParsers.add_parser(
        'add', help='Add an object')
    noteParser = subParsers.add_parser(
        'note', help='Commands related to an object\'s notes')
    listParser = subParsers.add_parser(
        'list', help='Search for knowledge base objects')
    grepParser = subParsers.add_parser(
        'grep', help='Grep through knowledge base objects')
    updateParser = subParsers.add_parser(
        'update', help='Update objects properties')
    deleteParser = subParsers.add_parser(
        'delete', help='Delete objects')
    backupParser = subParsers.add_parser(
        'backup', help='Manage backups of the current knowledge base')
    eraseParser = subParsers.add_parser(
        'erase', help='Erase the entire fkb knowledge base')
    watchParser = subParsers.add_parser(
        'watch', help='Watch a directory for changes and update knowledge base')
    configParser = subParsers.add_parser(
        'config', help='Modify the config files for the knowledge base')
    helpParser = subParsers.add_parser(
        'help', help='Show help of a particular command')

     # Add parser
    addParser.add_argument(
        'file',
        help='Path of the file to add to fkb as object',
        type=str,
        nargs='*'
    )
    addParser.add_argument(
        '-t', '--title',
        help='Title of the added object',
        type=str,
    )
    addParser.add_argument(
        '-c', '--category',
        help='Category associated to the object',
        default='default',
        type=str,
    )
    addParser.add_argument(
        '-g', '--tags',
        help='''
        Tags to associate to the object in the form \"tag1;tag2;...;tagN\"
        ''',
        type=str,
    )
    addParser.add_argument(
        '-a', '--author',
        help='Author of the object',
        type=str,
    )

    # Edit parser
    noteSubParser = noteParser.add_subparsers(help='sub-command help', dest='subcommand')
    noteSubParser.required = True
    noteEditParser = noteSubParser.add_parser('edit', help='Edit note for an object')
    noteDeleteParser = noteSubParser.add_parser('delete', help='Delete note for an object')
    noteCatParser = noteSubParser.add_parser('cat', help='Cat note for an object')
    noteEditParser.add_argument(
         '-i', '--id',
        help='ID of the object',
        dest='viewID',
        type=int,
    )
    noteEditParser.add_argument(
        '-t', '--title',
        help='Title of the object whose note to edit',
        default=None,
        type=str,
    )
    noteEditParser.add_argument(
        '-c', '--category',
        help='Category associated to the object whose note to edit',
        default=None,
        type=str,
    )
    noteDeleteParser.add_argument(
         '-i', '--id',
        help='ID of the object whose note to delete',
        dest='viewID',
        type=int,
    )
    noteDeleteParser.add_argument(
        '-t', '--title',
        help='Title of the object whose note to delete',
        default=None,
        type=str,
    )
    noteDeleteParser.add_argument(
        '-c', '--category',
        help='Category associated to the object whose note to delete',
        default=None,
        type=str,
    )
    noteCatParser.add_argument(
         '-i', '--id',
        help='ID of the object whose note to cat',
        dest='viewID',
        type=int,
    )
    noteCatParser.add_argument(
        '-t', '--title',
        help='Title of the object whose note to cat',
        default=None,
        type=str,
    )
    noteCatParser.add_argument(
        '-c', '--category',
        help='Category associated to the object whose note to cat',
        default=None,
        type=str,
    )

    # List parser
    listParser.add_argument(
        '-p', '--path',
        help='Filter search results by path',
        default=None,
        type=str,
    )
    listParser.add_argument(
        '-t', '--title',
        help='Filter search results by specified title',
        default=None,
        type=str,
    )
    listParser.add_argument(
        '-c', '--category',
        help='Filter search results by specified category',
        default=None,
        type=str,
    )
    listParser.add_argument(
        '-g', '--tags',
        help='''
        Tags associated to the object to search in the form \"tag1;tag2;...;tagN\"
        ''',
        default=None,
        type=str,
    )
    listParser.add_argument(
        '-a', '--author',
        help='Filter search results by specified author',
        default=None,
        type=str,
    )
    listParser.add_argument(
        '-v', '--verbose',
        help='Show additional information for the provided results',
        action='store_true',
        dest='verbose',
        default=False,
    )
    listParser.add_argument(
        '-n', '--no-color',
        help='Enabled no-color mode',
        action='store_true',
        dest='noColor',
        default=False,
    )
    listParser.add_argument(
        '-s', '--strict',
        help='Strict keyword search',
        action='store_true',
        default=False,
    )

    # Grep parser
    grepParser.add_argument(
        'regex',
        help='Filter search results by specified regex',
        type=str,
    )
    grepParser.add_argument(
        '-p', '--path',
        help='Filter search results by path',
        default=None,
        type=str,
    )
    grepParser.add_argument(
        '-t', '--title',
        help='Filter search results by specified title',
        default=None,
        type=str,
    )
    grepParser.add_argument(
        '-c', '--category',
        help='Filter search results by specified category',
        default=None,
        type=str,
    )
    grepParser.add_argument(
        '-g', '--tags',
        help='''
        Tags associated to the object to search in the form \"tag1;tag2;...;tagN\"
        ''',
        default=None,
        type=str,
    )
    grepParser.add_argument(
        '-a', '--author',
        help='Filter search results by specified author',
        default=None,
        type=str,
    )
    grepParser.add_argument(
        '-m', '--show-matches',
        help='Show text matching the regex within the artifact ',
        action='store_true',
        dest='matches',
        default=False,
    )
    grepParser.add_argument(
        '-i', '--case-insensitive',
        help='Perform grep using a case insensitive regex',
        action='store_true',
        dest='caseInsensitive',
        default=False,
    )
    grepParser.add_argument(
        '-v', '--verbose',
        help='Show additional information for the provided results',
        action='store_true',
        dest='verbose',
        default=False,
    )
    grepParser.add_argument(
        '-n', '--no-color',
        help='Enabled no-color mode',
        action='store_true',
        dest='noColor',
        default=False,
    )
    grepParser.add_argument(
        '-s', '--strict',
        help='Strict keyword search',
        action='store_true',
        default=False,
    )

    # Update parser
    updateParser.add_argument(
        'viewID',
        help='ID of the object to update',
        type=int,
    )
    updateParser.add_argument(
        '-t', '--title',
        help='Title to update',
        default=None,
        type=str,
    )
    updateParser.add_argument(
        '-c', '--category',
        help='Category to update',
        default=None,
        type=str,
    )
    updateParser.add_argument(
        '-g', '--tags',
        help='Tags to update in the form \"tag1;tag2;...;tagN\"',
        default=None,
        type=str,
    )
    updateParser.add_argument(
        '-a', '--author',
        help='Author to update',
        default=None,
        type=str,
    )

    # Delete parser
    deleteParser.add_argument(
        '-i', '--id',
        help='ID of the object',
        dest='viewID',
        type=int,
        nargs='*'
    )
    deleteParser.add_argument(
        '-t', '--title',
        help='Title of the object to remove',
        default=None,
        type=str,
    )
    deleteParser.add_argument(
        '-c', '--category',
        help='Category associated to the object to remove',
        default=None,
        type=str,
    )
    deleteParser.add_argument(
        '-f', '--force',
        help='Force removal without asking for confirmation prompt',
        action='store_true',
        default=False,
    )

    # Erase parser
    eraseParser.add_argument(
        '--db',
        help='Only remove fkb database',
        action='store_true',
        dest='db',
        default=False,
    )

    backupSubParser = backupParser.add_subparsers(help='sub-command help', dest='subcommand')
    backupSubParser.required = True
    backupImportParser = backupSubParser.add_parser('import', help='Import a backup of the current knowledge base')
    backupExportParser = backupSubParser.add_parser('export', help='Export a backup of the current knowledge base')

    # Import parser
    backupImportParser.add_argument(
        'file',
        help='Archive to import as knowledge base',
        type=str,
    )

    # Export parser
    backupExportParser.add_argument(
        '-f', '--file',
        help='Name of the exported archive',
        type=str,
        nargs='?'
    )

    # Help parser

    helpParser.add_argument(
        'cmd',
        help='Name of command to get help for',
        nargs='?'
    )

    if len(args) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    parsedArgs = parser.parse_args()
    if parsedArgs.command == 'help':
        if not parsedArgs.cmd:
            parser.print_help(sys.stderr)
        else:
            try:
                subParsers.choices[parsedArgs.cmd].print_help()
            except KeyError:
                print(f'Unknown command name `{parsedArgs.cmd}`')
                print(
                    'Valid commands are: {}'.format(', '.join(subParsers.choices.keys()))
                )
        sys.exit(1)

    return parsedArgs
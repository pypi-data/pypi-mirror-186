# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from typing import Dict
from watchdog.observers import Observer
from watchdog.events import *
from fkb.initialize import Initialize, InitializeDB
from pathlib import Path
from fkb.filesystem import *

def Watch(args: Dict[str, str], config: Dict[str, str]):
    '''
    Start a watch of a directory and propagate changes back to database

    Arguments:
    args            - None
    config          - a configuration dictionary as specified
                      in fkb/config.py
    '''
    Initialize(config)

    watcher = DBWatcher(config['PATH_FKB_ROOT'], config)

    # This runs an infinite loop watching the directory
    watcher.Run()

class KBEventHandler(FileSystemEventHandler):
    '''
    An override class of the watchdog FileSystemEventHandler

    This class will propagate changes to files watched
    by fkb to the database entries.
    '''
    
    def __init__(self, config: Dict[str, str]):
        self.config = config

        # This will be initialized when event handler is started
        self.db = None

    # Nothing to do
    def on_any_event(self, event: FileSystemEvent):
        pass

    # Nothing to do since path didn't change
    def on_closed(self, event: FileClosedEvent):
        # print('Closed File: {}'.format(event.src_path))
        pass
    
    # Nothing to do since new files won't be in fkb
    def on_created(self, event: DirCreatedEvent or FileCreatedEvent):
        # what = 'directory' if event.is_directory else 'file'
        # print('Created {}: {}'.format(what, event.src_path))
        pass

    # React by deleting note
    def on_deleted(self, event: DirDeletedEvent or FileDeletedEvent):
        '''
        React to a deleted file by checking if fkb tracks it
        and if yes, delete it from database

        Arguments:
        event           - a watchdog DirDeletedEvent or FileDeletedEvent
        config          - a configuration dictionary as specified
                        in fkb/config.py
        '''
        srcRelativePath = str(Path(event.src_path).relative_to(self.config['PATH_FKB_ROOT']))

        self.db = InitializeDB(self.config)
        obj = self.db.GetObjectByPath(srcRelativePath)
        
        # If we are tracking the object
        if obj is not None:
            what = 'directory' if event.is_directory else 'file'
            print('Deleted {}: {}'.format(what, event.src_path))
            # File gets removed from tracking
            self.db.DeleteObjectByID(obj.id)
            noteAbsPath = str(Path(self.config['PATH_FKB_DATA'], srcRelativePath)) + '.txt'
            if os.path.exists(noteAbsPath):
                RemoveFile(noteAbsPath)
        pass

    # Nothing to do since path didn't change
    def on_modified(self, event : DirModifiedEvent or FileModifiedEvent):
        # what = 'directory' if event.is_directory else 'file'
        # print('Modified {}: {}'.format(what, event.src_path))
        pass

    # Update internal path for the object if listed in fkb
    def on_moved(self, event : DirMovedEvent or FileMovedEvent):
        '''
        React to a moved file by checking if fkb tracks it
        and if yes, update the database entry

        Arguments:
        event           - a watchdog DirMovedEvent or FileMovedEvent
        config          - a configuration dictionary as specified
                        in fkb/config.py
        '''
        srcRelativePath = str(Path(event.src_path).relative_to(self.config['PATH_FKB_ROOT']))

        self.db = InitializeDB(self.config)
        obj = self.db.GetObjectByPath(srcRelativePath)
        
        # If we are tracking the object
        if obj is not None:
            what = 'directory' if event.is_directory else 'file'
            print('Moved {}: from {} to {}'.format(what, event.src_path, event.dest_path))

            newAbsolutePath = Path(event.dest_path)
            if not newAbsolutePath.is_relative_to(self.config['PATH_FKB_ROOT']):
                # File gets removed from tracking
                self.db.DeleteObjectByID(obj.id)
                noteAbsPath = str(Path(self.config['PATH_FKB_DATA'], srcRelativePath)) + '.txt'
                if os.path.exists(noteAbsPath):
                    RemoveFile(noteAbsPath)
                pass
            else:
                # File is still in FKB_ROOT
                newRelativePath = str(newAbsolutePath.relative_to(self.config['PATH_FKB_ROOT']))
                obj.path = newRelativePath
                self.db.DeleteObjectByID(obj.id)
                self.db.AddObjectWithID(obj.id, obj)

                # Also update the note if there is one
                noteAbsPath = str(Path(self.config['PATH_FKB_DATA'], srcRelativePath)) + '.txt'
                if os.path.exists(noteAbsPath):
                    newNoteAbsPath = str(Path(self.config['PATH_FKB_DATA'], newRelativePath)) + '.txt'
                    MoveFile(noteAbsPath, newNoteAbsPath)
        pass

class DBWatcher:
    '''
    An class to handle setup of watchdog directory watching
    '''

    def __init__(self, path: str, config: Dict[str, str]):
        self.path = path
        self.config = config

        self.event_handler = KBEventHandler(self.config)

        self.observer = Observer()
        self.watch = self.observer.schedule(self.event_handler, self.path, recursive=True)

    def Run(self):
        '''
        Start an infinite loop to watch the directory and
        send events to the EventHandler
        '''
        self.observer.start()

        try:
            # While still observing
            while self.observer.is_alive():
                # Try to join the thread but timeout after 1 second
                self.observer.join(timeout = 1)
        finally:
            # Either on exception or observer stopping stop it and join thread
            self.observer.stop()
            self.observer.join()
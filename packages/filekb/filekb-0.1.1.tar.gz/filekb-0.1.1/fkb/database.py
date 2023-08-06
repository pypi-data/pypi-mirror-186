# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

import sqlite3
from fkb.object import Object
from typing import List, Dict
from pathlib import Path

class Database:
    '''
    A class holding a connection to fkb's sqlite database.
    '''

    DB_CREATE_SQL = '''
                        PRAGMA foreign_keys = ON;
                        CREATE TABLE IF NOT EXISTS objects (
                            id integer PRIMARY KEY,
                            path text NOT NULL,
                            title text NOT NULL,
                            category text NOT NULL,
                            tags text,
                            author text
                        );
                        CREATE TABLE IF NOT EXISTS tags (
                            id integer,
                            tag text,
                            FOREIGN KEY(id)
                            REFERENCES objects(id)
                            ON DELETE CASCADE
                        );
                        '''

    def __init__(self, config: Dict[str, str]):
        '''
        Initialize the database
        Arguments:
        config          - a configuration dictionary as specified
                      in fkb/config.py
        '''
        self.DBPath = str(Path(config['PATH_FKB'], config['PATH_FKB_DB']))
        self.histPath = str(Path(config['PATH_FKB'], config['PATH_FKB_HIST']))

        # Create connection, creates DB if not existant yet
        self.conn = sqlite3.connect(self.DBPath)

        # Run the DB create query to create if not already created
        cur = self.conn.cursor()
        cur.executescript(self.DB_CREATE_SQL)

    def ResetDatabase(self):
        '''
        Drop all tables and reset database
        '''
        cur = self.conn.cursor()
        DB_DROP_TABLE_SQL = '''
                            DROP TABLE IF EXISTS tags;
                            DROP TABLE IF EXISTS objects;
                            '''
        cur.executescript(DB_DROP_TABLE_SQL)
        cur.executescript(self.DB_CREATE_SQL)

    def ContainsObjectByName(self, title: str, category: str) -> bool:
        '''
        A database is not allowed to have 2 objects with the same title and category
        '''
        return (self.GetObjectByName(title, category) is not None)

    def AddObject(self, obj : Object):
        '''
        Add an object to the database
        Arguments:
        obj             - an fkb object
        '''
        if self.ContainsObjectByName(obj.title, obj.category):
            print('Error: an object with title \"' + obj.title + '\" and category \"' + obj.category + '\" already existings in database')
            return

        # Split object tags by the ';' character
        tags_list = []
        if obj.tags:
            tags_list = list(set(obj.tags.split(';')))

        cur = self.conn.cursor()

        DB_INSERT_OBJ_SQL = '''
                            INSERT INTO objects 
                            (path, title, category, tags, author) 
                            VALUES(?, ?, ?, ?, ?)
                            '''
        sql_args = (obj.path, obj.title, obj.category, 
                    obj.tags if obj.tags is not None else '', 
                    obj.author if obj.author is not None else '')

        cur.execute(DB_INSERT_OBJ_SQL, sql_args)
        obj.id = cur.lastrowid

        DB_INSERT_TAG_SQL = '''
                            INSERT INTO tags
                            (id, tag)
                            VALUES(?, ?)
                            '''

        for tag in tags_list:
            sql_args = (obj.id, tag)
            cur.execute(DB_INSERT_TAG_SQL, sql_args)

        self.conn.commit()

    def AddObjectWithID(self, id : int, obj : Object):
        '''
        Add an object to the database with a specified id
        Arguments:
        id              - id of the object
        obj             - an fkb object
        '''
        if self.ContainsObjectByName(obj.title, obj.category):
            print('Error: the specified object already existings in database')
            return
        
        # Split object tags by the ';' character
        tags_list = []
        if obj.tags:
            tags_list = list(set(obj.tags.split(';')))

        cur = self.conn.cursor()

        DB_INSERT_OBJ_SQL = '''
                            INSERT INTO objects 
                            (id, path, title, category, tags, author) 
                            VALUES(?, ?, ?, ?, ?, ?)
                            '''
        sql_args = (obj.id, obj.path, obj.title, obj.category, 
                    obj.tags if obj.tags is not None else '', 
                    obj.author if obj.author is not None else '')

        cur.execute(DB_INSERT_OBJ_SQL, sql_args)

        DB_INSERT_TAG_SQL = '''
                            INSERT INTO tags
                            (id, tag)
                            VALUES(?, ?)
                            '''

        for tag in tags_list:
            sql_args = (obj.id, tag)
            cur.execute(DB_INSERT_TAG_SQL, sql_args)

        self.conn.commit()

    def DeleteObjectByID(self, id : int):
        '''
        Delete an object database with a specified id
        Arguments:
        id              - id of the object
        '''
        cur = self.conn.cursor()

        DB_DELETE_OBJ_SQL = '''
                            DELETE FROM objects WHERE id = ?
                            '''
        cur.execute(DB_DELETE_OBJ_SQL, (id,))
        self.conn.commit()

    def DeleteObjectByName(self, title: str, category: str):
        '''
        Delete an object database with a specified title and category
        Arguments:
        title           - title of the object
        category        - category of the object
        '''
        cur = self.conn.cursor()

        DB_DELETE_OBJ_SQL = '''
                            DELETE FROM objects 
                            WHERE title LIKE ? and category LIKE ?
                            COLLATE NOCASE
                            '''
        cur.execute(DB_DELETE_OBJ_SQL, (title, category))
        self.conn.commit()


    def GetObjectByID(self, id : int) -> Object:
        '''
        Get an object from the database by its ID
        Arguments:
        id              - id of the object
        Returns:
        An fkb object
        '''
        cur = self.conn.cursor()
        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects WHERE id = ?
                         '''
        cur.execute(DB_GET_OBJ_SQL, (id,))
        result = cur.fetchone()
        if result is not None:
            return Object(*result)
        else:
            return None

    def GetObjectByPath(self, path : str) -> Object:
        '''
        Get an object from the database by its path
        Arguments:
        path          - path of the object
        Returns:
        An fkb object
        '''
        cur = self.conn.cursor()
        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects 
                         WHERE path LIKE ?
                         COLLATE NOCASE
                         '''
        cur.execute(DB_GET_OBJ_SQL, (path,))
        result = cur.fetchone()
        if result is not None:
            return Object(*result)
        else:
            return None

    def GetObjectByName(self, title: str, category: str) -> Object:
        '''
        Get an object database with a specified title and category
        Arguments:
        title           - title of the object
        category        - category of the object
        Returns:
        An fkb object
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         WHERE title LIKE ? AND category LIKE ?
                         COLLATE NOCASE
                         '''
        sql_args = (title, category)

        cur.execute(DB_GET_OBJ_SQL, sql_args)
        result = cur.fetchone()
        if result is not None:
            return Object(*result)
        else:
            return None

    def GetObjectsByPath(self, path : str) -> List[Object]:
        '''
        Get all objects which are contained in a path
        Arguments:
        path            - path to filter by
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        # Do a fuzzy search on everything to the right of the base path to match
        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         WHERE path LIKE ?
                         '''
        sql_args = (path + '%',)
        
        cur.execute(DB_GET_OBJ_SQL, sql_args)
        res = [Object(*row) for row in cur.fetchall()]
        return res

    def GetObjectsByAuthor(self, author : str, strict : bool = False) -> List[Object]:
        '''
        Get all objects by a specified author
        Arguments:
        author          - author of the objects
        strict          - whether to exactly match
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         WHERE author LIKE ?
                         COLLATE NOCASE
                         '''
        sql_args = (author if strict else '%' + author + '%',)

        cur.execute(DB_GET_OBJ_SQL, sql_args)
        res = [Object(*row) for row in cur.fetchall()]
        return res

    def GetObjectsByCategory(self, category : str, strict : bool = False) -> List[Object]:
        '''
        Get all objects in a specified category
        Arguments:
        category        - category of the objects
        strict          - whether to exactly match
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         WHERE category LIKE ?
                         COLLATE NOCASE
                         '''
        sql_args = (category if strict else '%' + category + '%',)

        cur.execute(DB_GET_OBJ_SQL, sql_args)
        res = [Object(*row) for row in cur.fetchall()]
        return res

    def GetObjectsByTitle(self, title : str, strict : bool = False) -> List[Object]:
        '''
        Get all objects with a specified title
        Arguments:
        title           - title of the objects
        strict          - whether to exactly match
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         WHERE title LIKE ?
                         COLLATE NOCASE
                         '''
        sql_args = (title if strict else '%' + title + '%',)

        cur.execute(DB_GET_OBJ_SQL, sql_args)
        res = [Object(*row) for row in cur.fetchall()]
        return res

    def GetObjectsByTags(self, tags: List[str], strict : bool = False) -> List[Object]:
        '''
        Get all objects with specified tags
        Arguments:
        tags            - list of tags of the objects
        strict          - whether to exactly match
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM tags
                         WHERE tag LIKE ?
                         COLLATE NOCASE
                         '''

        objectIDSetList = []
        for tag in tags:
            cur.execute(DB_GET_OBJ_SQL, (tag if strict else '%' + tag + '%',))
            objectIDSetList.append({row[0] for row in cur.fetchall()})
        
        if len(objectIDSetList) == 0:
            return []

        resultingSet = objectIDSetList.pop()
        for objectIDSet in objectIDSetList:
            resultingSet.intersection_update(objectIDSet)

        objects = []
        for resultID in resultingSet:
            objects.append(self.GetObjectByID(resultID))
        return objects

    def UpdateObjectByID(self, id : int, object : Object):
        '''
        Update an object's entry in the database
        Arguments:
        id              - id of the object to update
        object          - fkb object with new information 
                          about the object
        '''
        currentObject = self.GetObjectByID(id)
        if currentObject is None:
            return None
        
        updateRecord = (id, object.path,  object.title,
                        object.category,  object.tags, object.author)

        currentRecord = (currentObject.id, currentObject.path, currentObject.title, 
                         currentObject.category, currentObject.tags, currentObject.author)

        # For each attribute check in order if we are updating it, or if we had it, or if it doesn't exist
        newRecord = []
        for i, elem in enumerate(currentRecord):
            if updateRecord[i] is not None:
                newRecord.append(updateRecord[i])
            elif elem is not None:
                newRecord.append(elem)
            else:
               newRecord.append(None)

        self.DeleteObjectByID(id)
        updatedObject = Object(*newRecord)
        self.AddObjectWithID(id, updatedObject)

    def GetObjectsByFilter(self, path: str = None, title: str = None, category: str = None, 
                           tags: List[str] = None, author: str = None, strict: bool = False) -> List[Object]:
        '''
        Get all objects with a generic filter function
        Arguments:
        path            - path to filter by
        title           - title of the objects
        category        - category of the objects
        tags            - list of tags of the objects
        author          - author of the objects
        strict          - whether to exactly match
        Returns:
        A list of fkb objects
        '''
        objectIDSetList = []

        if path is not None:
            objectsByPath = self.GetObjectsByPath(path)
            objectIDSetList.append({obj.id for obj in objectsByPath})
        if title is not None:
            objectsByTitle = self.GetObjectsByTitle(title, strict = strict)
            objectIDSetList.append({obj.id for obj in objectsByTitle})
        if category is not None:
            objectsByCategory = self.GetObjectsByCategory(category, strict = strict)
            objectIDSetList.append({obj.id for obj in objectsByCategory})
        if tags is not None:
            objectsByTag = self.GetObjectsByTags(tags, strict = strict)
            objectIDSetList.append({obj.id for obj in objectsByTag})
        if author is not None:
            objectsByAuthor = self.GetObjectsByAuthor(author, strict = strict)
            objectIDSetList.append({obj.id for obj in objectsByAuthor})

        if len(objectIDSetList) == 0:
            return []

        resultingSet = objectIDSetList.pop()
        for objectIDSet in objectIDSetList:
            resultingSet.intersection_update(objectIDSet)

        objects = []
        for resultID in resultingSet:
            objects.append(self.GetObjectByID(resultID))
        return objects

    def GetAllObjects(self) -> List[Object]:
        '''
        Get all objects from the database
        Returns:
        A list of fkb objects
        '''
        cur = self.conn.cursor()

        DB_GET_OBJ_SQL = '''
                         SELECT * FROM objects
                         '''

        cur.execute(DB_GET_OBJ_SQL)
        res = [Object(*row) for row in cur.fetchall()]
        return res
        
    def WriteSearchToHistoryFile(self, searchResults: List[Object]):
        '''
        Write the search history from a `list` or `grep` call to the history file
        Arguments:
        searchResults   - list of objects in display order
        '''
        with open(self.histPath, 'w') as hfile:
            for viewID, result in enumerate(searchResults):
                hfile.write('{},{}\n'.format(viewID, result.id))
    
    def GetObjectIDFromHistoryViewID(self, viewID: int) -> int:
        '''
        Get an object's ID using it's display ID
        Arguments:
        viewID          - viewID of the object from
                          `list` or `grep`
        Returns:
        An integer representing an object's id
        '''
        with open(self.histPath, 'r') as hfile:
            for line in hfile:
                items = line.split(',')
                if int(items[0]) == viewID:
                    return int(items[1])
        return None

    def GetObjectFromHistoryViewID(self, viewID: int) -> Object:
        '''
        Get an object using it's display ID
        Arguments:
        viewID          - viewID of the object from
                          `list` or `grep`
        Returns:
        An fkb object
        '''
        objID = self.GetObjectIDFromHistoryViewID(viewID)
        return self.GetObjectByID(objID)
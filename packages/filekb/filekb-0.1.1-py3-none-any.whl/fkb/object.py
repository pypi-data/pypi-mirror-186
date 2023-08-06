# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

class Object:
    '''
    A class to hold information about an object
    in the fkb database
    '''

    def __init__(self, id : int, path : str, title : str, category : str, tags : str, author : str):
        self.id = id
        self.path = path
        self.title = title
        self.category = category
        self.tags = tags
        self.author = author
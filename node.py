from os import name
import sys
from types import new_class

class iNode:
    def __init__(self, id, name = None, dataPointer = None, state = True, type = None, next = None, prev = None):
        self.id = id
        self.name = name
        self.dataPointer = dataPointer   #qual data está apontando
        self.state = state #True = Livre
        self.type = type
        self.next = next 
        self.prev = prev
    


class File:
    def __init__(self, name, content = '', owner = 'User', pages = 0, next = None, type = 'file'):
        self.name = name
        self.content = content
        self.owner = owner
        self.pages = pages
        self.next = next
        self.type = type

    def __str__(self):  # retorna uma string quando a classe é printada
      return self.name

class Directory:
    def __init__(self, name, iNodes = [], owner = "User", size = 0, parent = None, type = 'directory'):
        self.name = name
        self.iNodes = iNodes
        self.owner = owner  
        self.size = size
        self.parent = parent
        self.type = type
    def __str__(self):  # retorna uma string quando a classe é printada
      return self.name
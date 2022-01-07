from os import name
import sys

class iNode:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.dataPointer = None   #qual data está apontando
        self.state = True #True = Livre
        self.type = None
        self.next = None 
        self.prev = None
    
    def __str__(self):
        return self.id

class File:
    def __init__(self, name):
        self.name = name
        self.content=''
        self.owner = "Arthur"
        self.pages = 0
        self.next = None     
    
    def __str__(self):  # retorna uma string quando a classe é printada
      return self.name

class Directory:
    def __init__(self, name):
        self.name = name
        self.iNodes = []
        self.owner = "Arthur"  
        self.size = 0
        self.parent = None
    
    def __str__(self):  # retorna uma string quando a classe é printada
      return self.name
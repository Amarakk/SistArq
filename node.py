from os import name
import sys

class iNode:
    def __init__(self, id, type):
        self.id = id
        self.dataPointer = None   #qual data está apontando
        self.state = True #True = Livre
        self.type = type
        self.next = None 
        self.prev = None

class File:
    def __init__(self, name):
        self.name = name
        self.content=''
        self.owner = "Arthur"
        self.pages = 0
        self.next = None
        

class Directory:
    def __init__(self, name):
        self.name = name
        self.iNodes = []
        self.owner = "Arthur"  
        self.size = 0


print(sys.getsizeof("a"))
print(sys.getsizeof("b"))
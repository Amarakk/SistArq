from ctypes import sizeof
import os
import sys
import fileSystem
import node
import json
from types import SimpleNamespace
#31000 blocos de 4kB = 124mB
#cada indice i cabe 4kB !!!
#31000 inodes de 128B = 3.968mB
#cada inode cabe 128B

#newJson = json.dumps(objec.__dict__)                                      -> object -> JSON
#newObject = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))  -> JSON -> object

class VirtualDisk:
    def __init__(self,name):
        self.name = name
        self.diskOn = False
        self.f = open(name,"r")
        self.blocks = [None]*31000
        self.iNodesTable = [] 
        self.toObject()

        if not self.size():
            self.blocks = [None]*31000
            self.iNodesTable = [] 
            self.populateINodesTable()
        self.check()

    def end(self):
        self.f.writelines(self.toJSON())
        self.f.close()

    def populateINodesTable(self):

        for i in range(31000):
            inode = node.iNode(i)
            self.iNodesTable.append(inode)
            
        self.iNodesTable[0].name = "$"
        self.iNodesTable[0].type = "directory"
        self.iNodesTable[0].state = False
        self.blocks[0] = node.Directory("$")
        self.iNodesTable[0].dataPointer = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def toObject(self):
        teste = open('j','w+')
        loadDisk = json.load(self.f)
        for i in loadDisk['iNodesTable']:
            init = node.iNode(**i)
            self.iNodesTable.append(init)
        teste.writelines(str(self.iNodesTable))
        

        for j in loadDisk['blocks']:
            # teste.writelines(str(j))
            # print(j['type'])
            # break
            try:
                if j['type'] == "file":
                    print("file aqui",j['content'])
                    init = node.File(**j)
                    self.blocks.append(init)
                elif j['type'] == "directory":
                    print('diretorio aqui')
                    init = node.Directory(**j)
                    self.blocks.append(init)
                print(str(init))
            except:
                pass
      
        teste.writelines(str(self.blocks))
      
        
        
            
    def check(self):
        return os.path.exists(self.name)
        
    def size(self):
        return os.stat(self.name).st_size
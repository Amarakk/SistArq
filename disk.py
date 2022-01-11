
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
        if self.check():
            self.diskOn = True
            self.f = open(name,'r')
            self.out = open(name+'_att', 'w+')
        else:
            self.f = open(name, 'w+')

        if not self.size():
            self.blocks = [None]*300
            self.iNodesTable = [] 
            self.populateINodesTable()
        else:

            self.blocks = [None]*300
            self.iNodesTable = [] 
            self.toObject()

    def endNew(self):
        self.f.writelines(self.toJSON())
        self.f.close()
        
    def endExisting(self):
        self.out.writelines(self.toJSON())
        self.f.close()
        self.out.close()

    def populateINodesTable(self):

        for i in range(300):
            inode = node.iNode(i)
            self.iNodesTable.append(inode)
            
        self.iNodesTable[0].name = "$"
        self.iNodesTable[0].type = "directory"
        self.iNodesTable[0].state = False
        self.blocks[0] = node.Directory("$")
        self.blocks[0].parent = 0
        self.iNodesTable[0].dataPointer = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def toObject(self):

        loadDisk = json.load(self.f)
        for i in loadDisk['iNodesTable']:
            init = node.iNode(**i)
            self.iNodesTable.append(init)

        
        count = 0
        for j in loadDisk['blocks']:

            try:
                if j['type'] == "file":
                    init = node.File(**j)
                    self.blocks[count] = init
                

                elif j['type'] == "directory":
                    init = node.Directory(**j)
                    self.blocks[count] = init
                print(str(init))
                count += 1
            except:
                self.blocks[count] = None
                count +=1 
      
        
    def check(self):
        print(os.path.exists(self.name))
        return os.path.exists(self.name)
        
    def size(self):
        print(os.stat(self.name).st_size)
        return os.stat(self.name).st_size
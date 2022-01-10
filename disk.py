from ctypes import sizeof
import os
import sys
import fileSystem
import node

#31000 blocos de 4kB = 124mB
#cada indice i cabe 4kB !!!
#31000 inodes de 128B = 3.968mB
#cada inode cabe 128B

class VirtualDisk:
    def __init__(self,name):
        self.name = name
        self.diskOn = False
        self.f = open(name,"w+")
        
        if not self.size():
            self.blocks = [None]*31000
            self.iNodesTable = [] 
            self.populateINodesTable()
        self.check()

    def end(self):
        self.f.writelines(str(self.iNodesTable))
        self.f.writelines('\n')
        self.f.writelines(str(self.blocks))
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
            
    def check(self):
        return os.path.exists(self.name)
        
    def size(self):
        return os.stat(self.name).st_size
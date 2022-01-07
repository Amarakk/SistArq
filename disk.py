from ctypes import sizeof
import os
import sys
#31000 blocos de 4kB = 124mB
#cada indice i cabe 4kB !!!
#31000 inodes de 128B = 3.968mB
#cada inode cabe 128B
class VirtualDisk:
    def __init__(self,name):
        self.name = name
        self.diskOn = False
        self.f = open(name,"wb")
        
        if not self.size():
            self.blocks = [None]*31000
            self.iNodesTable = [None]*31000

        if self.check():
            return "disco inicializado com sucesso"
        else:
            raise "erro na criação do disco"

    def end(self):
        self.f.close()
        

    def check(self):
        return os.path.exists(self.name)
        

    def size(self):
        return os.stat(self.name).st_size

f = open("a","a+")
value = "sting grande"

print(os.stat("a").st_size)

import node
from main import disk

# ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
class fileSystem:

    def __init__(self, disk):
        pass
    
    
    
    #operações em directory
    
    def ls(self,iNode, current):
        pass

    def rmdir(self,iNode):
        pass

    def mkdir(self,nome):
        diretorio = node.Directory
        diretorio.nome = nome
    
   
    def cd(self,Directory,current,next):
        pass

    def mv(self,current,newName):
        pass

    def cp(self,iNode):
        pass

    #operações em File 
    #     
    def touch(self,iNode): #create file || touch file
        pass

    def cat(self,iNode,content): #write ||  cat content >> file
        pass
    
    def echo(self, iNode): #print || echo file
        pass

    def cp(self, baseINode, newINode):
        pass

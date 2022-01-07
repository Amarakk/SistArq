from os import name
import node

# ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
# class fileSystem:

#     def __init__(self, disk):
#         pass
    
#operações em directory

def ls(Node, current):
    pass

def rmdir(iNode):
    pass

def mkdir(name,disk):
    newNode = node.Directory(name)
    disk

def cd(Directory,current,next):
    pass

def mv(current,newName):
    pass

def cp(iNode):
    mkdir()
    pass

#operações em File 
    
def touch(fileName,disk): #create file || touch file
    newNode = node.File(fileName)
    print(newNode)
    disk.blocks.append(newNode)
    
    index = disk.blocks.index(newNode)

    for i in disk.iNodesTable:
        if i.state == True:
            i.dataPointer = index
            i.name = fileName
            i.type = "file"
        break

def cat(fileName,content,): #write ||  cat content >> file
    pass

def echo(fileName, disk): #print || echo fileName
    iNode = next((x for x in disk.iNodeTable if x.name == fileName ), None)
    pass

def cp(baseINode, newINode):
    touch()
    pass
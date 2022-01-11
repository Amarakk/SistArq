from os import name
import node
import disk

# ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
# class fileSystem:

#     def __init__(self, disk):
#         pass
    
#operações em directory

def ls(current :node.Directory, disk):
    inodes = current.iNodes
    for i in inodes:
        print(disk.iNodesTable[i].name, end=' ')
    print("")
        

def rmdir(fileName, currentDir : node.Directory, disk): #validar se esta vazio
    inodes = currentDir.iNode
    for i in inodes:
        if (currentDir.iNodesTable[i].name == remDir and disk.iNodesTable[i].size == 0):
            
            break
    pass

def mkdir(name, currDir,disk):
    newNode = node.Directory(name)
    newNode.parent = currDir

    for j in range(31000):
        if disk.blocks[j] == None:
            disk.blocks[j] = newNode

            break
    
    index = disk.blocks.index(newNode)

    for i in disk.iNodesTable:
        if i.state == True:
            i.dataPointer = index
            i.name = name
            i.type = "directory"
            i.state = False
            currDir.iNodes.append(i.id)
            break



def cd(nextDir,currentDir,disk):
    if nextDir == '..':
        objectDir = [item for item in disk.iNodesTable if item.name == currentDir.parent.name and item.type == "directory"]
        return (disk.blocks[objectDir[0].id], 0)

    objectDir = [item for item in disk.iNodesTable if item.name == nextDir and item.type == "directory"]
    for i in objectDir:
        if i.id in currentDir.iNodes:
            return (disk.blocks[i.id] , 1)


def mv(oldName, newName, currentDir : node.Directory, disk):#renomear
    inodes = currentDir.iNodes
    
    for i in inodes:
        if (disk.iNodesTable[i].name == oldName and (disk.iNodesTable[i].type == "file" or disk.iNodesTable[i].type == "directory")):
            disk.blocks[i].name = newName
            break
        


#operações em File 
    
def touch(fileName : str, currDir : node.Directory, disk): #create file || touch file
    newNode = node.File(fileName)
    
    for j in range(31000):
        if disk.blocks[j] == None:
            disk.blocks[j] = newNode

            break
     
    index = disk.blocks.index(newNode)

    for i in disk.iNodesTable:
        if i.state == True:
            i.dataPointer = index
            i.name = fileName
            i.type = "file"
            i.state = False
            currDir.iNodes.append(i.id)
            break

def cat(fileName, content, currentDir : node.Directory, disk): #write ||  cat content >> file
    inodes = currentDir.iNodes
    for i in inodes:
        if (disk.iNodesTable[i].name == fileName and disk.iNodesTable[i].type == "file"):
            disk.blocks[i].content = content
            break

def echo(fileName, currentDir : node.Directory, disk): #print || echo fileName
    inodes = currentDir.iNodes
    for i in inodes:
        if (disk.iNodesTable[i].name == fileName and disk.iNodesTable[i].type == "file"):
            print(disk.blocks[i].content)
            break

def cp(baseFile, newFile, currentDir : node.Directory, disk):
    touch(newFile, currentDir, disk)

    oldNode = 0
    newNode = 0
    inodes = currentDir.iNodes
    for i in inodes:
        if (disk.iNodesTable[i].name == baseFile and disk.iNodesTable[i].type == "file"):
            oldNode = i
            break

    for j in inodes:
        if (disk.iNodesTable[j].name == newFile and disk.iNodesTable[j].type == "file"):
            newNode = j
            break

    disk.blocks[newNode].content = disk.blocks[oldNode].content

def rm(fileName, currentDir : node.Directory, disk):   #remover arquivo
    inodes = currentDir.iNodes
    for i in inodes:
        if (disk.iNodesTable[i].name == fileName and disk.iNodesTable[i].type == "file"):
            
            disk.iNodesTable[i].name = None
            disk.iNodesTable[i].dataPointer = None   #qual data está apontando
            disk.iNodesTable[i].state = True #True = Livre
            disk.iNodesTable[i].type = None
            disk.iNodesTable[i].next = None 
            disk.iNodesTable[i].prev = None
            disk.blocks[i] = None
            currentDir.iNodes.pop(i)
            
        

    
    

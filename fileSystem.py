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
        

def rmdir(iNode, remDir): #validar se esta vaz
    
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


def mv(current,newName):#renomear
    pass


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

def rm(fileName, currDir):
    
    pass
from os import name
import os
import node
import disk

# ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
# class fileSystem:

#     def __init__(self, disk):
#         pass
    
#operações em directory

def ls(current :node.Directory, disk):
    try:
        inodes = current.iNodes
        for i in inodes:
            print(disk.iNodesTable[i].name, end=' ')
        print("")
    except:
        print("Comando inválido")
def rmdir(dirName, currentDir : node.Directory, disk): #validar se esta vazio
    try:

        objectDir = [item for item in disk.iNodesTable if item.id in currentDir.iNodes and item.name == dirName and item.type == "directory"]


        if objectDir[0].id in currentDir.iNodes:
        
            if len(disk.blocks[objectDir[0].id].iNodes) == 0:

                if disk.iNodesTable[objectDir[0].id].name == dirName:
                    disk.iNodesTable[objectDir[0].id].name = None
                    disk.iNodesTable[objectDir[0].id].dataPointer = None   #qual data está apontando
                    disk.iNodesTable[objectDir[0].id].state = True #True = Livre
                    disk.iNodesTable[objectDir[0].id].type = None
                    disk.iNodesTable[objectDir[0].id].next = None 
                    disk.iNodesTable[objectDir[0].id].prev = None
                    disk.blocks[objectDir[0].id] = None
                    currentDir.iNodes.remove(objectDir[0].id)
                
            else:
                print('Diretorio nao esta vazio')
        else:
            print("diretorio nao encontrado")
    except:
        print("Comando inválido")
        
def mkdir(name, currDir,disk):
    try:
        newNode = node.Directory(name)
        
        parent = [item for item in disk.iNodesTable if item.dataPointer == disk.blocks.index(currDir)]

        for j in range(300):
            if disk.blocks[j] == None:
                disk.blocks[j] = newNode
                break
        
        index = disk.blocks.index(newNode)
        newNode.iNodes = []
        for i in disk.iNodesTable:
            if i.state == True:
                i.dataPointer = index
                i.name = name
                i.type = "directory"
                i.state = False
                currDir.iNodes.append(i.id)
                newNode.parent = parent[0].id

                break
    except:
        print("Comando inválido")

def cd(nextDir,currentDir : node.Directory ,disk):

    try:
        if nextDir == '..':

            objectDir = [item for item in disk.iNodesTable if item.id == currentDir.parent and item.type == "directory"]
            return (disk.blocks[objectDir[0].id], 0)

        objectDir = [item for item in disk.iNodesTable if item.name == nextDir and item.type == "directory"]
        for i in objectDir:
            if i.id in currentDir.iNodes:
                return (disk.blocks[i.id] , 1)
                
    except:
        print("Comando inválido")
        return 0,0
        

def mv(oldName, newName, currentDir : node.Directory, disk):  #renomear

    try:
        inodes = currentDir.iNodes
        
        for i in inodes:
            if (disk.iNodesTable[i].name == oldName and (disk.iNodesTable[i].type == "file" or disk.iNodesTable[i].type == "directory")):
                disk.iNodesTable[i].name = newName
                disk.blocks[i].name = newName
                break
    except:
        print("Comando inválido")
#operações em File 
    
def touch(fileName : str, currDir : node.Directory, disk): #create file || touch file
    try:
        newNode = node.File(fileName)
        
        for j in range(300):
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
    except:
        print("Comando inválido")

def echo(fileName, content, currentDir : node.Directory, disk): #write ||  echo content >> file
    try:
        inodes = currentDir.iNodes
        objectFile = [item for item in disk.iNodesTable if item.id in inodes and item.name == fileName and item.type == "file"]
        previous = objectFile[0]
        #acha o iNode dentro do diretório atual
        
        countBlock = 0
        max = 2
        if len(content) >= max:
            split_string = [content[i:i+max] for i in range(0, len(content), max)]

            firstBlock =  disk.blocks[objectFile[0].id]
            firstBlock.content = split_string[0]
            split_string.pop(0)
            for j in split_string: 
                splitFile = node.File(None)

                for k in range(300):
                    if disk.blocks[k] == None:
                        disk.blocks[k] = splitFile
                        break

                index = disk.blocks.index(splitFile)

                for l in disk.iNodesTable:
                    
                    if l.state == True:
                        l.dataPointer = index
                        l.name = None
                        l.type = "file"
                        l.state = False
                        freeInode = l

                        break
            
                if countBlock == 0:

                    firstBlock.next = freeInode.id
                    nextBlock = disk.blocks[index]
                else:
    
                    nextBlock.next = freeInode.id
                    nextBlock = disk.blocks[index]

                
                previous.next = freeInode.id
                previous = freeInode
                splitFile.content = j
                countBlock += 1


        else: 
            disk.blocks[objectFile[0].id].content = content
    except:
        print("Comando inválido")
        return 0
def cat(fileName, currentDir : node.Directory, disk): #print || cat fileName
    try:
        inodes = currentDir.iNodes
        var = ''
        for i in inodes:
            if (disk.iNodesTable[i].name == fileName and disk.iNodesTable[i].type == "file"):
                contI = i
                while contI:
                    var += disk.blocks[contI].content 
            
                    
                    contI = disk.blocks[contI].next

        return var
    except:
        print("Comando inválido")
        
def cp(baseFile, newFile, currentDir : node.Directory, disk):
    try:
        string = cat(baseFile, currentDir, disk)

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

        echo(newFile, string, currentDir, disk)
    except:
        print("Comando inválido")

def rm(fileName, currentDir : node.Directory, disk):   #remover arquivo
    try:
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
                currentDir.iNodes.remove(i)           
    except:
        print("Comando inválido")
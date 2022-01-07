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
        print(i.name)

def rmdir(iNode): #validar se esta vaz

    pass

def mkdir(currDir, newDir,disk):
    newNode = node.Directory(name)
    newNode.parent = currDir

def cd(Directory,current,next):
    pass

def mv(current,newName):#renomear
    pass


#operações em File 
    
def touch(fileName : str, disk , currDir : node.Directory): #create file || touch file
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

            print(i.id)
        break
    print(currDir.iNodes)

def cat(fileName,content,): #write ||  cat content >> file
    pass

def echo(fileName, disk): #print || echo fileName
    iNode = next((x for x in disk.iNodeTable if x.name == fileName ), None)
    pass

def cp(baseINode, newINode, disk):
    touch()
    pass

def rmFile():
    pass
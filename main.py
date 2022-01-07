from disk import VirtualDisk
import fileSystem
from node import Directory


def main():
    disk1 = VirtualDisk("Disco 1")
    #inicia inodes
    #incia blocos
    reserveWord = ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
    x = True
    currentDir = Directory("root")
    while x:
        command = input().split(' ')
        if (command[0]) in reserveWord:
            if command[0] == reserveWord[0]:
                fileSystem.touch(command[1],disk1)

            elif command[0] == reserveWord[4]:
                fileSystem.cat(command[1],disk1)

            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)
                
            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)

            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)

        else:
            x = False
    for i in range(3):
        print("blocks:", disk1.blocks[i].name)
        print("iNodes:", disk1.iNodesTable[i].id)
main()
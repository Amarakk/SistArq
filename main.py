from disk import VirtualDisk
import fileSystem
from node import Directory

def main():
    disk1 = VirtualDisk("Disco 1")
    #inicia inodes
    #incia blocos
    reserveWord = ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
    x = True
    currentDir = disk1.blocks[0]

    while x:
        print(currentDir,'', end='')
        command = input().split(' ')
        if (command[0]) in reserveWord:
            if command[0] == reserveWord[0]:
                fileSystem.touch(command[1],disk1,currentDir)

            elif command[0] == reserveWord[2]:
                fileSystem.ls(currentDir,disk1)

            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)
                
            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)

            # if command[0] == reserveWord[0]:
            #     fileSystem.touch(command[1],disk1)

        else:
            x = False
            disk1.end()

main()
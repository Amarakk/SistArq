from disk import VirtualDisk
import fileSystem
from node import Directory

def main():
    disk1 = VirtualDisk("Disco 1")
    #inicia inodes
    #incia blocos
    reserveWord = ['touch','ls','mkdir','cd','cat','echo','cp','rm','mv','rmdir','exit']

    x = True

    currentDir = disk1.blocks[0]
    atualPath = '$'
    while x:
        print(atualPath+'/ ', end='')
        command = input().split(' ')
        if (command[0]) in reserveWord:

            if command[0] == reserveWord[0]: #touch
                fileSystem.touch(command[1],currentDir,disk1)

            elif command[0] == reserveWord[1]:  #ls
                fileSystem.ls(currentDir,disk1)

            elif command[0] == reserveWord[2]:  #mdkir
                fileSystem.mkdir(command[1],currentDir,disk1)
                
            elif command[0] == reserveWord[3]:  #c
                oldDir = currentDir.name
                currentDir , direction = fileSystem.cd(command[1],currentDir,disk1)
                if direction == 1:
                    atualPath += '/' + currentDir.name
                else:
                    atualPath = atualPath.translate({ord(i): None for i in "/"+oldDir})

            elif command[0] == reserveWord[4]: #cat 'conteudo legal' >> filename
                content = command[1:-2]
                strContent = ' '.join(content)
                fileSystem.cat(command[-1],strContent, currentDir, disk1)

            elif command[0] == reserveWord[5]:
                fileSystem.echo(command[1],currentDir,disk1)

            elif command[0] == reserveWord[6]:
                fileSystem.cp(command[1], command[2], currentDir, disk1)

            if command[0] == reserveWord[7]: # RM
                fileSystem.rm(command[1],currentDir,disk1)
            
            if command[0] == reserveWord[8]: # RM
                fileSystem.mv(command[1], command[2],currentDir,disk1)

            if command[0] == reserveWord[9]: # RM
                fileSystem.rmdir(command[1],currentDir,disk1)
            
            elif command[0] == reserveWord[-1]:
                if not (disk1.diskOn):
                    disk1.endNew()
                else:
                    disk1.endExisting()
                
                x = False
        else:
            print('Comando inválido')

main()
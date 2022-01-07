from disk import *
def main():
    #inicia inodes
    #incia blocos
    reserveWord = ['touch','ls','rm','echo','cat','cp','mv','mkdir','rmdir','cd']
    x = True
    disk = VirtualDisk("Disco 1")


    while x:
        command = input().split(' ',maxsplit=1)
        print(command)
        if (command[0]) in reserveWord:
            print(disk.size())
        else:
            x = False
    
main()
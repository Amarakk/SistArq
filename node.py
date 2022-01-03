class iNode:
    def __init__(self,name, lenght):
        self.name = name,
        self.lenght = lenght

class File(iNode):
    def __init__(self,name):
        self.conteudo=''
        super().__init__(name)
    
class Folder(iNode):
    def __init__(self,name):
        self.conteudo=[]
        super().__init__(name)

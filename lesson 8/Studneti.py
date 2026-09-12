class Studenti:

    def __init__(self ,name,age, parentName, nivelin,pagesa):
        self.name=name
        self.age=age
        self.parentName=parentName
        self.nivelin=nivelin
        self.pagesa=pagesa


    def vjenNeOre(self):
        print( self.name +" ka marr pjes ne ore")


    def projektiPersonal(self):
        print("projketi final eshte i perfunduar")

    def pagesaEPersonit(self):
        print(self.pagesa)

    def kryerjaEpagese(self):
        self.pagesa= self.pagesa-40

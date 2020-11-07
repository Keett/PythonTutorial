class Araba:
    def __init__(self):
        self.__hiz = 0

    def setHiz(self, hiz):
        self.__hiz = hiz

    def getHiz(self):
        return self.__hiz


x = Araba()
print(x.getHiz())
x.setHiz(100)
print(x.getHiz())

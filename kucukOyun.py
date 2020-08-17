"""
class Insan():
    def __init__(self,isim, guc):
        self.name =isim
        self.damage = guc
    def setName(self,isim):
        self.name = isim

player1 = Insan("Ket", 100)
player1.setName("KübraElif")
print(player1.name)


#-----------------------
class Dusman():
    def __init__(self):
        self.can = 100
        self.guc = 40

    def vur(self,oyuncu):
        oyuncu.can -= self.guc
class Oyuncu():
    def __init__(self):
        self.can = 500
        self.guc = 100

    def vur(self,dusman):
        dusman.can -= self.guc

#tekli örnekleme
player = Oyuncu()

#çoklu örnekleme
dusmanlar = []
for i in range(10):
    dusmanlar.append(Dusman())
print(dusmanlar[3].can)
player.vur(dusmanlar[3])
print(dusmanlar[3].can)
"""


# -----------------------

class Karakter():
    def __init__(self, can, guc, taraf):
        self.can = can
        self.guc = guc
        self.taraf = taraf

    def vur(self, rakip):
        rakip.can -= self.guc


x = Karakter(70, 40, "Düşman")
y = Karakter(100, 50,"Dost")

print("1. Durum", x.can)
y.vur(x)
print("2. Durum", x.can)

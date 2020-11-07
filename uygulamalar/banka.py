from time import sleep
from os import system

class Musteri:
    def __init__(self, isim: str, soyisim: str, id: int, parola: str):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__id = id
        self.__parola = parola
        self.__bakiye = 0

    def getIsim(self):
        return self.__isim

    def getSoyisim(self):
        return self.__soyisim

    def getId(self):
        return self.__id

    def getParola(self):
        return self.__parola

    def getBakiye(self):
        return self.__bakiye

    def setBakiye(self, miktar: float):
        self.__bakiye = miktar


class Banka:
    def __init__(self, isim: str):
        self.__isim = isim
        self.__musteriler = list()

    def paraAktar(self, gonderen: Musteri, alici: Musteri, miktar: float):
        if gonderen in self.__musteriler and alici in self.__musteriler:
            if gonderen.getBakiye() >= miktar:
                gonderen.setBakiye(gonderen.getBakiye() - miktar)
                alici.setBakiye(alici.getBakiye() + miktar)
                print("Gönderildi")
                sleep(1)
            else:
                print("Bakiye yetersiz")
                sleep(1)
        else:
            print("Alıcı veya gönderici bulunamadı..")
            sleep(1)

    def musteriOl(self, isim: str, soyisim: str, id: int, parola: str):
        self.__musteriler.append(Musteri(isim, soyisim, id, parola))

    def paraCek(self, alici: Musteri, neKadar: int):
        if neKadar % 10 != 0:
            print("Ancak 10un katlarını çekebilirsiniz")
            sleep(1)
        else:
            if alici.getBakiye() >= neKadar:
                print("Paranızı alınız")
                sleep(1)
                alici.setBakiye(alici.getBakiye() - neKadar)
            else:
                print("Bakiyeniz yetersiz")
                sleep(1)

    def paraYatir(self, yatirici: Musteri, neKadar: int):
        if neKadar % 5 != 0:
            print("Ancak 5in katlarını yatırabilirsiniz")
            sleep(1)
        else:
            yatirici.setBakiye(yatirici.getBakiye() + neKadar)
            print("Paranız yatırıldı")
            sleep(1)

    def bakiyebilgisi(self, musteri: Musteri):
        print("""
isim : {}
Soyisim: {}
Bakiye : {}
        """.format(musteri.getIsim(), musteri.getSoyisim(), musteri.getBakiye()))

    def musteriVarmi(self, idNo: str, parola: str):
        for i in self.__musteriler:
            if i.getId() == idNo and i.getParola() == parola:
                return i
        return False

    def aliciVarMi(self, idNo: str):
        for i in self.__musteriler:
            if i.getId() == idNo:
                return i
        return False


def Main():
    banka = Banka("Zalım Bank")
    while True:
        system("cls")
        print("""
        [1] Müsteri Ol
        [2] Giriş Yap
        """)
        secim = input("Seçim: ")
        if secim == "1":
            isim = input("İsim")
            soyisim = input("Soyisim")
            idno = input("ID: ")
            parola = input("Parola : ")

            banka.musteriOl(isim, soyisim, idno, parola)
            input("Ana Menüye dönmek için 'enter'a bas")
        elif secim == "2":
            idno = input("ID No'yu girin: ")
            parola = input("Parolanızı girin: ")

            if banka.musteriVarmi(idno, parola):
                musteri = banka.musteriVarmi(idno, parola)
                while True:
                    system("cls")
                    print("""
                    [1] Bakiye Göster
                    [2] Para Yatır
                    [3] Para Çek
                    [4] Para Aktar
                    [Q] ÇIKIŞ                    
                    """)
                    secim2 = input("İşleminiz: ")
                    if secim2 == "1":
                        banka.bakiyebilgisi(musteri)
                        input("Ana Menüye dönmek için 'enter'a bas")
                    elif secim2 == "2":
                        miktar = int(input("Yatırılacak miktarı giriniz: "))
                        banka.paraYatir(musteri, miktar)
                        input("Ana Menüye dönmek için 'enter'a bas")
                    elif secim2 == "3":
                        miktar = int(input("Çekilecek para miktarını giriniz: "))
                        banka.paraCek(musteri, miktar)
                    elif secim2 == "4":
                        aliciIdNo = input("Alıcının id'sini giriniz: ")
                        miktar = int(input("Çekilecek para miktarını giriniz: "))
                        if banka.aliciVarMi(aliciIdNo):
                            alici = banka.aliciVarMi(aliciIdNo)
                            banka.paraAktar(musteri, alici, miktar)
                        else:
                            print("Müşteri bulunamadı")
                            sleep(2)
                    elif secim2 == "Q" or secim2 == "q":
                        print("Ana menüye yönlendiriliyorsunuz...")
                        sleep(2)
                        break
                    else:
                        print("Hatalı Giriş")
                        input("Ana Menüye dönmek için 'enter'a bas")
            else:
                print("Banka kaydı bulunamadı veya parola hatalıdır")
                sleep(2)
        else:
            print("Hatalı Giriş")
            sleep(2)


if __name__ == "__main__":
    Main()

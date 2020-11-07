from datetime import datetime
from random import randint


class Sehir:
    def __init__(self, isim):
        self.__isim = isim
        self.__sicaklik = randint(18, 25)
        self.__havaDurumu = ["Açık", "Kapalı", "Yağmurlu", "Sağanak Yağışlı"][randint(0, 3)]

    def getIsim(self):
        return self.__isim

    def getSicaklik(self):
        return self.__sicaklik

    def getHavaDurumu(self):
        return self.__havaDurumu

    def setSicaklik(self, sicaklik):
        self.__sicaklik = sicaklik

    def setHavaDurumu(self, durum):
        if durum not in ["Açık", "Kapalı", "Yağmurlu", "Sağanak Yağışlı"]:
            pass
        else:
            self.__havaDurumu = durum

    def __str__(self):
        return self.__isim


class Ucus:
    def __init__(self, nereden: Sehir, nereye: Sehir, tarih: datetime):
        self.__nereden = nereden
        self.__nereye = nereye
        self.__tarih = tarih

    def rotar(self, neKadar: int):
        day = self.__tarih.day
        hour = self.__tarih.hour
        minute = self.__tarih.minute
        print("day = {}\nhour = {}\nminute = {}".format(day, hour, minute))

        if (minute + neKadar) >= 60:
            hour += int((minute + neKadar) / 60)
            minute = (minute + neKadar) % 60
            print("ilk if ***************\nhour = {}\nminute={}".format(hour, minute))

            if hour >= 24:
                day += int(hour / 24)
                hour = hour % 24
                print("ikinci if ***************\nday = {}\nhour={}".format(day, hour))

        newDate = datetime(self.__tarih.year, self.__tarih.month, day, hour, minute)
        self.__tarih = newDate

    def getTarih(self):
        return self.__tarih

    def getNereden(self):
        return self.__nereden

    def getNereye(self):
        return self.__nereye


class Yolcu:
    def __init__(self, isim: str, soyisim: str, tc: int):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__tc = tc

    def getIsim(self):
        return self.__isim

    def getSoyisim(self):
        return self.__soyisim

    def getTC(self):
        return self.__tc


class Bilet:
    def __init__(self, yolcu: Yolcu, ucus: Ucus, koltukNumarasi: str):
        self.__yolcu = yolcu
        self.__ucus = ucus
        self.__koltukNumarasi = koltukNumarasi

    def __str__(self):
        string = """
        İsim = \t{}
        Soyisim = \t{}
        T.C. = \t{}
        Uçuş Tarihi = \t{}
        Uçuş Saati = \t{}
        Nereden= \t{}\t\t Hava Durumu = \t{}\t\t Sıcaklık=\t{}
        Nereye = \t{}\t\t Hava Durumu = \t{}\t\t Sıcaklık=\t{}
        Koltuk Numarası = \t{}
        """.format(self.__yolcu.getIsim(), self.__yolcu.getSoyisim(), self.__yolcu.getTC(),
                   self.__ucus.getTarih().date(), self.__ucus.getTarih().time(), self.__ucus.getNereden(),
                   self.__ucus.getNereden().getHavaDurumu(), self.__ucus.getNereden().getSicaklik(),
                   self.__ucus.getNereye(), self.__ucus.getNereye().getHavaDurumu(),
                   self.__ucus.getNereye().getSicaklik(), self.__koltukNumarasi)
        return string

    def getUcus(self):
        return self.__ucus


class Pegasus:
    def __init__(self):
        # iki liste oluşturma şekli
        self.__aktifBiletler = list()
        self.__gecmisBiletler = []
        self.__aktifUcuslar = list()
        self.__gecmisUcuslar = list()

    def biletAl(self, yolcu: Yolcu, ucus: Ucus, koltukNumarasi):
        if ucus in self.__aktifUcuslar:
            bilet = Bilet(yolcu, ucus, koltukNumarasi)
            self.__aktifBiletler.append(bilet)
            return bilet

    def ucusOlustur(self, nereden: Sehir, nereye: Sehir, tarih: datetime):
        ucus = Ucus(nereden, nereye, tarih)
        self.__aktifUcuslar.append(ucus)
        return ucus

    def biletIptal(self, bilet: Bilet):
        if bilet in self.__aktifBiletler:
            self.__aktifBiletler.remove(bilet)
            print("Bilet İptal Edildi")
        else:
            print("Bilet Yok")
    def ucusGerceklesti(self, ucus: Ucus):
        for bilet in self.__aktifBiletler:
            if bilet.getUcus() == ucus:
                self.__aktifBiletler.remove(bilet)
                self.__gecmisBiletler.append(bilet)
        self.__aktifUcuslar.remove(ucus)
        self.__gecmisUcuslar.append(ucus)

    def rotar(self, ucus: Ucus, dakika: int):
        ucus.rotar(dakika)


def Main():
    ilListesi = """
    Adana
    Adıyaman
    Afyonkarahisar
    Ağrı
    Aksaray
    Amasya
    Ankara
    Antalya
    Ardahan
    Artvin
    Aydın
    Balıkesir
    Bartın
    Batman
    Bayburt
    Bilecik
    Bingöl
    Bitlis
    Bolu
    Burdur
    Bursa
    Çanakkale
    Çankırı
    Çorum
    Denizli
    Diyarbakır
    Düzce
    Edirne
    Elazığ
    Erzincan
    Erzurum
    Eskişehir
    Gaziantep
    Giresun
    Gümüşhane
    Hakkari
    Hatay
    Iğdır
    Isparta
    İstanbul
    İzmir
    Kahramanmaraş
    Karabük
    Karaman
    Kars
    Kastamonu
    Kayseri
    Kırıkkale
    Kırklareli
    Kırşehir
    Kilis
    Kocaeli
    Konya
    Kütahya
    Malatya
    Manisa
    Mardin
    Mersin
    Muğla
    Muş
    Nevşehir
    Niğde
    Ordu
    Osmaniye
    Rize
    Sakarya
    Samsun
    Siirt
    Sinop
    Sivas
    Şırnak
    Tekirdağ
    Tokat
    Trabzon
    Tunceli
    Şanlıurfa
    Uşak
    Van
    Yalova
    Yozgat
    Zonguldak"""
    # ilListesi.split("\n") => boşlukları bularak listeye indexli eleman olarak oluşturma işlemi
    sehirler = list()
    for i in ilListesi.split("\n"):
        sehirler.append(Sehir(i))

    yolcu1 = Yolcu("Kübra Elif", "Tozkoparan", 1234589)
    pegasusUcusObjesi = Pegasus()
    ucus1 = pegasusUcusObjesi.ucusOlustur(sehirler[1], sehirler[81], datetime(2020, 6, 28, 23, 30))
    bilet1 = pegasusUcusObjesi.biletAl(yolcu1, ucus1, "F4")
    pegasusUcusObjesi.rotar(ucus1,50)  #    6. ayın 28!i  23.30 du saat 50 dakikalık rotarla 6. ayın 29'u saat 00.20 oldu
    print(bilet1)
    pegasusUcusObjesi.biletIptal(bilet1)


if __name__ == "__main__":
    Main()

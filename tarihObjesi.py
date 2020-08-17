from datetime import date, datetime


class Kitap():
    def __init__(self, yazar:str, isim:str, basimTarihi : date, sayfaSayisi : int):
        self.yazar = yazar
        self.isim = isim
        self.basimTarihi = basimTarihi
        self.sayfaSayisi = sayfaSayisi


x = Kitap("Yazar ismi1", "Kitap İsmi", date(2018, 6, 28), 200)

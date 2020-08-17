class Birey:
    def __init__(self, isim: str, soyisim: str, tcNo: int):
        self.isim = isim
        self.soyisim = soyisim
        self.tcNo = tcNo

class CalismayanBirey(Birey):
    pass

class CalisanBirey(Birey):
    def __init__(self, isim: str, soyisim: str, tcNo: int, idNo: int, maas: int):
        Birey.__init__(self, isim, soyisim, tcNo)
        self.idNo = idNo
        self.maas = maas

    def zam(self,deger):
        self.maas += deger

class Muhendis(CalisanBirey):
    def __init__(self, isim: str, soyisim: str, tcNo: int, idNo: int, maas: int, yazilimDilleri: tuple,
                 yabanciDiller: tuple, bilinenProgramlar: tuple):
        CalisanBirey.__init__(self, isim, soyisim, tcNo, idNo, maas)
        self.yazilimDiller = yazilimDilleri
        self.yabanciDiller = yabanciDiller
        self.bilinenProgramlar = bilinenProgramlar


class Muhasebeci(CalisanBirey):
    def __init__(self, isim: str, soyisim: str, tcNo: int, idNo: int, maas: int, bilinenProgramlar: tuple):
        CalisanBirey.__init__(self, isim, soyisim, tcNo, idNo, maas)
        self.bilinenProgramlar = bilinenProgramlar


x = Muhendis("Mühİsim", "MühSoyisim", 122312, 2, 8000, ("Python", "Java"), ("İngilizce",), ("MS-Office",))
x1 = Muhendis("Mühİsim", "MühSoyisim", 122312, 2, 5000, ("Python", "Java"), ("İngilizce",), ("MS-Office",))
y = Muhasebeci("Muhİsim","MuhSoy",513543,3,5000,("cnr",))

print(x.maas)
print(x1.maas)
x1.zam(1000)
x.zam(500)
print(x.maas, x1.maas)
class Kitap:
    def __init__(self, yazar, isim, sayfaSayisi):
        self.__yazar = yazar
        self.__isim = isim
        self.__sayfaSayisi = sayfaSayisi

    def getYazar(self):
        return self.__yazar

    def getIsim(self):
        return self.__isim

    def getSayfaSayisi(self):
        return self.__sayfaSayisi

    def __str__(self):
        return "Kitabın yazarı: " + self.__yazar + "\n" + \
               "Kitabın ismi: "+self.__isim+"\n"+ \
               "Kitabın sayfa sayısı: "+str(self.__sayfaSayisi)

    def __len__(self):
        return self.__sayfaSayisi

    def __del__(self):
        print("{} yazarına ait olan {} isimli kitap silindi".format(self.__yazar,self.__isim))

x = Kitap("yazarismi", "kitapismi", 105)
print(str(x))
print(len(x))
"""
paint(x) dendiğinde;
<__main__.Kitap object at 0x02F4E6D0> Hataso verir sınıfın objesine ulaşmaya çalıştığı için 
çözmek için __str__ Özel metodu kullanılır
sayısal veri ile string verisi bir arada görüntülenmek istediği için hata alınır 
__str__ metodu override edildi çünkü tanımlı bir __str__ metodu var fakat tanımlı bir 
__len__ metodu yok muhakkak metot yazılmalı.

"""

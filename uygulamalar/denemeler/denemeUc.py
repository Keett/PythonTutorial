import math

secim = True

kenar1 = float(input("üçgenin birinci kenarı: "))
kenar2 = float(input("üçgenin ikinci kenarı: "))


def fonkUcgenCevresi():
    kenar3 = float(input("üçgenin üçüncü kenarı: "))
    sonucCevre = kenar1 + kenar2 + kenar3
    return sonucCevre


def fonkUcuncuKenarBul():
    aci = float(input("İki kenar arası açı: "))
    sonucKenar3 = math.sqrt(pow(kenar1, 2) + pow(kenar2, 2) - 2 * kenar1 * kenar2 * math.cos(math.radians(aci)))
    return sonucKenar3


def fonkUcgenAlanAcili():
    aci = float(input("iki kenar arası açı: "))
    sonucAlan = kenar1 * kenar2 * math.sin(math.radians(aci)) * 1 / 2
    return sonucAlan


def fonkUcgenAlan():
    sonucAlan = kenar1 * kenar2 / 2
    return sonucAlan


def fonkUcKenarliAlan():
    kenar3 = float(input("üçgenin üçüncü kenarını giriniz: "))
    u = (kenar1 + kenar2 + kenar3) / 2
    sonucAlan = math.sqrt(u * (u - kenar1) * (u - kenar2) * (u - kenar3))
    return sonucAlan


def fonkSecim():
    cevap = input("yeni bir hesaplama yapmak ister misiniz evet ise 'E or e' hayır ise 'H or h: ")
    if cevap == "E" or "e":
        main(True)
    elif cevap == "H" or "h":
        main(False)
    else:
        print("Lütfen seçim yapınız...")
        fonkSecim()
    return


def main(secim):
    if secim == True:
        fonkSec = int(input("Üçgenin çevresini bulmak için 1\n"
                            "üçgenin üçüncü kenarını bulmak için 2\n"
                            "üçgenin açıyla alanını bulmak için 3\n"
                            "üçgenin 2 kenarıyla alanını bulmak için 4\n"
                            "üçgenin 3 kenarıyla alanını bulmak için 5\n basınız: "))
        if fonkSec == 1:
            print("Üçgenin cevresi : ", fonkUcgenCevresi())
        elif fonkSec == 2:
            print("üçgenin üçüncü kenarı: ", fonkUcuncuKenarBul())
        elif fonkSec == 3:
            print("üçgenin açılı alanı: ", fonkUcgenAlanAcili())
        elif fonkSec == 4:
            print("üçgenin alanı: ", fonkUcgenAlan())
        elif fonkSec == 5:
            print("üçgenin 3 kenarlı alanı: ", fonkUcKenarliAlan())
        else:
            print("\n Seçim belirlenen aralıkta değil! lütfen yeniden seçim yapınız: ")
            main(True)
        fonkSecim()
    else:
        print("\n programımızı kullandığınız için teşekkürler by KET")
    return


main(secim)

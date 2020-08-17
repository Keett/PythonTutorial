import random
import math
from builtins import map

from termcolor import colored, cprint

# 1- Türk Silahlı Kuvvetleri
# 2- NATO Birliğine ait Silahlı Birim
# 3- Silahsız Araç
# 4- Tehdit Unsurları
# 5- Füze ve benzeri Silah unsurları
sampleArac = [1, 2, 3, 4, 5]
# A = Kara Aracı
# B = Deniz Aracı
# C = Hava Aracı

sampleTur = ["Kara", "Deniz", "Hava"]


def haversine(lon1, lat1, lon2, lat2):
    # Decimal değerleri radyan cinsine çeviriyor
    lon1, lat1, merkezlon, merkezlat = map(math.radians, [lon1, lat1, lon2, lat2])
    # Haversine Formülü
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    # Dünyanın yarıçapı = 6371
    km = 6371 * c
    return km


def tehditOLC():
    arac = random.sample(sampleArac, 1)
    tur = random.sample(sampleTur, 1)
    if arac[0] == 1 or arac[0] == 2 or arac[0] == 3:
        tehditmi = False
    else:
        tehditmi = True
    lon1 = random.uniform(25.0, 45.0)
    lat1 = random.uniform(25.0, 45.0)

    if haversine(lon1, lat1, merkezlon, merkezlat) > 6500 or tehditmi == False:
        if arac[0] == 1:
            cprint(
                "Bu birim Türk Silahlı kuvvetlerine ait {} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'green')
        if arac[0] == 2:
            cprint(
                "Bu birim NATO Birliğine ait {} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'green')
        if arac[0] == 3:
            cprint(
                "Bu birim Silahsız {} aracıdır. TEHDİT DEĞİLDİR.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'green')
        if arac[0] == 4:
            cprint("Bu cismin uzaklığı tehdit oluşturmayacak düzeydedir.", 'green')
            cprint(
                "Bu birim tanımlanamamıştır, {} aracıdır. TEHDİT OLABİLİR.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'orange')
        if arac[0] == 5:
            cprint(
                "Bu birim bir silahtır.{} dan/den gelmektedir. ACİL DURUM.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'red')
    else:
        if arac[0] == 4:
            cprint(
                "Bu birim tanımlanamamıştır, {} aracıdır. TEHDİT OLABİLİR.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'red')
            return 1
        if arac[0] == 5:
            cprint(
                "Bu birim bir silahtır.{} dan/den gelmektedir. ACİL DURUM.\nTespit edilen cismin kordinatları {},{} \nAramızdaki uzaklık: {}".format(
                    str(tur[0]), lon1, lat1, haversine(lon1, lat1, merkezlon, merkezlat)), 'red')
            return 1


print("tanımlamalar 2")
acildurum = 0
merkezlon = 39.9333635
merkezlat = 32.8597419
for i in range(0, 15, 1):
    cprint("Durum {}".format(i + 1), 'blue')
    cprint("\n------------------------------------------------------------------------\n", 'blue')
    if tehditOLC() == 1:
        acildurum = acildurum + 1
    cprint("\n------------------------------------------------------------------------\n", 'blue')
print("{} cisimden tehdit olabilecek {} cisim tespit edilmiştir.".format(15000, acildurum))

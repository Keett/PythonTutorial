import random
yukSample = [5,10,15,20,25,30,35,40,45,50,55,7,5,28,35]
yukSayisi = random.randint(0,100)
yukler = []

for i in range(0,yukSayisi,1):
    yukler.append(random.sample(yukSample,1))
aracSayisi = 1
aracMevcutKilo = 0
i = 0
print("Yük Sayısı: ",yukSayisi)
print("Yükler ",yukler)

while i<(yukSayisi-1):
    TMP = aracMevcutKilo + int(yukler[i][0])
    if TMP <= 300:
        aracMevcutKilo = TMP
        i+=1
    else:
        aracSayisi+=1
        aracMevcutKilo = 0
if aracMevcutKilo>0:
    aracSayisi +=1
    aracMevcutKilo = 0
print("Toplam kullanılan araç sayısı = {}".format(aracSayisi))
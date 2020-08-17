import random

anaDizi = []
siralanmisDizi = []
diziElemanSayisi = int(random.uniform(1,10))

#dizinin içini rastgale doldur
def diziDoldur(dizi = []):
    for i in range(-1,diziElemanSayisi,1):
        dizi.append(int(random.uniform(0,50)))
    return dizi

print(diziDoldur(anaDizi))
#anaDizi artık dolduruldu print ifadesyle bütün değişkenler geldi istenildiği gibi atama yapılıyor
siralanmisDizi = anaDizi

def selectionSort(siralanmisDizi):
    adim = 1
    for i in range(len(siralanmisDizi)-1):
        for j in range(i+1, len(siralanmisDizi)):
            print("Adım : ",adim, "(giriş) | i = ", i , " | j = ", j , "| ",siralanmisDizi)
            if siralanmisDizi[j] < siralanmisDizi[i]:
                temp = siralanmisDizi[i]
                siralanmisDizi[i] = siralanmisDizi[j]
                siralanmisDizi[j] = temp
            print("Adım: ", adim, "(çıkış) | i = ",i," | j= ",j, " | ",siralanmisDizi)
            adim += 1
    print("\n Sıralanmış dizi: ",end="")
    for i in range(len(siralanmisDizi)):
        if i+1 == len(siralanmisDizi):
            print(siralanmisDizi[i], end="")
        else:
            print(siralanmisDizi[i], end=",")

selectionSort(siralanmisDizi)
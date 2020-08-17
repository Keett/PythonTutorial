def basamakDegeriBul(sayi):
    sayac = 1
    while sayi >=10:
        sayac += 1
        sayi /= 10
    return sayac
sayi = int(input("lütfen bir sayı giriniz: "))
print("girdiğiniz sayının basamak değeri", basamakDegeriBul((sayi)))
print()

sayi = int(input("karakökü alınacak sayı:"))
e = float(input("doğruluk seviyesi (ne kadar küçükse o kadar iyi"))
x = sayi
y = 1
while(x-y >e):
    x = (x+y)/2
    y = sayi/x
print("{}sayısının karakökü = {}, doğruluk seviyesi={}".format(sayi,x,e))

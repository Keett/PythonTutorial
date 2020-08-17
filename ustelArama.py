import random
def BinarySearch (Dizi, sol, sag, aranan):
    if sag >= sol:
        ortanca = sol + (sag - sol)//2
        ortanca = int(ortanca)
        if Dizi[ortanca] == aranan:
            return ortanca
        elif Dizi[ortanca] > aranan:
            return BinarySearch(Dizi, sol, ortanca-1, aranan)
        else:
            return BinarySearch(Dizi, ortanca+1, sag, aranan)
    else:
        return -1

def ExponentialSearch(Dizi, n, aranan):
    if Dizi[0] == aranan:
        return 0
    i = 1
    while i < n and Dizi[i] <= aranan:
        i = i * 2
    return BinarySearch( Dizi, i / 2, min(i, n), aranan)

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
n = len(Dizi)
index = ExponentialSearch(Dizi,len(Dizi)-1,aranan)
if index > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}".format(Dizi,aranan,index))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı".format(Dizi,aranan))
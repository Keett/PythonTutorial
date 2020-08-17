import random
def linearSearch(dizi, aranan):
    for i in range(len(dizi)):
        if dizi[i] == aranan:
            return i
    return -1
dizi = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
randomSample = random.sample(dizi,1)
print("Random Sample: ",randomSample)
aranan = int(randomSample[0])

index = linearSearch(dizi,aranan)
if index > -1:
    print("dizi:{}\nAranan İfade = {}\nİfadenin İndexi = {}".format(dizi,aranan,index))
else:
    print("Dizi ={}\nAranan İfade = {}\nİfade bulunamadı".format(dizi,aranan))


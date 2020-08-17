"""
sayi = int(input("hangi sayının mükemmel sayı olduğunu bulmak istiyorsunuz: "))
t = 0
for i in range(1,sayi):
    if sayi%i == 0:
        print(i)
        t+=i
if sayi ==t:
    print("{} mükemmel sayıdır.".format(sayi))
else:
    print("{} mükemmmel sayı değildir.".format(sayi))
####################################################################################
def fibonacci(sayi):
    if sayi<0:
        print("sayı 0dan küçük")
    elif sayi == 1:
        return 0
    elif sayi == 2:
        return 1
    else:
        return fibonacci(sayi -1) + fibonacci(sayi-2)
"""
k = int(input("kaçıncı elemanı bulunacak"))
#print("{}. fibonacci elemanı  = {}".format(k,fibonacci(k)))

print("{} sayısının tam bölenleri: ".format(k))
print("1", end="")
for i in range(2,k+1):
    if k%i == 0:
        print(", {}".format(i),end="")

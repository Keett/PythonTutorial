def topla(*args):
    toplam = 0
    for i in args:
        toplam +=i
    return toplam

print(topla(1,2,3,5,3,5,36346,36346,2451351,56))

x = 5
y = x
print("x : {} ve xin id'si : {}\ny: {} ve ynin id'si:{}".format(x,id(x),y,id(y)))
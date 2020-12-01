# value types => string, number

"""
#--------------1
x = 5
print(id(x))
x = 6
print(x)
print(id(x))
#--------------2
x = 5
y = x
print(x,y)
print(id(x) == id(y))

x = 6
print(x,y)
print(id(x) == id(y))
#--------------3
x = 5
y = 25
print("id x: ",id(x))
print("id y: ",id(y))

x = y
print(x,y)
print("id x: ",id(x))
print("id y: ",id(y))
print(id(x) == id(y))

y = 10
print("id y: ",id(y))
print(x,y)
print(id(x) == id(y))
#--------------
"""
# reference types => list, class
"""
a = ["apple","banana"]
b = ["apple","banana"]
a = b
b[0] = "grape"
print(a, b)
#--------------
x = ["apple","banana"]
y = x
print(x,y)
print(id(x) == id(y))
print("x in 0. index id:", id(x[0]))
x[0] = 6  => direk değişkenin adresi değil o adres içindeki listenin 0. indexinin adresi değişir
print(x,y)
print(id(x) == id(y))
print("x in 0. index id:", id(x[0]))
#--------------
x = ["apple","banana"]
y = x
print(x,y)
print(id(x) == id(y))
x = 6  => direk değişkenin adresi değişir
print(x,y)
print(id(x) == id(y))
#--------------
x = ["apple","banana"]
y = x.copy()
print(x,y)
print(id(x) == id(y))
y[0] = 6
print(x,y)
print(id(x) == id(y))
"""



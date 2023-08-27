fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])
# Her elemandan sadece bir tane olabilir apple tekrar eklenmedi zaten vardı...
fruits.remove('mango')
fruits.discard('apple')
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)             #[1,2,5,4,4,2,1]
# print(set(myList))        #[1,2,5,4]
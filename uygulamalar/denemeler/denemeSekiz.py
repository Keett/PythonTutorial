class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        x = 101
        y = 0

        for item in self.__elements:
            if item < x:
                x = item
            if item > y:
                y = item
        self.maximumDifference = y - x
# End of Difference class
   
_ = input("Liste kaç elemanlı ?? ")
a = [int(e) for e in input("Liste elemanlarını arada bir boşlık bırakarak giriniz ").split(' ')]

d = Difference(a)
d.computeDifference()

print("Max Difference: ",d.maximumDifference)

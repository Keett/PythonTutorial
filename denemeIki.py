import math
kenar1 = float(input("birinci keanrı giriniz: "))
kenar2 = float(input("ikinci kenarı giriniz: "))
aci = float(input("Kenarlar arası açıyı giriniz: "))
alan = round(kenar1 * kenar2 * math.sin(math.radians(aci)) * 1/2)
print("Üçgenin bir kenarı {} ve\ndiğer kenarı {} ve\naradaki açısı {} olan üçgenin\n"
      "alanı {}".format(kenar1,kenar2,aci,alan))
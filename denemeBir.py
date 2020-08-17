import math
yaricap = float( input("Dairenin yarıçapını giriniz..."))
cevre = 2*math.pi*yaricap
cevre = round(cevre,3)
print("yarıçapı {} olann dairenin cevresi = {}".format(yaricap,cevre))
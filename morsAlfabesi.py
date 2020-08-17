# Mors Alfabesi
# A = .-
# B = -...
# C = -.-.
# D = -..
# E = .
# F = ..-.
# G = --.
# H = ....
# I = ..
# J = .---
# K = -.-
# L = .-..
# M = --
# N = -.
# O = ---
# P = .--.
# Q = --.-
# R = .-.
# S = ...
# T = -
# U = ..-
# V = ...-
# W = .--
# X = -..-
# Y = -.--
# Z = --..
# 0 = -----
# 1 = .----
# 2 = ..---
# 3 = ...--
# 4 = ....-
# 5 = .....
# 6 = -....
# 7 = --...
# 8 = ---..
# 9 = ----.
def MorsAlfabesiDonustur():
    yazi = input('Mors alfabesi ile yazdırmak istediğiniz mesaj nedir? \n')
    yazi = yazi.upper()
    for i in range(len(yazi)):
        if yazi[i] == 'A':
            print('.-', end='')
        elif yazi[i] == 'B':
            print('-...', end='')
        elif yazi[i] == 'C':
            print('-.-.', end='')
        elif yazi[i] == 'D':
            print('-..', end='')
        elif yazi[i] == 'E':
            print('.', end='')
        elif yazi[i] == 'F':
            print('..-.', end='')
        elif yazi[i] == 'G':
            print('..-', end='')
        elif yazi[i] == 'H':
            print('....', end='')
        elif yazi[i] == 'I':
            print('..', end='')
        elif yazi[i] == 'J':
            print('.---', end='')
        elif yazi[i] == 'K':
            print('-.-', end='')
        elif yazi[i] == 'L':
            print('.-..', end='')
        elif yazi[i] == 'M':
            print('--', end='')
        elif yazi[i] == 'N':
            print('-.', end='')
        elif yazi[i] == 'O':
            print('---', end='')
        elif yazi[i] == 'P':
            print('.--.', end='')
        elif yazi[i] == 'Q':
            print('--.-', end='')
        elif yazi[i] == 'R':
            print('-.-.', end='')
        elif yazi[i] == 'S':
            print('...', end='')
        elif yazi[i] == 'T':
            print('-', end='')
        elif yazi[i] == 'U':
            print('..-', end='')
        elif yazi[i] == 'V':
            print('...-', end='')
        elif yazi[i] == 'W':
            print('.--', end='')
        elif yazi[i] == 'X':
            print('-..-', end='')
        elif yazi[i] == 'Y':
            print('-.--', end='')
        elif yazi[i] == 'Z':
            print('--..', end='')
        elif yazi[i] == '0':
            print('-----', end='')
        elif yazi[i] == '1':
            print('.----', end='')
        elif yazi[i] == '2':
            print('..---', end='')
        elif yazi[i] == '3':
            print('...--', end='')
        elif yazi[i] == '4':
            print('....-', end='')
        elif yazi[i] == '5':
            print('.....', end='')
        elif yazi[i] == '6':
            print('-....', end='')
        elif yazi[i] == '7':
            print('--...', end='')
        elif yazi[i] == '8':
            print('---..', end='')
        elif yazi[i] == '9':
            print('----.', end='')
        else:
            print('', end='')
        print(' ', end='')
    print("")
    secim = input("Yeniden denemek ister misiniz(Evet = e , Hayır = h):")
    secim = secim.upper()
    if secim == "E":
        MorsAlfabesiDonustur()
    elif secim == "H":
        print("Bizi tercih ettiğiniz içi teşekkürler ")


sol = "E"
sag = "T"
solSol = ["I", "S", "R", "H", "F", "L", "P", 5]
solSag = ["A", "U", "W", "V", "J", 4, 3, 2, 1]
sagSol = ["N", "D", "G", "B", "C", "Z", 6, 7, 8, 9]
sagSag = ["M", "K", "O", "X", "Y", "Q", 0]

def TurkceyeCevir():
    yazi = input("Dönüştürülecek mors yazısı :\n")
    yazi = yazi.upper()
    nokta = 0
    cizgi = 0
    for i in range(len(yazi)):
        if yazi[i] == ".":
            if nokta > 0 or cizgi > 0:
                if temp == sol or temp == solSol or temp == solSag:
                    temp = solSol
                if temp == sag or temp == sagSol or temp == sagSag:
                    temp = sagSol
                nokta += 1
                print("burada ve i değeri = {} ve temp = {}, nokta = {}, çizgi = {}".format(i, temp, nokta,cizgi))
            else:
                temp = sol
                nokta +=1
                print("burada ve i değeri = {} ve temp = {}, nokta = {}, çizgi = {}".format(i, temp, nokta,cizgi))
        if yazi[i] == "/":
            print(temp)
            if temp == solSol:
                if len(yazi) == 3:
                    return temp[0]
                elif len(yazi) == 4:
                    if nokta == 3:
                        return temp[1]
                    elif nokta == 2:
                        return temp[2]
                elif len(yazi) == 5:
                    if nokta == 4:
                        return temp[3]
                    elif nokta == 3:
                        if yazi =="..-./" :
                            return temp[4]
                        else:
                            return temp[5]
                    elif nokta == 2:
                        return temp[6]
                    elif nokta == 5:
                        return temp[7]
            elif temp == solSag:
                if len(yazi) == 3:
                    return temp[0]
                elif len(yazi) == 4:
                    if nokta == 2:
                        return temp[1]
                    else:
                        return temp[2]
                elif len(yazi) == 5:
                    if nokta == 3:
                        return temp[3]
                    else:
                        return temp[4]
                elif len(yazi) == 6:
                    if nokta == 4:
                        return temp[5]
                    elif nokta == 3:
                        return temp[6]
                    elif nokta == 2:
                        return temp[7]
                    else:
                        return temp[8]
            elif temp == sagSol:
                if len(yazi) == 3:
                    return temp[0]
                elif len(yazi) == 4:
                    if nokta == 2:
                        return temp[1]
                    else:
                        return temp[2]
                elif len(yazi) == 5:
                    if nokta == 3:
                        return temp[3]
                    if nokta == 4:
                        if yazi =="-.-./":
                            return temp[4]
                        else:
                            return temp[5]
                elif len(yazi) == 6:
                    if nokta == 4:
                        return temp[6]
                    elif nokta == 3:
                        return temp[7]
                    elif nokta == 2:
                        return temp[8]
                    else:
                        return temp[9]
            elif temp == sagSag:
                if len(yazi) == 3:
                    return temp[0]
                elif len(yazi) == 4:
                    if nokta == 1:
                        return temp[1]
                    else:
                        return temp[2]
                elif len(yazi) == 5:
                    if nokta == 2:
                        return temp[3]
                    elif nokta == 1:
                        if yazi == "-.--" :
                            return temp[4]
                        else:
                            return temp[5]
                else:
                    return temp[6]

            temp = ""
            nokta = 0
            cizgi = 0

        if yazi[i] == "-":
            if cizgi > 0 or nokta > 0 :
                if temp == sag or temp == sagSol or temp == sagSag:
                    temp = sagSag
                if temp == sol or temp == solSol or temp == solSag:
                    temp = solSag
                cizgi += 1
                print("burada ve i değeri = {} ve temp = {}, nokta = {}, çizgi = {}".format(i, temp, nokta,cizgi))
            else:
                temp = sag
                cizgi +=1
                print("burada ve i değeri = {} ve temp = {}, nokta = {}, çizgi = {}".format(i, temp, nokta, cizgi))

print(TurkceyeCevir())
# MorsAlfabesiDonustur()

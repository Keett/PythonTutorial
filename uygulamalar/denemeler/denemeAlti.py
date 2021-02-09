import math
import os
import random
import re
import sys

n = int(input("Sayı gir"))
temp = []
for i in range(0, n):
    s = input("diziye eklenen elemanı gir")
    temp.append(s)
    print(temp)

for i in range(0, n):
    for j in range(0, len(temp[i]), 2):
        print(temp[i][j], end='')
    print(end=' ')
    for j in range(1, len(temp[i]), 2):
        print(temp[i][j], end='')
    print("")

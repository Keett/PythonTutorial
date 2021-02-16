import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    arr=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    for i in range(0,6):
        for j in range(0,6):
            print(arr[i][j],end=" ")
        print("\n",arr[i][j])
        
    sum = 0
    tarr = []
    for l in range(0,4):
        for k in range(0,4):
            for i in range(l,l+3):
                for j in range(k,k+3):
                    if i == l+1 and ( j == k or j == k+2):
                        continue
                    else:
                        sum += arr[i][j]
            tarr.append(sum)
            sum = 0
    
    print(max(tarr))
        
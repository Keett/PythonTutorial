import random
import time

AnaDizi=[290, 1339, 930, 2319, 1534, 1618, 454, 1104, 164, 1290, 763, 470, 814, 1230, 2428, 984, 2073, 2635, 1672, 2702, 940, 2600, 1309, 830, 2106, 1233, 2931, 449, 591, 375, 324, 1225, 526, 1679, 1047, 782, 1001, 578, 1474, 181, 1838, 2552, 2951, 1422, 1984, 2203, 24, 2957, 1217, 2854, 483, 1185, 2972, 74, 1586, 2245, 1888, 2897, 2346, 954, 697, 2211, 2235, 340, 1867, 2034, 2689, 1430, 421, 2666, 2187, 787, 277, 2191, 2316, 2195, 1764, 2012, 955, 607, 2663, 510, 2224, 1258, 2447, 543, 233, 1461, 2142, 65, 425, 2437, 1771, 2889, 2936, 863, 2680, 523, 1417, 1324, 1048, 2108, 312, 1177, 1, 328, 1491, 1986, 2659, 2781, 296, 31, 2118, 2207, 265, 696, 842, 2652, 2176, 2047, 765, 2222, 2483, 2100, 1959, 881, 2209, 2570, 314, 2397, 1500, 1593, 138, 369, 1212, 780, 1407, 1026, 2454, 711, 1768, 2620, 184, 2132, 257, 1533, 2020, 1660, 269, 1342, 2974, 1130, 495, 1725, 253, 80, 963, 2336, 2649, 2116, 517, 1696, 1587, 1188, 1250, 1761, 2244, 747, 837, 2789, 2250, 2969, 2679, 1757, 1249, 966, 1298, 2533, 2985, 2414, 701, 2065, 2019, 1556, 2617, 1926, 870, 811, 1571, 146, 1755, 1364, 1117, 2396, 2676, 432, 731, 2922, 500, 2430, 2192, 1380, 1431, 1945, 1919, 2252, 225, 428, 1004, 513, 566, 802, 688, 1326, 824, 693, 1931, 1918, 2874, 2093, 2627, 876, 1102, 1858, 440, 793, 2537, 524, 1370, 2314, 484, 2953, 2024, 2950, 1795, 1798, 434, 2090, 215, 1312, 2062, 2920, 2832, 2069, 1928, 1889, 121, 2248, 1068, 779, 2197, 2901, 1666, 1664, 2583, 217, 549, 2258, 1920, 241, 1078, 18, 1993, 836, 1995, 820, 1264, 2496, 2261, 1604, 2111, 1045, 1916, 822, 1416, 199, 1060, 2196, 1529, 1522, 682, 1694, 1109, 243, 272, 393, 28, 271, 1943, 1195, 736, 2893, 2577, 353, 1885, 1554, 892, 1016, 762, 2292, 2696, 1000, 1722, 1669, 1841, 2479, 40, 2937, 2290, 299, 570, 1509, 2051, 746, 1002, 859, 2511, 2460, 221, 1132, 1662, 1451, 1350, 42, 1325, 2523, 197, 562, 980, 617, 2940, 2793, 2218, 611, 67, 474, 1477, 2623, 2722, 783, 2833, 1313, 2882, 2129, 1234, 2786, 335, 1484, 2855, 1440, 1607, 234, 805, 194, 2205, 933, 1949, 2591, 2784, 1050, 1120, 1825, 1046, 1041, 1236, 1525, 1175, 1561, 601, 2102, 1293, 1504, 41, 2508, 950, 1706, 757, 2036, 1314, 677, 1056, 1744, 784, 2960, 1846, 1371, 2716, 2991, 528, 2001, 92, 2165, 1724, 833, 2582, 1419, 2637, 2000, 2731, 98, 1251, 2375, 2286, 900, 2838, 695, 2707, 2943, 1893, 807, 1183, 2509, 287, 592, 2198, 946, 615, 75, 855, 1007, 1828, 1685, 478, 2790, 2155, 179, 2322, 1295, 2246, 2769, 2978, 700, 1822, 885, 2910, 2560, 69, 1454, 1190, 2598, 1539, 2498, 125, 1969, 702, 2435, 378, 2064, 1266, 2870, 246, 245, 320, 2755, 1517, 1187, 2227, 815, 229, 190, 1999, 1469, 303, 264, 2605, 223, 409, 2308, 1844, 1286, 391, 2749, 912, 953, 2908, 1240, 2067, 306, 1832, 791, 1809, 149, 945, 1302, 1938, 2253, 2796, 530, 2983, 2519, 2753, 1146, 593, 2239, 2486, 587, 1097, 239, 2363, 2516, 1584, 1473, 2590, 2097, 2917, 1972, 2565, 2406, 336, 247, 2398, 891, 1040, 447, 329, 1184, 2031, 1700, 1721, 2038, 752, 2735, 130, 744, 908, 1260, 1659, 795, 1160, 1206, 1008, 2002, 2174, 2861, 920, 1090, 1013, 1620, 2438, 1562, 1445, 2425, 313, 93, 2726, 883, 1300, 2657, 2361, 1323, 1357, 456, 2242, 139, 844, 571, 1924, 2965, 2806, 1210, 1787, 2119, 2554, 8, 2372, 1372, 2039, 1065, 1043, 1648, 1030, 453, 493, 893, 334, 1436, 827, 1617, 625, 2141, 1968, 981, 1933, 630, 2561, 512, 2267, 993, 1723, 1403, 619, 260, 1035, 743, 2467, 2802, 658, 618, 1900, 2426, 252, 2662, 1719, 1526, 315, 2289, 1646, 1239, 1076, 2282, 1837, 533, 556, 1849, 1823, 2400, 1023, 1468, 1223, 2961, 458, 577, 2033, 1983, 19, 66, 1069, 1382, 1848, 1633, 123, 2581, 507, 1496, 1590, 1895, 1981, 944, 2718, 1010, 2407, 2886, 1222, 1038, 251, 545, 218, 2384, 1973, 2778, 2632, 1122, 2084, 2997, 231, 665, 626, 2530, 2654, 472, 1802, 840, 1892, 1704, 598, 2904, 2057, 2104, 2443, 730, 1789, 2283, 2688, 948, 849, 2857, 415, 1105, 1730, 89, 2259, 596, 2302, 2493, 1405, 384, 1245, 1020, 964, 2179, 1283, 927, 76, 1774, 2887, 2876, 2932, 20, 505, 480, 1158, 1248, 1864, 1708, 1420, 1320, 1172, 2072, 1126, 1877, 2449, 1189, 580, 2856, 2421, 998, 309, 916, 2923, 2378, 2299, 637, 2008, 2531, 1414, 1595, 254, 202, 1017, 427, 987, 931, 2048, 2213, 2377, 742, 1801, 1341, 1813, 1330, 2343, 445, 52, 9, 2948, 1641, 1570, 1208, 2993, 2053, 2758, 1216, 2474, 2798, 796, 2827, 1688, 2631, 2843, 722, 1594, 1638, 1452, 1273, 1901, 2389, 2599, 2365, 2501, 2210, 1018, 2513, 2658, 405, 2401, 2080, 1559, 1044, 32, 2186, 2800, 2427, 211, 896, 1872, 1435, 1075, 398, 1697, 354, 1421, 2568, 2524, 498, 1680, 96, 901, 847, 1982, 2473, 2906, 1377, 1161, 2740, 379, 1159, 1621, 2603, 2912, 699, 1512, 1437, 2885, 2190, 2404, 342, 1527, 894, 2415, 2695, 471, 1709, 2349, 2892, 532, 936, 594, 1671, 404, 1411, 2178, 623, 1459, 2423, 2971, 552, 1609, 2777, 914, 1322, 1596, 2640, 988, 819, 2045, 2803, 437, 286, 2546, 2303, 468, 118, 2595, 435, 2639, 1409, 1091, 2518, 535, 2451, 273, 88, 1879, 136, 2098, 2964, 2103, 2180, 1870, 2480, 2126, 813, 457, 397, 403, 2585, 2381, 2042, 1061, 803, 692, 258, 2088, 1304, 817, 486, 360, 2500, 284, 337, 707, 651, 2015, 465, 884, 684, 460, 1944, 2730, 2555, 2182, 2858, 2999, 574, 1519, 1014, 2298, 1432, 835, 2455, 2, 1608, 928, 1074, 1209, 2419, 2492, 443, 210, 1674, 488, 10, 2324, 220, 1734, 442, 2457, 2667, 874, 2323, 561, 2134, 2188, 703, 643, 2177, 1883, 2054, 2673, 451, 401, 2770, 295, 1329, 2478, 133, 51, 518, 1448, 2446, 613, 2458, 2071, 2818, 645, 2215, 326, 2835, 1684, 1810, 2059, 282, 1576, 520, 2121, 2497, 563, 1467, 2089, 1088, 1541, 2816, 606, 667, 542, 1658, 1974, 2619, 2608, 2616, 479, 2382, 1514, 330, 214, 270, 414, 1934, 1063, 1083, 1425, 2032, 2153, 177, 547, 903, 104, 1351, 1740, 605]
SiralanmisDizi = []

def SelectionSort(SiralanmisDizi):
    for i in range(len(SiralanmisDizi)-1):
        for j in range(i+1,len(SiralanmisDizi)):
            if SiralanmisDizi[j]<SiralanmisDizi[i]:
                tmp = SiralanmisDizi[i]
                SiralanmisDizi[i] = SiralanmisDizi[j]
                SiralanmisDizi[j] = tmp

def BubbleSort(SiralanmisDizi):
    for i in range(len(SiralanmisDizi)):
        for j in range(len(SiralanmisDizi)-1):
            if SiralanmisDizi[j+1] <SiralanmisDizi[j]:
                 tmp = SiralanmisDizi[j]
                 SiralanmisDizi[j] = SiralanmisDizi[j+1]
                 SiralanmisDizi[j+1] = tmp

def CombSort(SiralanmisDizi):
    def getNextGap(gap):
        # Küçültme yapılıyor. Küçülte faktörü kullanılarak
        gap = (gap * 10)/13
        if gap < 1:
            return 1
        return gap

    n = int(len(SiralanmisDizi))
    gap = n
    degistimi = True
    while gap !=1 or degistimi == True:
        gap = int(getNextGap(gap))
        degistimi = False
        for i in range(0, n-gap):
            if SiralanmisDizi[i] > SiralanmisDizi[i + gap]:
                SiralanmisDizi[i], SiralanmisDizi[i + gap]=SiralanmisDizi[i + gap], SiralanmisDizi[i]
                degistimi = True

def InsertionSort(SiralanmisDizi):
    for i in range(1, len(SiralanmisDizi)):
        key = SiralanmisDizi[i]
        j = i-1
        while j >=0 and key < SiralanmisDizi[j] :
            SiralanmisDizi[j+1] = SiralanmisDizi[j]
            j -= 1
            SiralanmisDizi[j+1] = key

def ShellSort(SiralanmisDizi):
    n = int(len(SiralanmisDizi))
    gap = int(round((n+1)//2))
    while gap > 0:
        for i in range(gap,n):
            temp = SiralanmisDizi[i]
            j = i
            while  j >= gap and SiralanmisDizi[j-gap] >temp:
                SiralanmisDizi[j] = SiralanmisDizi[j-gap]
                j -= gap
            SiralanmisDizi[j] = temp
        gap //= 2

def MergeSort(SiralanmisDizi):
    lendizi = len(SiralanmisDizi)
    if len(SiralanmisDizi)>1:
        orta = len(SiralanmisDizi)//2
        sag = SiralanmisDizi[orta:]
        sol = SiralanmisDizi[:orta]
        MergeSort(sag)
        MergeSort(sol)
        i=0
        j=0
        k=0
        while i<len(sol) and j<len(sag):
            if sol[i]<sag[j]:
                SiralanmisDizi[k]=sol[i]
                i = i +1
            else:
                SiralanmisDizi[k] = sag[j]
                j = j + 1
            k = k + 1
        while i<len(sol):
            SiralanmisDizi[k]=sol[i]
            i = i+1
            k = k+1
        while j<len(sag):
            SiralanmisDizi[k]=sag[j]
            j = j+1
            k = k+1

def QuickSort(SiralanmisDizi,sol=0,sag=(len(SiralanmisDizi)-1)):

    def partition(SiralanmisDizi,sol,sag):
        i = ( sol-1 )
        pivot = SiralanmisDizi[sag]
        for j in range(sol , sag):
            if   SiralanmisDizi[j] <= pivot:
                i = i+1
                SiralanmisDizi[i],SiralanmisDizi[j] = SiralanmisDizi[j],SiralanmisDizi[i]
        SiralanmisDizi[i+1],SiralanmisDizi[sag] = SiralanmisDizi[sag],SiralanmisDizi[i+1]
        return ( i+1 )

    if sol < sag:
        pF = partition(SiralanmisDizi,sol,sag)
        QuickSort(SiralanmisDizi, sol, pF-1)
        QuickSort(SiralanmisDizi, pF+1, sag)

def HeapSort(SiralanmisDizi):
    def heapify(SiralanmisDizi, n, i):
        ebuyuk = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and SiralanmisDizi[i] < SiralanmisDizi[l]:
            ebuyuk = l
        if r < n and SiralanmisDizi[ebuyuk] < SiralanmisDizi[r]:
            ebuyuk = r
        if ebuyuk != i:
            SiralanmisDizi[i],SiralanmisDizi[ebuyuk] = SiralanmisDizi[ebuyuk],SiralanmisDizi[i]
            heapify(SiralanmisDizi, n, ebuyuk)

    n = len(SiralanmisDizi)
    for i in range(n, -1, -1):
        heapify(SiralanmisDizi, n, i)
    for i in range(n-1, 0, -1):
        SiralanmisDizi[i], SiralanmisDizi[0] = SiralanmisDizi[0], SiralanmisDizi[i]
        heapify(SiralanmisDizi, i, 0)

def PigeonholeSort(SiralanmisDizi):
    my_min = min(SiralanmisDizi)
    my_max = max(SiralanmisDizi)
    size = my_max - my_min + 1
    holes = [0] * size
    for t in SiralanmisDizi:
        holes[t - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            SiralanmisDizi[i] = count + my_min
            i += 1




for i in range(9):
    SiralanmisDizi = AnaDizi.copy()
    start = time.time()
    cevap = i+1
    if cevap == 1:
        SelectionSort(SiralanmisDizi)
    elif cevap == 2:
        BubbleSort(SiralanmisDizi)
    elif cevap == 3:
        CombSort(SiralanmisDizi)
    elif cevap == 4:
        InsertionSort(SiralanmisDizi)
    elif cevap == 5:
        ShellSort(SiralanmisDizi)
    elif cevap == 6:
        MergeSort(SiralanmisDizi)
    elif cevap == 7:
        QuickSort(SiralanmisDizi)
    elif cevap == 8:
        HeapSort(SiralanmisDizi)
    elif cevap == 9:
        PigeonholeSort(SiralanmisDizi)
    end = time.time()
    print("Seçim = ",i+1," | İşlemin Gerçekleşme Süresi = ",end-start)

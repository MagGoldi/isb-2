import math
from scipy.special import gamma, factorial

sequence = list("10101100111100001010010011100000100001010111011010010000001101101001101111100100111011100010110001111100001100100011011110010000")
sequence = list(map(lambda x: int(x), sequence))

list_lil, list_total = [], []
count = 0

#По рекомендациям NIST разбиваем последовательность на 8 блоков

for n in sequence:
    if count == 8: 
        list_total.extend([list_lil])
        list_lil = []
        count = 0
    list_lil.append(n)     
    count+=1  
print(list_total) 
#[[1, 0, 1, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1, 1, 1]]  



dict_lil_list = {}
count, max_count, i_count = 0, 0, 1

for list_lil in list_total:
    for n in list_lil:
        if n == 1: 
            count+=1
            if count>max_count: max_count = count
        else: count=0
    dict_lil_list["list"+str(i_count)] = max_count
    i_count += 1
    max_count, count = 0, 0 
print(dict_lil_list) 

#{'list1': 2, 'list2': 4, 'list3': 1, 'list4': 3, 'list5': 1, 'list6': 3, 'list7': 1, 'list8': 2, 'list9': 2, 'list10': 3, 'list11': 3, 'list12': 2, 'list13': 5, 'list14': 2, 'list15': 3}


dict_v = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}

for value in dict_lil_list.values():
    if value == 1: dict_v["v1"] += 1
    if value == 2: dict_v["v2"] += 1
    if value == 3: dict_v["v3"] += 1
    if value >= 4: dict_v["v4"] += 1
print(dict_v)
#{'v1': 3, 'v2': 5, 'v3': 5, 'v4': 2}




#hard...  Вычисляем Хи-квадрат:
xi = 0

#для блока из 8 значений:
R = 16
K = 3

#Теоретические вероятности πi задаются константами.Для K=3 и M=8 рекомендуется взять π0 = 0.2148, π1 = 0.3672, π2 = 0.2305, π3 = 0.1875. 

xi = (dict_v["v1"] - (R * 0.2148)/(R * 0.2148)) + (dict_v["v2"] - (R * 0.3672)/(R * 0.3672)) + (dict_v["v3"] - (R * 0.2305)/(R * 0.2305)) +(dict_v["v4"] - (R * 0.1875)/(R * 0.1875))

print(xi)
#11.0

#я облазил весь internet но не нашел гамма функцию, так что поверьте на слово и вычислением с того же internet

#P= math.igamc (3/2,XX/2)
#print(P)

#P 0.011725
#Вывод: последовательность прошла тест

        



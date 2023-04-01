import math

sequence = list("10101100111100001010010011100000100001010111011010010000001101101001101111100100111011100010110001111100001100100011011110010000")
sequence = list(map(lambda x: int(x), sequence))

dict_sequence = {}

for n in sequence:
    if n not in dict_sequence: dict_sequence[n] = 1
    else: dict_sequence[n]+=1  
print(dict_sequence)  
#{1: 61, 0: 67}

pi = dict_sequence[1]/128
print(pi)
#0.4765625

#проверяем условие 
print((abs(pi-0.5))<2/math.sqrt(128))
#True 

#проверка условия во всей последовательности 
k1 = - (pi - 0.5)
k2 = (2/math.sqrt(128))
print (k1)
#0.0234375
print (k2)
#0.17677669529663687


count = 0
for i in range(len(sequence)-1):
    if sequence[i] != sequence[i+1]: count += 1
print (count)
#61

P =  math.erfc((66-2*128*pi*(1-pi))/(2*math.sqrt(2*128)*pi*(1-pi)))
print(P)
#0.7045052566807751
#Вывод: Если 0.7045 >= 0.01, то последовательность признается случайной.
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:34:03 2020

@author: paty-
"""
from math import log
from math import factorial

lista = []
maior = -1000000000000
media =0 
for i in range(0,10):
    if i%2==0:
        lista.append(3**i + 7*factorial(i))
    else:
        lista.append(2**i+4*log(i))
    a = lista[i]
    if a > maior:
        maior = a
    media = media + a/10
    

print(f'O vetor com 10 posições é: {lista} \n\n')
print(f'A média foi: {round(media, 2)} \n\n')
print(f'O maior valor foi: {maior} \n\n')




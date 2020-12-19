# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:07:57 2020

@author: paty-
"""
a=0
for i in range(1,5000001):
    if i%2 == 0 and i%37 ==0 and i%49==0:
        a+=1

print(f'O número de números é {a}')


# ou,se for direto ao ponto    

print(int(5000000/(37*49*2)))
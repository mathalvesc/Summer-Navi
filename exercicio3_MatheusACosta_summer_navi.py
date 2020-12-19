# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:32:59 2020

@author: paty-
"""


aluno = dict()
lista = list()
maior = - 999999999999999999999999999
for i in range(1,6):
    aluno['nome'] = str(input(f'Nome do aluno {i}: '))
    aluno['nota'] = float(input(f'Nota do aluno{i}: '))
    lista.append(aluno.copy())
    if aluno['nota'] > maior:
        alm = aluno['nome']
        maior = aluno['nota']
print(lista, f' \n\n O aluno com a maior média foi o(a) aluno(a) {alm} e a média foi {maior}')


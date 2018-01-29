# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def somatorio(e, p):
    soma = 0
    for i in range(3):
        soma += e[i] * p[i]
    return soma

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

soma = somatorio(entradas, pesos)
resultado = stepFunction(soma)
print(resultado)
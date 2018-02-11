#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:21:25 2018
@author: eduardo
"""
import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0, 0, 0, 1])
saidas = np.array([0, 1, 1, 1])
pesos = np.array([0.0, 0.0])
taxaDeAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = round(registro.dot(pesos), 2)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asanyarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                    pesos[j] = pesos[j] + (taxaDeAprendizagem * entradas[i][j] * erro)
                    print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
            
treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
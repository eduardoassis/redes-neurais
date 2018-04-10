#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:59:10 2018

@author: eduardo
"""
import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])

saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])
    
pesos1 = np.array([[-0.017, -0.893, 0.148]])

epocas = 100

for j in range(epocas):
    camadaEntrada = entradas
    somaSinopse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinopse0)
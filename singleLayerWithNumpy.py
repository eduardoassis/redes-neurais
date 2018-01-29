#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:28:26 2018

@author: eduardo
"""

import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def somatorio(e, p):
    return e.dot(p) 
# dot product / produto escalar

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

soma = somatorio(entradas, pesos)
resultado = stepFunction(soma)
print(resultado)
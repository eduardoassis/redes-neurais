#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:59:10 2018

@author: eduardo
"""
import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

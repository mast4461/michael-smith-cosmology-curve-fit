# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import numpy as np
from scipy.integrate import quad
from settings import speed_of_light

"""
The function below is the exact function decribing the FLRW model with two parameters, Hubble constant and matter density. Note this is a 2-parameter FIT OF CURVED SPACETIME WITHOUT DARK ENERGY
"""
def InterST_D_L(EspFact, Hubble, Matter):
    return _portion1(EspFact, Hubble, Matter)*np.sinh(np.sqrt(np.fabs(1-Matter))*(_vectorizedIntersum(EspFact, Matter)))

"""
This second portion is the function to be integrated
"""
def _portion2(EspFact, Matter):
    return 1/(EspFact*np.sqrt((Matter/EspFact) + (1-Matter)))

def _intersum(EspFact, Matter):
    return quad(_portion2, EspFact, args=(Matter))[0], 1
_vectorizedIntersum = np.vectorize(_intersum, excluded=["Matter"])

"""
This first portion is a simple calculation
"""
def _portion1(EspFact, Hubble, Matter):
    return speed_of_light / (EspFact * Hubble * np.sqrt(np.fabs(1 - Matter)))

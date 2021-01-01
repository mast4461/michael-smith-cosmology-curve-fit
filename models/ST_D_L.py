# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike
"""

import numpy as np
from settings import speed_of_light

"""
This routine analyses D_L_Data for the CURVED UNIVERSE WITHOUT DARK ENERGY.
"""
def ST_D_L(EspFact, Hubble, Matter):
    return (speed_of_light/(Hubble*EspFact*np.sqrt(np.fabs(1-Matter))))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/EspFact)+np.fabs(1-Matter)))))
"""
One can breakdown the above function into two portions if necessary

_portion1 being
def _portion1(EspFact, Hubble, Matter):
    return (speed_of_light/(Hubble*EspFact*np.sqrt(np.fabs(1-Matter))))
    
_portion2 being 
def _portion2(EspFact, Matter):
    np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/EspFact)+np.fabs(1-Matter)))))
    
the final product being 
def cmpltfunction(EspFact, Hubble, Matter):
    return _portion1 * _portion2
"""

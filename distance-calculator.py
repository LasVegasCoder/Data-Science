# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:20 2017
Calculate distance from point B to point A, distance between two points.
@author: Prince Adeyemi
"""

import numpy as np
def distance(p1, p2):
    """find distance between two points"""
    d = np.sqrt(np.sum(np.power(p2-p1,2)))
    return d
    

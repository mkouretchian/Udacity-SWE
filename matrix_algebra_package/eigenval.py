#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:19:05 2021

@author: roji
"""
from matrix_algebra import matrix_algebra
import numpy as np
from sympy.abc import x
class eigenval(matrix_algebra):
    def __init__(self):
        super().__init__()
        
        
    def characteristPolynomial(self,arr_1):
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
            
        else:
             p = self.getMatrixDeterminant(arr_1 - self.multiply(np.identity(len(arr_1))),[[x]]*len(arr_1))
             
        return p
        
    
    
    def eigenval(self,arr_1):
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
            
            
        
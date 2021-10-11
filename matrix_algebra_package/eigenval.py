#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:19:05 2021

@author: roji
"""
from matrix_algebra import matrix_algebra
import numpy as np
import sympy as sym
from sympy.abc import x
class eigenval_function(matrix_algebra):
    def __init__(self):
        super().__init__()
        
        
    def characteristPolynomial(self,arr_1):
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
            
        else:
            arr_2 = x * np.eye(len(arr_1))
            p = self.getMatrixDeternminant(arr_1 - arr_2)
             
        return p
        
    
    
    def eigenvalue(self,arr_1):
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
        else:
            poly = self.characteristPolynomial(arr_1)
            solution = sym.solve(poly,x)
            return solution
            
            

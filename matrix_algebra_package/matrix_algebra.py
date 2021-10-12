#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:08:01 2021

@author: roji
"""
import numpy as np
from inverse import inverse
import sympy as sym
from sympy.abc import x
from rref import rref
from nullSpace import nullSpace

class matrix_algebra(inverse,rref):
    def __init__(self):
        super().__init__()
        
    def add(self,arr_1,arr_2):
        if len(arr_1[0]) != len(arr_2[0]) or len(arr_1) != len(arr_2):
            print("The dimensions of given matrices do not match for addition operator")
        
        else:
        
            s = (len(arr_1)),len(arr_1[0])
            aux = np.zeros(s)
        
            
            for i in range(len(arr_1)):
                for j in range(len(arr_1[0])):
                    aux[i][j] = arr_1[i][j] + arr_2[i][j]
                    
            return aux
    
    
    def transpose(self,arr_1):
        
        num_row = len(arr_1)
        num_col = len(arr_1[0])
        s_transpose = (num_col,num_row)
        aux = np.zeros(s_transpose)
        for i in range(num_col):
            for j in range(num_row):
                aux[i][j] = arr_1[j][i]
                
        return aux
    
    def multiply(self,arr_1,arr_2):
        if len(arr_1[0]) != len(arr_2):
            print("The dimension of two given matrices does not match for matrix multiplication")
            
        else:
            result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*arr_2)]
                                for A_row in arr_1]
            
            return result
        
    def inverse(self,arr_1):
        return self.matrixInverse(arr_1)
    
    def solve(self,arr_1,arr_2):
        
        if len(arr_1) != len(arr_2):
            print("The system of linear equation is inconsistence")
        else :
                arr_1_transpose = self.transpose(arr_1)
                arr_1_transpose_times_arr_1 = self.multiply(arr_1_transpose, arr_1)
                arr_1_transpose_times_arr_1_inverse = self.inverse(arr_1_transpose_times_arr_1)
                arr_1_transpose_times_arr_2 = self.multiply(arr_1_transpose, arr_2)
                solution = self.multiply(arr_1_transpose_times_arr_1_inverse,arr_1_transpose_times_arr_2)
            
        return solution

    def characteristPolynomial(self,arr_1):
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
            
        else:
            arr_2 = x * np.eye(len(arr_1))
            p = self.getMatrixDeternminant(arr_1 - arr_2)
             
        return p
        
    
    
    def eigenvalue(self,arr_1): 
        roots = []
        if len(arr_1) != len(arr_1[0]):
            print("The eigenvalues can be calculated for only square matrices")
        else:
            poly = self.characteristPolynomial(arr_1)
            solution = sym.roots(poly)
            for key , value in solution.items():
                for i in range(value):
                    roots.append(key)
                
            return roots
        
    def rref (self,arr_1):
         arr_1 = np.array(arr_1)
         aux1,_,_ = rref.rref(rref,arr_1)
         return aux1
     
    def null (self,arr_1):
        aux = nullSpace.null(nullSpace,arr_1)
        return aux
    
        
        
    
    
    
    
        
# matrix_algebra = matrix_algebra()
a = [[5,0,1],[2,0,2]]
c = matrix_algebra()
d = c.null(a)
print(d) 
# b = [[2,2],[2,2]]
# c = [[1,2],[3,4],[5,6]]
# add_1 = matrix_algebra.add(a,b)
# print(add_1)

# transpose = matrix_algebra.transpose(c)
# print(transpose)

# multiply = matrix_algebra.multiply(a,b)
# print(multiply)
# d = [[1,0],[0,1]]
# inverse = matrix_algebra.inverse(d)
# print(inverse)

# sol = matrix_algebra.solve([[1,2],[2,1],[3,3]],[[1],[1],[1]])
# print(sol)

# eigenvalue_2 = matrix_algebra.eigenvalue(d)
# print(eigenvalue_2)
       
    
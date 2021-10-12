#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:43:02 2021

@author: roji
"""

from rref import rref
import numpy as np


class nullSpace(rref):
    def __init__(self):
        pass
    
    def null(self,arr):
        arr = np.array(arr)
        arr_rref,pivot,_ = rref.rref(rref,arr)
        col = set(np.arange(len(arr[0])))
        pivot_variable = []
        for item in col :
            for item2 in pivot:
                if item == item2[1]:
                    pivot_variable.append(item)
        pivot_variable = set(pivot_variable)
        free_variable = list(col - pivot_variable)
        
        if len(free_variable) == 0:
            arr = np.zeros(len(arr[0]))
            return arr
        vec = []
        for i in range(len(free_variable)):
            a = np.zeros(len(arr[0]))
            vec.append(a)
        
        
        for item , variable in zip(vec , free_variable):
            for i,_ in pivot:
                item[i] = - arr_rref[i][variable]
            item[variable] = 1
                
        return vec
            
                
                
            
        
            
       
            
                    
        
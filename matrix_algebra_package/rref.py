#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:38:01 2021

@author: roji
"""


import numpy as np

class rref():
    def __init__(self):
        pass
    
    def rref(self,B, tol=1e-8, debug=False):
      A = np.array(B)
      rows, cols = np.shape(A)
      r = 0
      pivots_pos = []
      row_exchanges = np.arange(rows)
      for c in range(cols):
    
        ## Find the pivot row:
        pivot = np.argmax (np.abs (A[r:rows,c])) + r
        m = np.abs(A[pivot, c])
        if m <= tol:
          ## Skip column c, making sure the approximately zero terms are
          ## actually zero.
          A[r:rows, c] = np.zeros(rows-r)
    
        else:
          ## keep track of bound variables
          pivots_pos.append((r,c))
    
          if pivot != r:
            ## Swap current row and pivot row
            A[[pivot, r], c:cols] = A[[r, pivot], c:cols]
            row_exchanges[[pivot,r]] = row_exchanges[[r,pivot]]
            
    
          ## Normalize pivot row
          A[r, c:cols] = A[r, c:cols] / A[r, c];
    
          ## Eliminate the current column
          v = A[r, c:cols]
          ## Above (before row r):
          if r > 0:
            ridx_above = np.arange(r)
            A[ridx_above, c:cols] = A[ridx_above, c:cols] - np.outer(v, A[ridx_above, c]).T
          ## Below (after row r):
          if r < rows-1:
            ridx_below = np.arange(r+1,rows)
            A[ridx_below, c:cols] = A[ridx_below, c:cols] - np.outer(v, A[ridx_below, c]).T
          r += 1
        ## Check if done
        if r == rows:
          break;
      return (A, pivots_pos, row_exchanges)


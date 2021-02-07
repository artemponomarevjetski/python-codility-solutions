#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:32:45 2020

@author: artemponomarev
"""

A = [-3, 1, 2, -2, 5, 6]

def solution(A):
    """ 
    Task description is given on Codility website, https://app.codility.com/programmers/
    maximum product among all triplets
    """
    A.sort()

    if max(A) < -1000 and max(A) > 1000:
        return 0

    if len(A) < 3 or len(A) > 100000:
        return 0

    if len(A) == 3:
        return A[0]*A[1]*A[2]

    product = []
    if A[-1] > 0 and A[-2] > 0 and A[-3] > 0:
        product.append(A[-1]*A[-2]*A[-3])

    if A[0] < 0 and A[1] < 0 and A[-1] >= 0:
        product.append(A[0]*A[1]*A[-1])

    if A[0] < 0 and A[1] >= 0:
        if A[1] == 0:
            product.append(0)
        else:
            product.append(A[0]*A[1]*A[2])

    if A[-1] <= 0 and A[-2] <= 0 and A[-3] <= 0:
        product.append(A[-1]*A[-2]*A[-3])

    if product:
        return max(product)
    else:
        return -1

# main()
print("result  = ", solution(A))

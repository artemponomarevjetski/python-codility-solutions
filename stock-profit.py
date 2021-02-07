#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:32:50 2020

@author: artemponomarev
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    max profit from stocks
    """
    N=len(A)
    if N==0:
        return 0
    if not (N>=0 and N<=4e5):
        return 0
    if not (min(A)>=0 and max(A)<=2e5):
        return 0
    for a in A:
        if a<0:
            return 0
    
    global_max=local_max=0
    for i in range(1, N):
        d=A[i]-A[i-1]
        local_max=max(d, local_max+d)
        global_max=max(global_max, local_max)
    if global_max<=0:
        return 0
    else:
        return global_max
    
# main()
print("result  = ", solution([1, 2, 3]))
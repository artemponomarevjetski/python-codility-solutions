#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:17:17 2020

@author: artemponomarev
"""
A =[ 10,  50,  5,  1]

def solution(A):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    triangular array
    """
    A.sort()
    if len(A)>100000 or len(A)==0 or len(A)==1 or len(A)==2:
        return 0
    if A[-1] >2147483647 or A[0] <-2147483648:
        return 0

    P=0
    for _ in range(len(A)-2):
        Q=P+1
        R=Q+1
        if A[P]+A[Q] > A[R]:
            for j in range(len(A)-R):
                if A[P]+A[Q] > A[R+j] and A[P]+A[R+j]>A[Q]:
                    return 1

        P+=1

    return 0

# main()
print("result  = ", solution(A))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:21:46 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    minimal positive missing array member
    """
    N = len(A)
    if not (N >= 1 and N <= 1e5):
        return -1
    if not (min(A) >= -1e6 and max(A) <= 1e6):
        return 1
    if N == 0:
        return -1
    if N == 1:
        if A[0] <= 0:
            return 1
        else:
            if A[0] > 1:
                return 1
            else:
                return A[0]+1
    if max(A) <= 0:
        return 1
    if min(A) > 1:
        return 1

    A.sort()
    for i in range(N):
        if i == 0:
            if A[i] > 1:
                return 1
        else:
            if A[i] != A[i-1]:
                if A[i] != A[i-1]+1:
                    if A[i-1]+1 > 0:
                        if A[i-1]+1 > 1:
                            return A[i-1]+1
                    else:
                        if A[i] > 1:
                            return 1

    return A[N-1]+1

print("solution = ", solution([0, 1, 2, 3, 4, 7, 9, 12]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:32:27 2020

@author: artemponomarev
"""

def solution(N):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    maximum gap (with 0's) in a binary representation of a number
    """
    if not (N >= 1 and N <= 2147483647):
        return 0
    if N < 0:
        return 0
    if N == 0:
        return 0
    if N == 1:
        return 0

    A = bin(N)
    print(A)
    le = False
    max1 = 0
    len0 = 0
    for i in range(len(A)):
        if i > 1:
            if A[i] == '1':
                if not le:
                    le = True
                else:
                    if len0 != 0:
                        max1 = max(max1, len0)
                        len0 = 0
                    else:
                        pass
            else:
                if le:
                    len0 += 1
                else:
                    pass
    return max1

print(solution(100))

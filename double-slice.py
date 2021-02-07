#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:37:32 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    """
    N=len(A)
    if not (N>=3 and N<=1e5):
        return 0
    if not (min(A)>=-1e4 and max(A)<=1e4):
        return 0
        
    if N==1:
        return 0
    if N==2:
        return 0
    if N==3:
        return 0
        
    max1 = 0
    hole=False
    for i in range(1, N):
        if i == 1:
            max1 = A[i]
            sum1 = A[i]
        else:
            if not hole and A[i+1]+sum1 >= A[i]:
                sum1 += A[i]
                max1 = max(sum1, max1)
                hole=True
            else:
                if A[i] > A[i]+sum1:
                    sum1=A[i]
                    hole=False
                else:
                    sum1 += A[i]
                    if hole:
                        max1 = max(sum1, max1)

    return max1

print(solution([4, 3, 4, 4, 4, 2]))
print(solution([2, 2]))
print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
print(solution([1, 2, 300, 4, 5]))

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
print(solution([5, 17, 0, 3]))
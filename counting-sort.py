#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:28:17 2020

@author: artemponomarev
"""

def countingSort(A, k):
    """
    ~O(n+m) algorithm for sorting
    introduction is given on Codility website, https://app.codility.com/programmers/
    """
    print(A, "\n\n")
    n = len(A)
    count = [0]*(k+1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    print(count, '\n')
    for i in range(k + 1):
        print(i)
        for j in range(count[i]):
            A[p] = i
            p += 1
            print(A, p, i, j, count[i])
    return A

A=[1, 3, 2, 5, 8]
k=max(A)
countingSort(A, k)
print("\n\n\n")
print('result = ', A)

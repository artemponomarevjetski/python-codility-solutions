#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:57:07 2020

@author: artemponomarev
"""

def solution(A, K):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    rotate A K times
    """
    result = [None] * len(A)

    for i in range(len(A)):
        result[(i + K) % len(A)] = A[i]

    return result

print(solution([1, 2, 3, 4, 5], 2))

print(solution([1, 2, 3, 4, 5], 5))

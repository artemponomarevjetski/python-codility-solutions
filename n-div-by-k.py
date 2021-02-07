#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:42:35 2020

@author: artemponomarev
"""

def solution(A, B, K):
    """"
    Task description is given on Codility website, https://app.codility.com/programmers/
    number of divisibles
    """

    if A > B or A < 0 or B < 0 or K <= 0 or K > 2e9 or B > 2e9:
        return 0

    if A % K == 0:
        return (int(B / K) - int(A / K)) + 1

    return int(B / K) - int(A / K)

print("result  = ", solution(6, 11, 2))

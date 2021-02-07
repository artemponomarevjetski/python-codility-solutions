#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:12:59 2020

@author: artemponomarev
"""
import math
def solution(N):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    number of factors of N
    """
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has two factors: candidate and N // candidate
        if N % candidate == 0:
            result += 2
        candidate += 1
    # If N is square of some value.
    if candidate * candidate == N:
        result += 1
    return result

print(solution(24))
print(solution(41))
print(solution(61))
print(solution(68))
print(solution(math.pow(2, 100)))

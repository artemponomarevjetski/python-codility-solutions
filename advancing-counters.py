#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:23:00 2020

@author: artemponomarev
"""
# write your code in Python 3.6
A = [3, 4, 4, 6, 1, 4, 4]
N = 5

def solution(N, A):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    advancing counters
    """
    if N <= 0:
        return 0
    if len(A) == 0:
        return 0
    M = len(A)
    if not (N >= 1 and N <= 1e5):
        return 0
    if not (M >= 1 and M <= 1e5):
        return 0
    for a in A:
        if not (a >= 1 and a <= N+1):
            return 0

    counters = [0]*N
    new_start = 0
    current_max = 0
    a_prev = -1
    for a in A:
        if a == N+1:
            if a_prev != N+1:
                new_start += current_max
                counters = [0]*N
                current_max = 0
        else:
            counters[a-1] += 1
            if counters[a-1] > current_max:
                current_max = counters[a-1]
        a_prev = a

    for j in range(N):
        counters[j] += new_start

    return counters

# main()
print("result  = ", solution(N, A))

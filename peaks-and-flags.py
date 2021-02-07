#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:19:38 2020

@author: artemponomarev
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    View the codility problem description on
    https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
    """
    # write your code in Python 3.6
    N = len(A)

    if not (N >= 1 and N <= 4e5):
        return 0
    if not (min(A) >= 0 and max(A) <= 1e9):
        return 0
    if N == 0 or N == 1 or N == 2:
        return 0
    if N == 3:
        if A[0] < A[1] and A[1] > A[2]:
            return 1
        else:
            return 0

    stack = []
    i_prev = 0
    npeaks = 0
    for i in range(N-1):
        if i == 0:
            pass
        elif A[i-1] < A[i] and A[i] > A[i+1] and npeaks == 0:
            i_prev = i
            npeaks = 1
        elif A[i-1] < A[i] and A[i] > A[i+1]:
            stack.append(i-i_prev)
            i_prev = i
            npeaks += 1
        else:
            pass

    if npeaks == 0:
        return 0
    if npeaks == 1:
        return 1

    max1 = 1
    k = 2
    while k*(k-1) <= N-2 and k <= npeaks:
        nflags = 1
        delta = 0
        for j in range(npeaks-1):
            delta += stack[j]
            if delta >= k:
                if nflags >= k:
                    break
                nflags += 1
                delta = 0

        max1 = max(max1, nflags)
        if nflags < k:
            break

        k += 1

    return max1

A = [0] * 12
A[0] = 1
A[1] = 5
A[2] = 3
A[3] = 4
A[4] = 3
A[5] = 4
A[6] = 1
A[7] = 2
A[8] = 3
A[9] = 4
A[10] = 6
A[11] = 2

print(solution(A))

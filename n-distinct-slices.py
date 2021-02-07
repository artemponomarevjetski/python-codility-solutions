#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:43:03 2020

@author: artemponomarev
"""

def solution(M, A):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    count distinct slices
    """
    total_slices = 0
    in_current_slice = [False] * (M + 1)
    head = 0
    for tail in range(0, len(A)):
        while head < len(A) and (not in_current_slice[A[head]]):
            in_current_slice[A[head]] = True
            total_slices += (head - tail) + 1
            head += 1
            total_slices = 1000000000 if total_slices > 1000000000 else total_slices
        in_current_slice[A[tail]] = False
        print(A, tail, in_current_slice)
    return total_slices


print(solution(9, [2, 4, 1, 7, 4, 9, 7, 3, 5, 5, 8, 7, 1]))

print(solution(6, [3, 4, 5, 5, 2]))

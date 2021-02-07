#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 08:57:30 2020

@author: artemponomarev
"""

A = [2, 1, 1, 2, 3, 1]

def solution(A):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    number of unique elements in a list
    """
    if not (len(A) > 0 and len(A) <= 1e5):
        return 0
    if not (min(A) >= -1e6 and max(A) <= 1e6):
        return 0
    if len(A)==0:
        return 0

    return len(list(set(A)))
# main()
print("result  = ", solution(A))

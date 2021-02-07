#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:55:22 2020

@author: artemponomarev
"""
A = [0, 1, 0, 1, 1]

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    number of pairs of passing cars
    """
    for a in A:
        if a not in [0, 1]:
            return 0
    N = len(A)
    if not (N >= 1 and N <= 1e5):
        return 0
    if N == 0 or N == 1:
        return 0

    sum_pairs = 0
    sum_west = sum(A)
    for i in range(N-1):
        if not A[i]:
            sum_pairs += sum_west
            if sum_pairs > 1e9:
                return -1
        else:
            sum_west -= 1
    return sum_pairs

# main()
print("result  = ", solution(A))

#Task description
#A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
#
#Array A contains only 0s and/or 1s:
#
#0 represents a car traveling east,
#1 represents a car traveling west.
#The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
#
#For example, consider array A such that:
#
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
#
#The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
#
#For example, given:
#
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#the function should return 5, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer that can have one of the following values: 0, 1.

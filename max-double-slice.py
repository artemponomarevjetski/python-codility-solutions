#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:18:46 2020

@author: artemponomarev
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    this is the solution for the max double slice problem
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 3 and N <= 1e5):
        return 0
    if not (min(A) >= -1e4 and max(A) <= 1e4):
        return 0
    if N == 1:
        return 0
    if N == 2:
        return 0
    if N == 3:
        return 0

    head = [0] * len(A)
    tail = [0] * len(A)

    for idx in range(1, len(A)):
        head[idx] = max(0, head[idx-1] + A[idx])

    for idx in reversed(range(len(A)-1)):
        tail[idx] = max(0, tail[idx+1] + A[idx])

    max_double_slice = 0

    for idx in range(1, len(A)-1):
        max_double_slice = max(max_double_slice, head[idx-1] + tail[idx+1])

    return max_double_slice

A_exmpl = [0]*8
A_exmpl[0] = 3
A_exmpl[1] = 2
A_exmpl[2] = 6
A_exmpl[3] = -1
A_exmpl[4] = 4
A_exmpl[5] = 5
A_exmpl[6] = -1
A_exmpl[7] = 2
print(solution(A_exmpl))

#
#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ simple1
#first simple test ✔OK
#▶ simple2
#second simple test ✔OK
#▶ simple3
#third simple test ✔OK
#▶ negative
#all negative numbers ✔OK
#▶ positive
#all positive numbers ✔OK
#▶ extreme_triplet
#three elements ✔OK
#expand allPerformance tests
#▶ small_random1
#random, numbers form -10**4 to 10**4, length = 70 ✔OK
#▶ small_random2
#random, numbers from -30 to 30, length = 300 ✔OK
#▶ medium_range
#-1000, ..., 1000 ✔OK
#▶ large_ones
#random numbers from -1 to 1, length = ~100,000 ✔OK
#▶ large_random
#random, length = ~100,000 ✔OK
#▶ extreme_maximal
#all maximal values, length = ~100,000 ✔OK
#▶ large_sequence
#many the same small sequences, length = ~100,000 ✔OK
#
#This the task description as given on Codility website:
#
#    Task description
#A non-empty array A consisting of N integers is given.
#
#A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
#
#The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
#
#For example, array A such that:
#
#    A[0] = 3
#    A[1] = 2
#    A[2] = 6
#    A[3] = -1
#    A[4] = 4
#    A[5] = 5
#    A[6] = -1
#    A[7] = 2
#contains the following example double slices:
#
#double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
#double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
#double slice (3, 4, 5), sum is 0.
#The goal is to find the maximal sum of any double slice.
#
#Write a function:
#
#def solution(A)
#
#that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.
#
#For example, given:
#
#    A[0] = 3
#    A[1] = 2
#    A[2] = 6
#    A[3] = -1
#    A[4] = 4
#    A[5] = 5
#    A[6] = -1
#    A[7] = 2
#the function should return 17, because no double slice of array A has a sum of greater than 17.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [3..100,000];
#each element of array A is an integer within the range [−10,000..10,000].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

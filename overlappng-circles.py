#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:12:48 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    number of pairs of overlapping circles
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 0 and N <= 1e5):
        return 0
    if not (min(A) >= 0 and max(A) <= 2147483647):
        return 0
    for a in A:
        if a < 0:
            return 0

    B = [[i-A[i], 1] for i in range(N)]
    C = [[i+A[i],-1] for i in range(N)]
    D = B+C
    E = sorted(D, key=lambda x: x[0])
    sum1 = sum2 = 0
    for i in range(len(E)):
        temp = E[i][1]
        sum1 += temp
        if temp == 1:
            sum2 += sum1-1
            if sum2 > 1e7:
                return -1
    return sum2

# main()
#    A = [1, 5, 2, 1, 4, 0]
#A = [1, 1, 1]
print("result  = ", solution([1, 5, 2, 1, 4, 0]))
#
#Task description
#We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
#
#We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).
#
#The figure below shows discs drawn for N = 6 and A as follows:
#
#  A[0] = 1
#  A[1] = 5
#  A[2] = 2
#  A[3] = 1
#  A[4] = 4
#  A[5] = 0
#
#
#There are eleven (unordered) pairs of discs that intersect, namely:
#
#discs 1 and 4 intersect, and both intersect with all the other discs;
#disc 2 also intersects with discs 0 and 3.
#Write a function:
#
#def solution(A)
#
#that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
#
#Given array A shown above, the function should return 11, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range [0..2,147,483,647].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#
#
#Analysis
#Detected time complexity:
#O(N*log(N)) or O(N)
#expand allExample tests
#▶ example1
#example test ✔OK
#expand allCorrectness tests
#▶ simple1 ✔OK
#▶ simple2 ✔OK
#▶ simple3 ✔OK
#▶ extreme_small
#empty and [10] ✔OK
#▶ small1 ✔OK
#▶ small2 ✔OK
#▶ small3 ✔OK
#▶ overflow
#arithmetic overflow tests ✔OK
#expand allPerformance tests
#▶ medium1 ✔OK
#▶ medium2 ✔OK
#▶ medium3 ✔OK
#▶ medium4 ✔OK
#▶ 10M_intersections
#10.000.000 intersections ✔OK
#▶ big1 ✔OK
#▶ big2 ✔OK
#▶ big3
#[0]*100.000 ✔OK

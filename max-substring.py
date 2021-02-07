#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:03:08 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """ 
    Task description is given on Codility website, https://app.codility.com/programmers/
    find the maximum sum of elements in all substrings
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 1 and N <= 1e6):
        return 0
    if not (min(A) >= -1e6 and max(A) <= 1e6):
        return 0

    max1 = sum1 = 0
    for i in range(N):
        if i == 0:
            max1 = A[i]
            sum1 = A[i]
        elif A[i] > A[i]+sum1:
            sum1 = A[i]
            max1 = max(sum1, max1)
            if not (max1 >= -2147483648 and max1 <= 2147483647):
                return 0
        else:
            sum1 += A[i]
            max1 = max(sum1, max1)
            if not (max1 >= -2147483648 and max1 <= 2147483647):
                return 0

    return max1

print(solution([3, 2, -6, 4, 0]))
#
#Task description
#A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].
#
#Write a function:
#
#def solution(A)
#
#that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
#
#For example, given array A such that:
#
#A[0] = 3  A[1] = 2  A[2] = -6
#A[3] = 4  A[4] = 0
#the function should return 5 because:
#
#(3, 4) is a slice of A that has sum 4,
#(2, 2) is a slice of A that has sum −6,
#(0, 1) is a slice of A that has sum 5,
#no other slice of A has sum greater than (0, 1).
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..1,000,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000];
#the result will be an integer within the range [−2,147,483,648..2,147,483,647].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example ✔OK
#expand allCorrectness tests
#▶ one_element ✔OK
#▶ two_elements ✔OK
#▶ three_elements ✔OK
#▶ simple ✔OK
#▶ extreme_minimum ✔OK
#▶ fifty_random ✔OK
#▶ neg_const ✔OK
#▶ pos_const ✔OK
#expand allPerformance tests
#▶ high_low_1Kgarbage ✔OK
#▶ 1Kgarbage_high_low ✔OK
#▶ growing_saw ✔OK
#▶ blocks ✔OK
#▶ growing_negative ✔OK

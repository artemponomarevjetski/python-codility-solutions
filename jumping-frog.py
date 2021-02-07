#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:22:40 2020

@author: artemponomarev
"""
A = [1, 3, 1, 4, 2, 3, 5, 4]; X = 5

def solution(X, A):
# write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    jumping frog
    """
    N = len(A)
    if X <= 0:
        return 0
    if N == 0:
        return 0
    if max(A) > X:
        return 0
    for a in A:
        if not (a >= 1 and a <= X):
            return 0
        if not (N >= 1 and N <= 1e5):
            return 0
    if not (X >= 1 and X <= 1e5):
        return 0

    B = [[i, A[i]] for i in range(N)]
    C = sorted(B, key=lambda x: x[1])
    last_stop = 0
    last_drop = 0
    for i in range(N):
        if last_stop+1 == C[i][1]:
            last_stop += 1
    if last_drop < C[i][0]:
        last_drop = C[i][0]
        if last_stop == X:
            return last_drop
    return -1

# main()
print("result  = ", solution(X, A))

#
#Task description
#A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
#
#You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
#
#The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.
#
#For example, you are given integer X = 5 and array A such that:
#
#  A[0] = 1
#  A[1] = 3
#  A[2] = 1
#  A[3] = 4
#  A[4] = 2
#  A[5] = 3
#  A[6] = 5
#  A[7] = 4
#In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
#
#Write a function:
#
#def solution(X, A)
#
#that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
#
#If the frog is never able to jump to the other side of the river, the function should return −1.
#
#For example, given X = 5 and array A such that:
#
#  A[0] = 1
#  A[1] = 3
#  A[2] = 1
#  A[3] = 4
#  A[4] = 2
#  A[5] = 3
#  A[6] = 5
#  A[7] = 4
#the function should return 6, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N and X are integers within the range [1..100,000];
#each element of array A is an integer within the range [1..X].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#
#O(N)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ simple
#simple test ✔OK
#▶ single
#single element ✔OK
#▶ extreme_frog
#frog never across the river ✔OK
#▶ small_random1
#3 random permutation, X = 50 ✔OK
#▶ small_random2
#5 random permutation, X = 60 ✔OK
#▶ extreme_leaves
#all leaves in the same place ✔OK
#expand allPerformance tests
#▶ medium_random
#6 and 2 random permutations, X = ~5,000 ✔OK
#▶ medium_range
#arithmetic sequences, X = 5,000 ✔OK
#▶ large_random
#10 and 100 random permutation, X = ~10,000 ✔OK
#▶ large_permutation
#permutation tests ✔OK
#▶ large_range
#arithmetic sequences, X = 30,000 ✔OK

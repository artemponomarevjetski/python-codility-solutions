#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:41:39 2020

@author: artemponomarev
"""

def solution(A, B):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    big/small fish encounters
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 1 and N <= 1e5):
        return 0
    if len(B) != N:
        return 0
    if not (min(A) >= 0 and max(A) <= 1e9):
        return 0
    for b in B:
        if b not in [0, 1]:
            return 0

    stack = []
    nsurvivors_upstream = 0
    for i in range(N):
        if i == 0 and B[0] == 0:
            nsurvivors_upstream += 1
        else:
            if B[i] == 0:
                if stack:
                    while stack:
                        C = stack.pop()
                        if C > A[i]:
                            stack.append(C)
                            break
                    if not stack:
                        nsurvivors_upstream += 1
                else:
                    nsurvivors_upstream += 1
            else:
                stack.append(A[i])

    nsurvivors_total = nsurvivors_upstream+len(stack)
    return nsurvivors_total

# main()
print("result  = ", solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

#ask description
#You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.
#
#The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.
#
#Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:
#
#0 represents a fish flowing upstream,
#1 represents a fish flowing downstream.
#If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:
#
#If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
#If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
#We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.
#
#For example, consider arrays A and B such that:
#
#  A[0] = 4    B[0] = 0
#  A[1] = 3    B[1] = 1
#  A[2] = 2    B[2] = 0
#  A[3] = 1    B[3] = 0
#  A[4] = 5    B[4] = 0
#Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.
#
#Write a function:
#
#def solution(A, B)
#
#that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.
#
#For example, given the arrays shown above, the function should return 2, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [0..1,000,000,000];
#each element of array B is an integer that can have one of the following values: 0, 1;
#the elements of A are all distinct.
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
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
#▶ extreme_small
#1 or 2 fishes ✔OK
#▶ simple1
#simple test ✔OK
#▶ simple2
#simple test ✔OK
#▶ small_random
#small random test, N = ~100 ✔OK
#expand allPerformance tests
#▶ medium_random
#small medium test, N = ~5,000 ✔OK
#▶ large_random
#large random test, N = ~100,000 ✔OK
#▶ extreme_range1
#all except one fish flowing in the same direction ✔OK
#▶ extreme_range2
#all fish flowing in the same direction ✔OK

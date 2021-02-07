#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:35:06 2020

@author: artemponomarev
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    solution for equileader
    """
    N = len(A)
    if not (N >= 1 and N <= 1e5):
        return 0
    if not (min(A) >= -1e9 and max(A) <= 1e9):
        return 0
    if N == 1:
        return 0
    if N == 2:
        if A[0] == A[1]:
            return 1
        else:
            return 0

    A_len = N
    candidate = None
    candidate_count = 0
    # Find out a leader candidate
    for index in range(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= A_len//2:
        # The candidate is not the leader
        return 0 # return 0, when there is no leaders in A
    else:
        leader = candidate
    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(A_len):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 \
        and leader_count-leader_count_so_far > (A_len-index-1)//2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            equi_leaders += 1
    return equi_leaders

print(solution([1, 1, 5, 5, 5, 5]))
#
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ single
#single element ✔OK
#▶ double
#two elements ✔OK
#▶ simple
#simple test ✔OK
#▶ small_random
#small random test with two values, length = ~100 ✔OK
#▶ small
#random + 200 * [MIN_INT] + random ,length = ~300 ✔OK
#expand allPerformance tests
#▶ large_random
#large random test with two values, length = ~50,000 ✔OK
#▶ large
#random(0,1) + 50000 * [0] + random(0, 1), length = ~100,000 ✔OK
#▶ large_range
#1, 2, ..., N, length = ~100,000 ✔OK
#▶ extreme_large
#all the same values

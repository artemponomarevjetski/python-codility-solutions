#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:47:18 2020

@author: artemponomarev
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    Manhattan skyline
    """
    N = len(H)
    if N == 0:
        return 0
    if not (N >= 1 and N <= 1e5):
        return 0
    if not (min(H) >= 1 and max(H) <= 1e9):
        return 0
    for h in H:
        if h <= 0:
            return 0

    accepted_blocks = []
    new_blocks = []
    for i in range(N):
        if i == 0:
            new_blocks.append(H[i])
        elif H[i] > H[i-1]:
            new_blocks.append(H[i]-H[i-1])
        else:
            height_drop = H[i-1]-H[i]
            if height_drop:
                sum_height_top_blocks = 0
                while new_blocks and sum_height_top_blocks < height_drop:
                    block_out = new_blocks.pop()
                    sum_height_top_blocks += block_out
                    accepted_blocks.append(block_out)
                if sum_height_top_blocks > height_drop:
                    new_blocks.append(sum_height_top_blocks-height_drop)

    return len(accepted_blocks+new_blocks)

# main()
print("result  = ", solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
#
#Task description
#You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
#
#The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
#
#Write a function:
#
#def solution(H)
#
#that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
#
#For example, given array H containing N = 9 integers:
#
#  H[0] = 8    H[1] = 8    H[2] = 5
#  H[3] = 7    H[4] = 9    H[5] = 8
#  H[6] = 7    H[7] = 4    H[8] = 8
#the function should return 7. The figure shows one possible arrangement of seven blocks.
#
#
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#each element of array H is an integer within the range [1..1,000,000,000].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#
#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example ✔OK
#expand allCorrectness tests
#▶ simple1 ✔OK
#▶ simple2 ✔OK
#▶ simple3 ✔OK
#▶ simple4 ✔OK
#▶ boundary_cases ✔OK
#expand allPerformance tests
#▶ medium1 ✔OK
#▶ medium2 ✔OK
#▶ medium3 ✔OK
#▶ medium4 ✔OK
#▶ large_piramid ✔OK
#▶ large_increasing_decreasing ✔OK
#▶ large_up_to_20 ✔OK
#▶ large_up_to_100 ✔OK
#▶ large_max ✔OK

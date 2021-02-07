#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:12:40 2020

@author: artemponomarev
"""

def solution(N):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    """
    if not (1 <= N <= 1e9):
        return 0
    min_per=2*(N+1)
    factor = 1
    while factor * factor < N:
        # N has two factors: factor and N // factor
        if N % factor == 0:
            min_per=min(min_per, 2*(factor+N//factor))
        factor += 1
    # the last case is when N is square of some value.
    if factor * factor == N:
        min_per=min(min_per, 4*factor)
        
    return min_per

print(solution(30))
print(solution(100))
print(solution(101)) # prime N results in a rectangle with one side = 1
print(solution(pow(2, 8)))
#
#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(sqrt(N))
#expand allExample tests
#▶ example 
#example test ✔OK
#expand allCorrectness tests
#▶ extreme_min 
#N = 1 test ✔OK
#▶ simple1 
#N = 36 test ✔OK
#▶ simple2 
#N = 48 test ✔OK
#▶ simple3 
#N = 101 test ✔OK
#▶ small 
#N = 1,234 test ✔OK
#expand allPerformance tests
#▶ medium 
#N = 4,564,320 test ✔OK
#▶ prime1 
#N = 15,486,451 test ✔OK
#▶ square 
#N = 100,000,000 test ✔OK
#▶ prime2 
#N = 982,451,653 test ✔OK
#▶ extreme_max 
#N = 1,000,000,000 test ✔OK
#
#Task description
#An integer N is given, representing the area of some rectangle.
#
#The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
#
#The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.
#
#For example, given integer N = 30, rectangles of area 30 are:
#
#(1, 30), with a perimeter of 62,
#(2, 15), with a perimeter of 34,
#(3, 10), with a perimeter of 26,
#(5, 6), with a perimeter of 22.
#Write a function:
#
#def solution(N)
#
#that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.
#
#For example, given an integer N = 30, the function should return 22, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..1,000,000,000].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
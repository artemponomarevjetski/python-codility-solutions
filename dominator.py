#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:37:17 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    dominator = element of an array that occurs more than N/2 times
    """
    N = len(A)
    if N == 0:
        return -1
    if not N <= 1e5:
        return -1
    if not (min(A) >= -2147483648 and max(A) <= 2147483647):
        return -1

    if N == 1:
        return 0
    stack = []
    B = A[:]
    B.sort()
    for i in range(len(B)):
        if i == 0:
            stack.append(B[i])
        else:
            if stack and B[i] == stack.pop():
                stack.append(B[i])
                stack.append(B[i])
            else:
                if not stack:
                    stack.append(B[i])

    if stack:
        dominator = stack.pop()
        noccur = 0
        for i in range(len(A)):
            if A[i] == dominator:
                noccur += 1
        if noccur > N/2:
            print(dominator, noccur)
            for i in range(len(A)):
                if A[i] == dominator:
                    return i
        else:
            return -1
    else:
        return -1
    return -1

# main()
print("result  = ", solution([3, 4, 3, 2, 3, -1, 3, 3]))

#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(N*log(N)) or O(N)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ small_nondominator
#all different and all the same elements ✔OK
#▶ small_half_positions
#half elements the same, and half + 1 elements the same ✔OK
#▶ small
#small test ✔OK
#▶ small_pyramid
#decreasing and plateau, small ✔OK
#▶ extreme_empty_and_single_item
#empty and single element arrays ✔OK
#▶ extreme_half1
#array with exactly N/2 values 1, N even + [0,0,1,1,1] ✔OK
#▶ extreme_half2
#array with exactly floor(N/2) values 1, N odd + [0,0,1,1,1] ✔OK
#▶ extreme_half3
#array with exactly ceil(N/2) values 1 + [0,0,1,1,1] ✔OK
#expand allPerformance tests
#▶ medium_pyramid
#decreasing and plateau, medium ✔OK
#▶ large_pyramid
#decreasing and plateau, large ✔OK
#▶ medium_random
#random test with dominator, N = 10,000 ✔OK
#▶ large_random
#random test with dominator, N = 100,000 ✔OK
#
#Task description is given on Codility website, https://app.codility.com/programmers/
#An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
#
#For example, consider array A such that
#
# A[0] = 3    A[1] = 4    A[2] =  3
# A[3] = 2    A[4] = 3    A[5] = -1
# A[6] = 3    A[7] = 3
#The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
#Write a function
#
#def solution(A)
#
#that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.
#
#For example, given array A such that
#
# A[0] = 3    A[1] = 4    A[2] =  3
# A[3] = 2    A[4] = 3    A[5] = -1
# A[6] = 3    A[7] = 3
#the function may return 0, 2, 4, 6 or 7, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#

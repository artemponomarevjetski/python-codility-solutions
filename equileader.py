#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:02:56 2020

@author: artemponomarev
"""

def solution(A):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    equileader
    """
    N = len(A)
    if N == 0:
        return 0
    if not (N >= 1 and N <= 1e5):
        return 0
    if not (min(A) >= -1e9 and max(A) <= 2e9):
        return 0

    left_leaders = []
    right_leaders = []
    for i in range(N-1):
        if i == 0:
            left_leaders.append([i, A[i]])
        else:
            B = A[0:i+1]
            stack = []
            for j in range(len(B)):
                if j == 0:
                    stack.append(B[j])
                else:
                    if stack and B[j] == stack.pop():
                        stack.append(B[j])
                        stack.append(B[j])
                    else:
                        if not stack:
                            stack.append(B[j])

            if stack:
                dominator = stack.pop()
                noccur = 0
                for j in range(len(B)):
                    if B[j] == dominator:
                        noccur += 1
                if noccur > len(B)/2:
                    left_leaders.append([i, dominator])
                else:
                    left_leaders.append([i, -1])
            else:
                left_leaders.append([i, -1])

        if i == N-2:
            right_leaders.append([i, A[N-1]])
        else:
            B = A[i+1:]
            stack = []
            for j in range(len(B)):
                if j == 0:
                    stack.append(B[j])
                else:
                    if stack and B[j] == stack.pop():
                        stack.append(B[j])
                        stack.append(B[j])
                    else:
                        if not stack:
                            stack.append(B[j])

            if stack:
                dominator = stack.pop()
                noccur = 0
                for j in range(len(B)):
                    if B[j] == dominator:
                        noccur += 1
                if noccur > len(B)/2:
                    right_leaders.append([i, dominator])
                else:
                    right_leaders.append([i, -1])
            else:
                right_leaders.append([i, -1])

    count = 0
    for i in range(N-1):
        for j in range(N-1):
            if left_leaders[i][0] == right_leaders[j][0]:
                if left_leaders[i][1] != -1 and left_leaders[i][1] == right_leaders[j][1]:
                    count += 1
    return count

print(solution([4, 3, 4, 4, 4, 2]))
print(solution([2, 2]))
print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
print(solution([1, 2, 3, 4, 5]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:12:31 2020

@author: artemponomarev

Solution to the codility problem:
Problem statement is from https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
The following best solution is taken from  https://massivealgorithms.blogspot.com/2015/07/
"""

def solution(A):
    # write your code in Python 3.6
      A_max = max(A)
      count = {}
      for element in A:
        if element not in count:
          count[element] = 1
        else:
          count[element] += 1
      divisors = {}
      for element in A:
        divisors[element] = set([1, element])
      # default divisors
      # start the Sieve of Eratosthenes
      divisor = 2
      while divisor*divisor <= A_max:
        element_candidate = divisor
        while element_candidate <= A_max:
          if element_candidate in divisors and not divisor in divisors[element_candidate]:
            divisors[element_candidate].add(divisor)
            divisors[element_candidate].add(element_candidate//divisor)
          element_candidate += divisor
        divisor += 1
      result = [0] * len(A)
      for idx, element in enumerate(A):
        result[idx] = (len(A)-sum([count.get(divisor,0) for divisor in divisors[element]]))
      return result

# backup solutions:
#     def solution(A):
#   # write your code in Python 3.6
#   one_hot = [0]*max(A)
#   for i in range(N):
#     one_hot[A[i]-1] += 1
#   result = []
#   for i in range(N):
#     j = 1
#     count = 0
#     while j*j < A[i]:
#       if A[i] % j == 0:
#         count += one_hot[j-1]
#         count += one_hot[A[i]//j-1]
#       j += 1
#     if j*j == A[i]:
#       if j in A:
#         count += one_hot[j-1]
#     result.append(N-count)
#   return result

# def solution(A):
#   # write your code in Python 3.6
#   return [len(A)-sum([A.count(A[i]//l) for l in range(1, A[i]+1) if A[i]//l == A[i]/l]) for i in range(len(A))]


A=[0]*5
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 3
A[4] = 6
print(solution(A))

# The solution obtained perfect score.
# Analysis
# Detected time complexity:
# O(N * log(N))
# expand all
# Example tests
# ▶
# example
# example test
# ✔
# OK
# expand all
# Correctness tests
# ▶
# extreme_simple
# extreme simple
# ✔
# OK
# ▶
# double
# two elements
# ✔
# OK
# ▶
# simple
# simple tests
# ✔
# OK
# ▶
# primes
# prime numbers
# ✔
# OK
# ▶
# small_random
# small, random numbers, length = 100
# ✔
# OK
# expand all
# Performance tests
# ▶
# medium_random
# medium, random numbers length = 5,000
# ✔
# OK
# ▶
# large_range
# 1, 2, ..., N, length = ~20,000
# ✔
# OK
# ▶
# large_random
# large, random numbers, length = ~30,000
# ✔
# OK
# ▶
# large_extreme
# large, all the same values, length = 50,000

# Problem statement is from https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/
# Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
# You are given an array A consisting of N integers.
# For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.
# For example, consider integer N = 5 and array A such that:
#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:
# * A[0] = 3, the non-divisors are: 2, 6,
# * A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# * A[2] = 2, the non-divisors are: 3, 3, 6,
# * A[3] = 3, the non-divisors are: 2, 6,
# * A[4] = 6, there aren't any non-divisors.
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.
# Result array should be returned as an array of integers.
# For example, given:
#     A[0] = 3
#    A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# the function should return [2, 4, 3, 2, 0], as explained above.
# Write an efficient algorithm for the following assumptions:
# * N is an integer within the range [1..50,000];
# * each element of array A is an integer within the range [1..2 * N].
# Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:05:40 2020

@author: artemponomarev
"""

def solution(S):
    # write your code in Python 3.6
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    test for properly nested ( and )
    """
    N = len(S)
    if N == 0:
        return 1
    if not (N >= 0 and N <= 1e6):
        return 0
    for c in S:
        if c not in ['(', ')']:
            return 0

    stack = []
    for c in S:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                return 0

    if stack == []:
        return 1
    else:
        return 0

# main()
print("result  = ", solution("(()(())())"))

#Task description
#A string S consisting of N characters is called properly nested if:
#
#S is empty;
#S has the form "(U)" where U is a properly nested string;
#S has the form "VW" where V and W are properly nested strings.
#For example, string "(()(())())" is properly nested but string "())" isn't.
#
#Write a function:
#
#def solution(S)
#
#that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
#
#For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..1,000,000];
#string S consists only of the characters "(" and/or ")".
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#
#Analysis summary
#The solution obtained perfect score.
#
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example1
#example test ✔OK
#▶ example2
#example test2 ✔OK
#expand allCorrectness tests
#▶ negative_match
#invalid structure, but the number of parentheses matches ✔OK
#▶ empty
#empty string ✔OK
#▶ simple_grouped
#simple grouped positive and negative test, length=22 ✔OK
#▶ small_random ✔OK
#expand allPerformance tests
#▶ large1
#simple large positive and negative test, 10K or 10K+1 ('s followed by 10K )'s ✔OK
#▶ large_full_ternary_tree
#tree of the form T=(TTT) and depth 11, length=177K+ ✔OK
#▶ multiple_full_binary_trees
#sequence of full trees of the form T=(TT), depths [1..10..1], with/without unmatched ')' at the end, length=49K+ ✔OK
#▶ broad_tree_with_deep_paths
#string of the form (TTT...T) of 300 T's, each T being '(((...)))' nested 200-fold, length=1 million ✔OK

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:05:40 2020

@author: artemponomarev
"""

def solution(S):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    check whether there is proper nesting
    """
    N = len(S)
    if N == 0:
        return 1
    if not (N >= 0 and N <= 2e5):
        return 0
    for c in S:
        if c not in ['(', '{', '[', ')', '}', ']']:
            return 0
    n_left = n_right = 0
    for c in S:
        if c in ['(', '{', '[']:
            n_left += 1
        else:
            n_right += 1
    if n_left != n_right:
        return 0

    test = True
    stack = []
    for c in S:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c == ')':
            test = False if stack and stack.pop() != '(' else test
        elif c == '}':
            test = False if stack and stack.pop() != '{' else test
        elif c == ']':
            test = False if stack and stack.pop() != '[' else test

    return 1 if test and not stack else 0

# main()
print("result  = ", solution('{[()]}'))

#
#Task description
#A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
#
#S is empty;
#S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
#S has the form "VW" where V and W are properly nested strings.
#For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
#Write a function:
#
#def solution(S)
#
#that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#
#For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [0..200,000];
#string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#Analysis
#Detected time complexity:
#O(N)
#expand allExample tests
#▶ example1
#example test 1 ✔OK
#▶ example2
#example test 2 ✔OK
#expand allCorrectness tests
#▶ negative_match
#invalid structures ✔OK
#▶ empty
#empty string ✔OK
#▶ simple_grouped
#simple grouped positive and negative test, length=22 ✔OK
#expand allPerformance tests
#▶ large1
#simple large positive test, 100K ('s followed by 100K )'s + )( ✔OK
#▶ large2
#simple large negative test, 10K+1 ('s followed by 10K )'s + )( + () ✔OK
#▶ large_full_ternary_tree
#tree of the form T=(TTT) and depth 11, length=177K+ ✔OK
#▶ multiple_full_binary_trees
#sequence of full trees of the form T=(TT), depths [1..10..1], with/without some brackets at the end, length=49K+ ✔OK
#▶ broad_tree_with_deep_paths
#string of the form [TTT...T] of 300 T's, each T being '{{{...}}}' nested 200-fold, length=120K+ ✔OK

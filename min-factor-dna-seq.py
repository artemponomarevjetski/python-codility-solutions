#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:26:52 2020

@author: artemponomarev
"""
S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]


def solution(S, P, Q):
    # write your code in Python 3.6
    """ 
    Task description is given on Codility website, https://app.codility.com/
    minimal factor for among DNA bases in all DNA sequences
    """
    N = len(S)
    M = len(P)

    if N<=max(max(P),max(Q)):
        return 0
    if N==0 or M==0:
        return 0
    if not (N>=1 and N<=1e5):∑
        return 0
    if not (M>=1 and M<=5e4):
        return 0

    A=[[i, P[i], Q[i]] for i in range(M)]
    A=sorted(A, key=lambda x: x[1])
    S=S[A[0][1]:]
    B=[-1]*M
    for i in range(M):
        C=S[0:A[i][2]-A[i][1]+1]
        if 'A' in C:
            B[i]=1
        elif 'C' in C:
            B[i]=2
        elif 'G' in C:
            B[i]=3
        else:
            B[i]=4
        if i<M-1:
            S=S[A[i+1][1]-A[i][1]:]

    C=[0]*M
    for i in range(M):
        C[A[i][0]]=B[i]

    return C

# main()
print("result  = ", solution(S, P, Q))
#
#Task description
#A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?
#
#The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).
#
#For example, consider string S = CAGCCTA and arrays P, Q such that:
#
#    P[0] = 2    Q[0] = 4
#    P[1] = 5    Q[1] = 5
#    P[2] = 0    Q[2] = 6
#The answers to these M = 3 queries are as follows:
#
#The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
#The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
#The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
#Write a function:
#
#def solution(S, P, Q)
#
#that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.
#
#Result array should be returned as an array of integers.
#
#For example, given the string S = CAGCCTA and arrays P, Q such that:
#
#    P[0] = 2    Q[0] = 4
#    P[1] = 5    Q[1] = 5
#    P[2] = 0    Q[2] = 6
#the function should return the values [2, 4, 1], as explained above.
#
#Write an efficient algorithm for the following assumptions:
#
#N is an integer within the range [1..100,000];
#M is an integer within the range [1..50,000];
#each element of arrays P, Q is an integer within the range [0..N − 1];
#P[K] ≤ Q[K], where 0 ≤ K < M;
#string S consists only of upper-case English letters A, C, G, T.
#Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#
#Analysis
#Detected time complexity:
#O(N + M)
#expand allExample tests
#▶ example
#example test ✔OK
#expand allCorrectness tests
#▶ extreme_sinlge
#single character string ✔OK
#▶ extreme_double
#double character string ✔OK
#▶ simple
#simple tests ✔OK
#▶ small_length_string
#small length simple string ✔OK
#▶ small_random
#small random string, length = ~300 ✔OK
#expand allPerformance tests
#▶ almost_all_same_letters
#GGGGGG..??..GGGGGG..??..GGGGGG ✔OK
#▶ large_random
#large random string, length ✔OK
#▶ extreme_large
#all max ranges ✔OK
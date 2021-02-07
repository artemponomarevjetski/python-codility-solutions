#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:11:11 2020

@author: artemponomarev
"""

END_TYPE = {'left end': 1, 'right end': -1}

def checks(A):
    """
    edge cases
    """
    N = len(A)
    if N == 0:
        return 0
    return 1

class Disc():
    """
    disk obj
    """
    def __init__(self, position, et):
        self.position = position
        self.et = et

def solution(A):
    """
    Task description is given on Codility website, https://app.codility.com/programmers/
    solution to overlapping disk problem
    """

    discs = []

    for i, item in enumerate(A):
        discs.append(Disc(i - item, END_TYPE['left end']))
        discs.append(Disc(i + item, END_TYPE['right end']))

    discs.sort(key=lambda disc: (disc.position, -disc.et))

    npairs = 0
    disc_overlaps = 0
    for entry in discs:
        disc_overlaps += entry.et
        if entry.et == END_TYPE['left end']:
            npairs += disc_overlaps - 1
        if npairs > 1e7:
            return -1

    return npairs

print(solution([1, 5, 2, 1, 4, 0]))

print(solution([0] * 100000))

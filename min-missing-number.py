##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Fri Feb  7 09:40:14 2020
#
#@author: artemponomarev
#"""
#
## codility test for Eversight
#

# Task description is given on Codility website, https://app.codility.com/programmers/

test = [3, 4, 6, 7, 9]

def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")

def determinant(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        builder = 0

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total

def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :returns: list of lists that form the matrix.
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M):
    """
    docstring here
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x,3)+0 for x in row])

def transpose(M):
    """
    Creates and returns a transpose of a matrix.
        :param M: The matrix to be transposed
        :return: the transpose of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def matrix_multiply(A,B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def check_matrix_equality(A,B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check
        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],tol) != round(B[i][j],tol):
                    return False

    return True

def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
        :return: The inverse of the matrix A
    """
    # Section 1: Make sure A can be inverted.
    check_squareness(A)
    check_non_singular(A)

    # Section 2: Make copies of A & I, AM & IM, to use for row operations
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    # Section 4: Make sure that IM is an inverse of A within the specified tolerance
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")

def solution(A):
    """
    smallest missing number
    """
    # write your code in Python 3.6
    debug = True
    result = -1
    if debug:
        pass
    else:
        res = -1

        if len(A) == 0:
            return 0

        if max(A) < 0:
            return 1

        B = A[:]
        B.sort()

        tally = [0]*(max(B)+1)
        for b in B:
            tally[b] += 1

        firstnonzero = 0
        for i, t in enumerate(tally):
            if t != 0:
                firstnonzero = i
                break

        tally = tally[firstnonzero:]
        for i, t in enumerate(tally):
            if t == 0:
                res = i
                break

        if res == -1:
            result = B[-1]+1
        else:
            result = res+firstnonzero

    return result

print("solution = ",solution(test))
#
#Analysis
#expand allExample tests
#▶ example1
#first example test ✔OK
#▶ example2
#second example test ✔OK
#▶ example3
#third example test ✔OK
#expand allCorrectness tests
#▶ extreme_single
#a single element ✘RUNTIME ERROR
#tested program terminated with exit code 1
#▶ simple
#simple test ✘RUNTIME ERROR
#tested program terminated with exit code 1
#▶ extreme_min_max_value
#minimal and maximal values ✘RUNTIME ERROR
#tested program terminated with exit code 1
#▶ positive_only
#shuffled sequence of 0...100 and then 102...200 ✘RUNTIME ERROR
#tested program terminated with exit code 1
#▶ negative_only
#shuffled sequence -100 ... -1 ✔OK
#expand allPerformance tests
#▶ medium
#chaotic sequences length=10005 (with minus) ✘WRONG ANSWER
#got 9968 expected 111
#▶ large_1
#chaotic + sequence 1, 2, ..., 40000 (without minus) ✘RUNTIME ERROR
#tested program terminated with exit code 1
#▶ large_2
#shuffled sequence 1, 2, ..., 100000 (without minus) ✘WRONG ANSWER
#got 99999 expected 50001
#▶ large_3
#chaotic + many -1, 1, 2, 3 (with minus) ✘RUNTIME ERROR
#tested program terminated with exit code 1

#Before you begin
#There are 3 tasks in the test. You can solve them in any order.
#There's no option to pause. Make sure you will not be interrupted for 40 minutes.
#Do not use any ready-made solution(s). Cheating is easy for us to discover.
#Play the game. Read our Code of Honour.
#Your solution(s) should consider all possible corner cases and handle large input efficiently. Passing the example test does not indicate that your solution is correct. The example test is not part of your final score.
#After finishing the test you will receive feedback containing your score. See example feedback.
#If you accidentally close your browser, use the invitation link to get back to your test.
#Hint: you can use your own IDE and use copy-paste, but make sure your solution compiles in Codility's environment.
#You can write your solution(s) in C, C++, C#, Go, Java 8, JavaScript, Kotlin, Lua, Objective-C, Pascal, Perl, PHP, Python, Ruby, Scala, Swift 4 or Visual Basic*.
#* the availability of the programming languages depends on the task, and in some tasks the choice of programming languages might be limited.
#The test will include multiple-choice questions.
'''
    Solution by Michel K. Buhendwa II
    BSc. Software Engineering
    University of Eastern Africa Baraton, Kenya

    Problem link: https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

    My solution is then obtained by:
        * sorting the array
        * checking if every two consecutive numbers are equal if not returning the first of the two
        * returning the last element of the sorted array in case the odd element is the largest

'''


def solution(A):
    A.sort()
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i + 1]:
            return A[i]
    return A[-1]

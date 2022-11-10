'''
    Solution by Michel K. Buhendwa II
    BSc. Software Engineering
    University of Eastern Africa Baraton, Kenya

    Problem link: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

    My solution is then obtained by:
        * finding the first occurrence of the longest possible [from size-2 down to 1] sequence of zeros
        * check if the character after that occurrence is a 1
        * return the length of that sequence

'''


def solution(A):
    A.sort()
    try:
        print("before: ", A)
        A = list(set(A[A.index(1):]))
        print("after: ", A)
    except ValueError:
        return 1
    for i in range(0, len(A)):
        print("n {0}  i {1}".format(i, A[i]))
        if A[i + 1] != A[i] + 1:
            return A[i] + 1

A = [5, 1, 3, 1, -4, -3, 4, 2]
print(solution(A))

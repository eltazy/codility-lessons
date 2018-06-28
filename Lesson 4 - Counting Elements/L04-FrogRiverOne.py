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


def solution(X, A):
    try:
        rep = A.index(X)
        for i in range(X, 0, -1):
            n = A.index(i)
            if n > rep:
                rep = n
    except ValueError:
        return -1
    return rep


A = [5,1,3,1,4,3,4]
print(solution(5, A))

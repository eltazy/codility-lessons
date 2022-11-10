'''
    Solution by Michel K. Buhendwa II
    BSc. Software Engineering
    University of Eastern Africa Baraton, Kenya

    Problem link: https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
'''


def solution(A):
    # empty list []
    if len(A) == 0:
        return 1
    # array [1]
    if len(A) == 1 and A[0] == 1:
        return 2
    # general case
    try:
        return (set(range(1, len(A) + 1)) - set(A)).pop()
    except KeyError:  # there is no difference between the sets
        return len(A) + 1

'''
    Solution by Michel K. Buhendwa II
    BSc. Software Engineering
    University of Eastern Africa Baraton, Kenya

    Problem link: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
'''


def solution(A):
    # # empty list []
    # if len(A) == 0:
    #     return 0
    # # array [1]
    # if len(A) == 1:
    #     return A[0]
    # # general case
    # diffs = []
    # for i in range(1, len(A)):
    #     diffs.append(abs(sum(A[:i]) - sum(A[i:])))
    # diffs.sort()
    # print(diffs)
    # return diffs[0]
    sumA = sum(A)
    diffs = []
    for i in range(1, len(A)):
        diffs.append(abs(sumA - sum(A[:i])))
        print(diffs)
    return min(diffs)


print(solution([-1000, 1000]))

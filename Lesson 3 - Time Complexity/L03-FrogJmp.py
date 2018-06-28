'''
    Solution by Michel K. Buhendwa II
    BSc. Software Engineering
    University of Eastern Africa Baraton, Kenya

    Problem link: https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
'''
import math


def solution(X, Y, D):
    return math.ceil((Y - X) / D)


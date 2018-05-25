'''
    Link: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
    For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
    No matter the value of K there is a finite set of outputs possible
    After rotating len(A) times the output is the same as the len(A) first times
    i.e. all naturals K having the same reminder modulo len(A) give the same output

    Our solution is then obtained by:
        * splitting the array at its K-th [K%len(A)-th] element [3, 8] and [9, 7, 6]
        * merging those arrays in reverse [9, 7, 6, 3, 8]

'''


def solution(A, K):
    # extreme case: empty array A given
    if len(A) == 0:
        return A
    # easy case: number of turn is a full cycle
    if K % len(A) == 0:
        return A
    # general case
    new_start_index = len(A)-(K % len(A))
    return A[new_start_index:]+A[:new_start_index]
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


def solution(N):
    # get and store binary notation of N as a string
    bin_str = "{0:b}".format(N)
    # for the longest possible sequence
    for i in range(len(bin_str) - 2, 0, -1):
        search_str = "0" * i
        found_at = bin_str.find(search_str)
        # if sequence of zeros of length i was found AND
        # is not at the end of the binary notation AND
        # the character after it is a 1 then return the length i of the sequence
        if found_at != -1 and found_at + i + 1 <= len(bin_str) and bin_str[found_at + i] == "1":
                return i
    return 0

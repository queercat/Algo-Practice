"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. 
"""

def check_permutation(s0, s1):
    s0 = sorted(s0)
    s1 = sorted(s1)

    return s0 == s1
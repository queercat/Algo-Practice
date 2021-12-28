"""
Example: Given a smaller string s and a bigger string b, 
design an algorithm to find all permutations of the shorter 
string within the longer one. Print the location of each permutation. 
"""

""" constraints
len(s) < len(b)
"""

"string abbacabbaabbabaabaaabaaabbaababaaabaa"
"substr abba"

"sorted(string[i:len(abba)) + i] == sorted(substr)"

def permutations_of_substr(s, b):
    perms = []
    sorted_s = sorted(s)

    for i in range(0, len(b) - len(s)):
        if sorted(b[i:len(s) + i]) == sorted_s:
            perms.append(i)

    return perms
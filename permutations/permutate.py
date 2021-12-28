"""
Example: Given a string find and print all permutations of that string
"""

"""Base case and build...
Solve from increasing cases.

string=a: [a]
string=ab: [ab, ba]
string=abc: [cab, acb, abc]
"""

def permutate_string(string: str) -> list:
    permutations = []
    
    if len(string) <= 1:
        return string

    perms = [string[0:len(string) - 1]]

    for perm in perms:
        for char in range(len(perm) + 1):
            perm(perm[0:char] + string[-1] + perm[char:len(perm)])

permutate_string("abcd")
"""1.9
String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, s1 and s0, write code to check if s0 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
"""

"""constraints
ordering matters
can't sort strings
s0 < s1

s0: erbottlewat
s1: waterbottlewaterbottle

algeba!!!
"""

def is_substr(s0: str, s1: str):
    """returns if s0 is a substring of s1"""
    
    return (s1.find(s0) > 0)

def is_rotation(s0: str, s1: str):
    return is_substr(s0, s1 * 2)
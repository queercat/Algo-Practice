"""1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

def is_unique(s: str) -> bool:
    visited = []
    
    for c in s:
        if c in visited:
            return False
        else:
            visited.append(c)

    return True

print(is_unique('abcdefghijklmnopqrstuvwxyz'))